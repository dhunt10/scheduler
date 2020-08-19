from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
from main_class import Scheduler
from person import person

app = Flask(__name__)
api = Api(app)

model = Scheduler()

class HealthCheck(Resource):

    def get(self):
        return {'status{}': 'alive{}'}, 200


class get_avail_times(Resource):
    def __init__(self):
        """

        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('club',
                           type=str,
                           required=True,
                           help='What Club Are You A Member At')
        parser.add_argument('date',
                           type=str,
                           required=True,
                           help='Date is in MM/DD/YYYY format')
        self.parser = parser


    def get(self):
        """
        """

        args = self.parser.parse_args()
        result = model.get_avail_times(club=args.club, date=args.date)
        return result

class make_appt(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_erros=True)
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='name of applicant')
        parser.add_argument('club',
                            type=str,
                            required=True,
                            help='name of applicants club')
        parser.add_argument('email',
                            type=str,
                            required=True,
                            help='email of applicant')
        parser.add_argument('phone',
                            type=str,
                            required=False,
                            help='phone number of applicant')
        parser.add_argument('date',
                            type=str,
                            required=True,
                            help='Date is in MM/DD/YYYY format')
        parser.add_argument('time',
                            type=str,
                            required=True,
                            help='time is 24 hr format')

        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        customer = person()
        customer.name = args.name
        customer.club = args.club
        customer.email = args.email
        customer.phone = args.phone
        result = model.make_appt(customer, time=args.time, date=args.date)
        return result

class get_dates(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('club',
                            type=str,
                            required=True,
                            help='club of available dates')
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        result = model.get_avail_dates(args.club)
        return result

api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(get_avail_times, '/at')
api.add_resource(make_appt, '/ma')
api.add_resource(get_dates, '/gd')

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
