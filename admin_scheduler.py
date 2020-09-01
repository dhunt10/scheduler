from data_process import *
import datetime
from helpers import *
from person import person
import os


class adminScheduler(object):

    def __init__(self):
        """

        Initialization
        """

    def make_timeset(self, start, end):
        day = {}
        if start >= end:
            return 'Invalid Day Selection'

        for i in range(start, end):
            for x in ("00","15","30","45"):
                day[str(str(i) + ":" + str(x))] = None

        return day

    def make_day(self, day, start, end):
        time_list = self.make_timeset(start, end)
        day = datetime.datetime.strptime(day, "%m/%d/%Y")
        new_day = {day : time_list}
        return new_day

    def add_day(self, day, club, start, end):
        curr_schedule = load_data()
        day = self.make_day(day, start, end)
        try:
            curr_schedule[club_name(club)].update(day)
        except KeyError:
            return 'Club Does Not Exist'

        update_now(curr_schedule)
        return "day made on {} from {} to {} at {}".format(day, start, end, club)

    def make_club(self, club):
        curr_schedule = load_data()
        if curr_schedule == '':
            curr_schedule = dict()
        club = club_name(club)
        if club not in curr_schedule:
            curr_schedule[club] = {}
            update_now(curr_schedule)
            return "{} has been created".format(club)
        else:
            return 'That club already exists, try another name'

    def make_appt(self, person, time, date):
        curr_schedule = load_data()
        date = date_to_data_form(date)
        if curr_schedule[person.club][date][time] == None:
            person_list = [person.name, person.phone, person.email]
            curr_schedule[person.club][date][time] = person_list
            update_now(curr_schedule)
            return "Confirmed for {}, at {}".format(date, time)
        else:
            return "Time is no longer available"

    def get_avail_times(self, club, date):
        open_dates = []
        data = load_data()

        date = date_to_data_form(date)
        club = club_name(club)
        try:
            data[club][date]
        except KeyError:
            return []

        for i in data[club][date]:
            if data[club][date][i] == None:
                open_dates.append(i)

        return open_dates

    def get_avail_dates(self, club):
        open_dates = []
        data = load_data()

        club = club_name(club)
        try:
            data[club]
        except KeyError:
            return []

        for i in data[club]:
            open_dates.append(data_form_to_date(i))

        return open_dates

    def get_current_appts(self, club, date):
        data = load_data()
        appts = []
        date = date_to_data_form(date)
        club = club_name(club)

        try:
            data[club][date]
        except KeyError:
            return []

        for i in data[club]:
            appts.append(data_form_to_date(i))

        return appts

    def del_date(self, club, date):
        data = load_data()

        try:
            data[club_name(club)].pop(date_to_data_form(date))
        except KeyError:
            return "{} is not a valid date at {}".format(date, club)

        update_now(data)
        return "{} has been deleted from {}".format(date, club)

    def del_club(self, club):
        data = load_data()
        try:
            data.pop(club_name(club))
        except KeyError:
            return "No Club named {}".format(club)
        update_now(data)
        return "{} has been deleted".format(club)