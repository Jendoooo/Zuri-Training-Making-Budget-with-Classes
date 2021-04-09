import datetime
import time
import random

TimeDisplay = datetime.datetime.now()

UserDatabase = {"olajide": "passwordolajide",
                "ayeola": "passwordayeola",
                "hafeez": "passwordhafeez"}

account_status = random.randint(5000, 1000000)


def login():
    username = str(input("Please enter your Username: \n"))
    password = str(input("Please enter your password: \n"))

    if(username in UserDatabase.keys()) and password in UserDatabase.values():
        print(UserDatabase.values())
        print(UserDatabase.keys())
        print("Time:  " + TimeDisplay.strftime("%Y-%m-%d %H:%M:%S"))
        print("Welcome " + username)
        return True
    else:
        print("Login Failed!! Username or Password Incorrect. Please try again later")
        return False


def register():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")

    account_type = {"1": "Savings",
                    "2": "Current",
                    "3": "Fixed Deposit"}
    print(account_type)
    account = str(input(" From the above, What type of account do you want to create ? "))
    if account in account_type:
        print(" Your {} account will  be created shortly. ".format(account_type[account]))
        time.sleep(3)
        account_number = random.randint(1111111111, 9999999999)
        print("Hello {} {}, your account has been created with "
              "account number : {}".format(firstname, lastname, account_number))
        print("You can start carrying out transactions as from tomorrow.")
        print("Have a good day.")
        return True
    else:
        return False


def operation():
    activity = int(input("Hello, these are the available options:\n"
                         "1: Withdrawal\n"
                         "2: Cash Deposit\n"
                         "3: Complaint\n"))
    if activity == 1:
        cash = int(input("You have {} Naira. How much would you like to withdraw ? ".format(account_status)))
        if cash < account_status:
            balance = account_status - cash
            print("Take your {} Naira cash. You have {} Naira left ".format(cash, balance))
        while cash >= account_status:
            print("Please choose an ammount below {}".format(account_status))
            cash = int(input("You have {} Naira. How much would you like to withdraw ? ".format(account_status)))
            if cash < account_status:
                balance = account_status - cash
                print("Take your {} Naira cash. You have {} Naira left ".format(cash, balance))
                print("Thank you for banking with us. Have a good day. ")
                break

    elif activity == 2:
        cash = int(input("How much would you like to deposit ? "))
        balance = account_status + cash
        print("You deposited {} Naira and have a current balance of {} Naira ".format(cash, balance))
    elif activity == 3:
        input("What issue would you like to report ? \t")
        print("Thank you for contacting us. We will take actions and get back to you shortly.\n"
              "Have a nice day")
    else:
        print("Invalid Option selected, please try again")


def main():
    welcome = int(input("Hello!, What would you like to do today ? \n"
                        "1. Login\n"
                        "2. Register a new account. \n"
                        "0. Exit\n"))

    print(welcome)

    if welcome == 1:
        # login()
        if login():
            print("stuff = true")
            operation()

    elif welcome == 2:
        isregistersuccessful = False

        while not isregistersuccessful:
            isregistersuccessful = register()

    elif welcome == 0:
        print("Have a good day")

    else:
        print("Invalid Selection. Try again later ")


main()
