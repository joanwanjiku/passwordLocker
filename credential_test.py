import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    All the test cases for the class credentials
    """
    def setUp(self):
        """
        method that runs before each testcase
        """
        self.new_credential = Credentials("twitter", "jojoOne", "123456")

    def tearDown(self):
        """
        method that cleans up after each testcase
        """
        Credentials.credential_list = []

    def test_init(self):
        """
        test if the object has been initialized properly
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
        check whether the credentials have been added to the list
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        self.assertEqual(len(Credentials.credential_list), 2)

    def test_delete_credential(self):
        """
        check whether the credentials have been removed from the list
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        another_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_find_by_app_name(self):
        """
        check whether we can find credentials by the app_name
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        found_credentials = another_credential.find_by_app_name("facebook")
        self.assertEqual(found_credentials.username, another_credential.username)

    def test_display_all_credentials(self):
        """
        test method to check whether all credentials in the list are being displayed
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)

    def test_whether_credential_exist(self):
        """
        test to check if credential exist
        """
        self.new_credential.save_credential()
        another_credential = Credentials("facebook", "jojoOne","7891011")
        another_credential.save_credential()

        present_credential = another_credential.check_if_exists("facebook")
        self.assertTrue(present_credential)
