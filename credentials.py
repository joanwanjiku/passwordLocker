class Credentials:
    """
    Describes the attributes and methods of the class credentials
    """
    credential_list = []

    def __init__(self, app, user, password):
        """

        :param app:
        :param user:
        :param password:
        """
        self.app_name = app
        self.username = user
        self.password = password

    def save_credential(self):
        """

        :return:
        """
        Credentials.credential_list.append(self)

    def delete_credential(self):
        """

        :return:
        """
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_app_name(cls, name):
        """

        :param name: appname
        :return: credentials
        """
        for credentials in cls.credential_list:
            if credentials.app_name == name:
                return credentials

    @classmethod
    def display_credentials(cls):
        """

        :return:
        """
        return cls.credential_list

    @classmethod
    def check_if_exists(cls, name):
        """

        :param name:
        :return:
        """
        for credential in cls.credential_list:
            if credential.app_name == name:
                return True
        return False
