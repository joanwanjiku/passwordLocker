from user import User
from credentials import Credentials
import random


def create_user(name, password):
    user = User(name, password)
    return user


def create_credential(app, user, password):
    new_credential = Credentials(app, user, password)
    return new_credential


def save_credentials(credential):
    return Credentials.save_credential(credential)


def delete_credential(credential):
    return Credentials.delete_credential(credential)


def find_credentials_by_app_name(name):
    return Credentials.find_by_app_name(name)


def display_credentials():
    return Credentials.display_credentials()


def main():
    print("Hi Welcome to your password locker. Create your login credentials")
    name = input("Name: ")
    password = input("Password: ")

    print(name + " " + password)
    print(name + " What do you want to achieve? ")
    print('\n')
    while True:
        print("For adding a credential, type:- add\nFor displaying all credentials, type:- display\nFor finding credentials, type:- find")
        print('\n')
        code_word = input('Enter the code word: ').lower()

        if code_word == 'add':
            print('You have chosen to add ..')
            print('\n')
            app_name = input('Application name ...')
            username = input('Username ...')
            pass_option = input("Do you want to generate a random password? Yes/No: ").lower()

            if pass_option == 'yes':
                with open('random.txt', 'r') as file:
                    lines = file.read()
                    line_list = lines.split()
                filtered_list = list(filter(lambda x: len(x) > 6, line_list))
                random_index = random.randint(3, 15)
                password = filtered_list[random_index]
                save_credentials(create_credential(app_name, username, password))

                print('New credential created app: %s username: %s password: %s' % (app_name, username, password))

            elif pass_option == 'no':
                password = input('Enter Password ...')
                save_credentials(create_credential(app_name, username, password))

                print('New credential created app: %s username: %s password: %s' % (app_name, username, password))

            else:
                print('Try again..')

        elif code_word == 'display':
            print('You have chosen to display')
        elif code_word == 'find':
            print('You have chosen to find')
        else:
            print('Exiting...')
            break




if __name__ == '__main__':
    main()
