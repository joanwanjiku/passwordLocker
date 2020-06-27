import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    All the test cases for the class credentials
    """
    def setUp(self):
        """
        Run before each test case
        """
        self.new_credential = Credentials("twitter", "jojoOne", "123456")

    def tearDown(self):
        """

        :return:
        """
        Credentials.credential_list = []

    def test_init(self):
        """

        """
        self.assertEqual(self.new_credential.app_name, "twitter")
        self.assertEqual(self.new_credential.username, "jojoOne")
        self.assertEqual(self.new_credential.password, "123456")

    def test_save_credentials(self):
        """

        :return:
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_save_more_credentials(self):
        """

        :return:
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        self.assertEqual(len(Credentials.credential_list), 2)

    def test_delete_credential(self):
        """

        :return:
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        another_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_find_by_app_name(self):
        """

        :return:

        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        found_credentials = another_credential.find_by_app_name("facebook")
        self.assertEqual(found_credentials.username, another_credential.username)

    def test_display_all_credentials(self):
        """

        :return:
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)
