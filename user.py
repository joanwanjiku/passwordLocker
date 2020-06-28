import json


class User:
    """
    Describes the behaviours of the class user
    """
    def __init__(self, name, password):
        """

        """
        self.name = name
        self.password = password

    def store_user_in_a_text_document(self):
        user = {
            'name': self.name,
            'password': self.password
        }
        with open('user.txt', 'w') as file:
            json.dump(user, file)
