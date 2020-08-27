from data_process import *
from helpers import *
import datetime
from person import person
import os


class Scheduler(object):

    def __init__(self):
        """

        Initialization
        """

    def make_appt(self, person, time, date):
        curr_schedule = load_data()
        date = date_to_data_form(date)
        if curr_schedule[club_name(person.club)][date][time] == None:
            person_list = [person.name, person.phone, person.email]
            curr_schedule[club_name(person.club)][date][time] = person_list
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
