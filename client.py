from person import person
from data_process import update_now, load_data

def log_in():
    username = input("What is your username")
    psswrd = input("What is your password")

    user_list = load_data("resources/usernames.txt")
    user_data = load_data("resources/userdata.txt")

    if user_list[username] != psswrd:
        return "Invalid Password"

    else:
        return user_data[username]

def make_account():

    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    club = input("Club: ")

    user_list = load_data("resources/usernames.txt")
    user_data = load_data("resources/userdata.txt")

    newman = Person(name, email, phone, club)

    key_value, username = make_user()

    user_list.update(key_value)
    user_data.update({username : newman})

    update_now(user_list, "resources/usernames.txt")
    update_now(user_data, "resources/userdata.txt")

    return "Account has been made"

def make_user():
    username = input("Username: ")
    users = load_data("resources/usernames.txt")

    if username in users:
        make_user()

    psswrd = input("Password: ")
    repeat = input("Confirm Password: ")

    if psswrd != repeat:
        make_user()

    key_value = {username: psswrd}

    return key_value, username
