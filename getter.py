from data_process import *

def get_avail_times(club, date):
    open_dates = []
    data = load_data()

    date = date_to_data_form(date)

    for i in data[club][date]:
        if data[club][date][i] == None:
            open_dates.append(i)

    return open_dates

def get_avail_dates(club):
    open_dates = []
    data = load_data()

    for i in data[club]:
        open_dates.append(data_from_to_date(i))

    return open_dates
