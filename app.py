from flaskimport Flask, request, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class HealthCheck(Resource):
    def get(self):
        return {'status': 'alive'}, 200


class get_avail_times(Resource):
    def __init__(self):
        """
        """
        parser = reqparse.Requestparser(bundle_errors=True)
        parse.add_argument('club',
                           type=str,
                           required=True,
                           help='What Club Are You A Member At')
        parse.add_argument('date'
                           type=str,
                           required=True,
                           help='Date is in MM/DD/YYYY format')
        self.parser = parser


        def get(self):
            """
            """

            args = self.parser.parse_args()
            result = model.get_avail_times()
            return result
