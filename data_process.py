import datetime

def load_data(path="resources/data_set.txt"):
        try:
            data = eval(open(path, 'r').read())
        except SyntaxError:
            return ''
        return data

def update_now(data_set, path = "resources/data_set.txt"):
        f = open(path, "w")
        f.write(str(data_set))
        f.close()

def date_to_data_form(date):
    return datetime.datetime.strptime(date, "%m/%d/%Y")

def data_form_to_date(data):
    return ("{}/{}/{}".format(data.month, data.day, data.year))

