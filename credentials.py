class Credentials:
    """
    Describes the attributes and methods of the class credentials
    """
    credential_list = []

    def __init__(self, app, user, password):
        """
        method that initializes the attributes of the class Credeentials
        :param app:
        :param user:
        :param password:
        """
        self.app_name = app
        self.username = user
        self.password = password

    def save_credential(self):
        """
        method that add credentials object to the credential_list
        """
        Credentials.credential_list.append(self)

    def delete_credential(self):
        """
        method that deletes credentials object from the credential_list
        """
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_app_name(cls, name):
        """
        method that takes in a name as a parameter and returns the credentials that matches the app_name
        :param : app_name
        :return: credentials
        """
        for credentials in cls.credential_list:
            if credentials.app_name == name:
                return credentials

    @classmethod
    def display_credentials(cls):
        """
        method that displays all the credentials in the credential_list
        """
        return cls.credential_list

    @classmethod
    def check_if_exists(cls, name):
        """
        method that takes in a name as parameter and returns true if the credentials that match the name exist
        :param name:app_name
        :return: boolean
        """
        for credential in cls.credential_list:
            if credential.app_name == name:
                return True
        return False
