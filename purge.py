import datetime
from main_class import load_data, update_now 


def get_date():
    date = datetime.datetime.now()
    #return ("{}/{}/{}".format(date.month, date.day, date.year))
    return date

def purger():

    data = load_data()
    curr = get_date()
    for club in list(data):
        for date in list(data[club]):
            #past = datetime.datetime.strptime(date, "%m/%d/%Y")
            if date < curr:
                data[club].pop(date)
    update_now(data)
