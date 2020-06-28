from user import User
from credentials import Credentials
import random
import json


def create_user(name, password):
    user = User(name, password)
    return user


def add_user(user):
    return user.store_user_in_a_text_document()


def read_text_file(text_file):
    with open(text_file, 'r') as json_file:
        data = json_file.read()
        user = json.loads(data)
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


def check_existence(name):
    return Credentials.check_if_exists(name)



def main():
    print("Hi Welcome to your password locker.")
    name = input("Enter your name: ")

    data = read_text_file('user.txt')
    # print(data)
    if name == data['name']:
        password = input('Enter Your password: ')
        if password != data['password']:
            print('Wrong Password, Try again')
        else:
            print("Welcome %s  What do you want to achieve? " %(name))
            while True:
                print("For adding a credential, type:- add\nFor displaying all credentials, type:- display\nFor finding credentials, type:- find\nFor deleting credentials, type:- delete")
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
                        generated_password = filtered_list[random_index]
                        save_credentials(create_credential(app_name, username, generated_password))

                        print('New credential created app: %s username: %s password: %s' % (app_name, username, generated_password))
                        print('\n')

                    elif pass_option == 'no':
                        entered_password = input('Enter Password ...')
                        save_credentials(create_credential(app_name, username, entered_password))

                        print('New credential created app: %s username: %s password: %s' % (app_name, username, entered_password))
                        print('\n')

                    else:
                        print('Try again..')
                        print('\n')

                elif code_word == 'display':
                    if display_credentials():
                        print('List of all credentials..')
                        for credential in display_credentials():
                            print('%s %s' % (credential.app_name, credential.username))
                        print('\n')

                    else:
                        print('You have not added any credentials')
                        print('\n')

                elif code_word == 'find':
                    print('You have chosen to find')

                    name_search = input('Enter the application name: ').lower()
                    if check_existence(name_search):
                        credentials = find_credentials_by_app_name(name_search)
                        print('Found .. %s username: %s password: %s' % (credentials.app_name, credentials.username, credentials.password))
                        print('\n')
                    else:
                        print('No such application, Try Again')

                elif code_word == 'delete':
                    name_of_app = input('Enter the application name for which you want to delete credentials: ')
                    if check_existence(name_of_app):
                        credentials = find_credentials_by_app_name(name_of_app)
                        delete_credential(credentials)
                        print('Deleted %s successfully' % credentials.app_name)
                        print('\n')
                    else:
                        print('No such application, Try Again')

                else:
                    print('Exiting...')
                    break

    else:
        password = input('User not found, Enter password for to create account: ')
        add_user(create_user(name, password))
        print('\n')
        print("Welcome %s  What do you want to achieve? " %(name))

        while True:
            print("For adding a credential, type:- add\nFor displaying all credentials, type:- display\nFor finding credentials, type:- find\nFor deleting credentials, type:- delete")
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
                    generated_password = filtered_list[random_index]
                    save_credentials(create_credential(app_name, username, generated_password))

                    print('New credential created app: %s username: %s password: %s' % (app_name, username, generated_password))
                    print('\n')

                elif pass_option == 'no':
                    entered_password = input('Enter Password ...')
                    save_credentials(create_credential(app_name, username, entered_password))

                    print('New credential created app: %s username: %s password: %s' % (app_name, username, entered_password))
                    print('\n')

                else:
                    print('Try again..')
                    print('\n')

            elif code_word == 'display':
                if display_credentials():
                    print('List of all credentials..')
                    for credential in display_credentials():
                        print('%s %s' % (credential.app_name, credential.username))
                    print('\n')

                else:
                    print('You have not added any credentials')
                    print('\n')

            elif code_word == 'find':
                print('You have chosen to find')

                name_search = input('Enter the application name: ').lower()
                if check_existence(name_search):
                    credentials = find_credentials_by_app_name(name_search)
                    print('Found .. %s username: %s password: %s' % (credentials.app_name, credentials.username, credentials.password))
                    print('\n')
                else:
                    print('No such application, Try Again')

            elif code_word == 'delete':
                name_of_app = input('Enter the application name for which you want to delete credentials: ')
                if check_existence(name_of_app):
                    credentials = find_credentials_by_app_name(name_of_app)
                    delete_credential(credentials)
                    print('Deleted %s successfully' % credentials.app_name)
                    print('\n')
                else:
                    print('No such application, Try Again')

            else:
                print('Exiting...')
                break


        print('\n')





if __name__ == '__main__':
    main()
