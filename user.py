import json


class User:
    """
    Describes the behaviours of the class user
    """
    def __init__(self, name, password):
        """
        method that initializes the attributes of the class User
        """
        self.name = name
        self.password = password

    def store_user_in_a_text_document(self):
        """
        method that writes the user's name and password to a text-file
        """
        user = {
            'name': self.name,
            'password': self.password
        }
        with open('user.txt', 'w') as file:
            json.dump(user, file)
