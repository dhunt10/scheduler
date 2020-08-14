from person import person
import os

class Scheduler(object):

    def __init__(self):
        """

        Initialization
	"""

    def make_timeset(self, start, end):
        day = {}
        for i in range(start, end+1):
            for x in ("00","15","30","45"):
                day[str(str(i) + ":" + str(x))] = None

        return day

    def make_day(self, day, start, end):
        time_list = self.make_timeset(start, end)
        new_day = {day : time_list}
        return new_day

    def add_day(self, day, club, start, end):
        curr_schedule = self.load_data()
        day = self.make_day(day, start, end)
        print(curr_schedule, type(curr_schedule))
        curr_schedule[club].update(day)
        self.update_now(curr_schedule)

    def load_data(self, path="resources/data_set.txt"):
        try:
            data = eval(open(path, 'r').read())
        except SyntaxError:
            return ''
        return data

    def make_club(self, club):
        curr_schedule = self.load_data()
        if curr_schedule == '':
            curr_schedule = dict()
            print("ye")
        if club not in curr_schedule:
            curr_schedule[club] = {}
        self.update_now(curr_schedule)


    def make_appt(self, person, time, date):
        curr_schedule = self.load_data()
        if curr_schedule[person.club][date][time] == None:
            person_list = [person.name, person.phone, person.email]
            curr_schedule[person.club][date][time] = person_list
            self.update_now(curr_schedule)
            return "Confirmed for {}, at {}".format(date, time)
        else:
            return "Time is no longer available"

    def update_now(self, data_set, path = "resources/data_set.txt"):
        f = open(path, "w")
        f.write(str(data_set))
        f.close()
