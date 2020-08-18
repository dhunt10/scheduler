from data_process import *

def get_avail_times(club, date):
    open_dates = []
    data = load_data()

    date = date_to_data_form(date)

    for i in data[club][date]:
        if data[club][date][i] == None:
            open_dates.append(i)

    return open_dates
