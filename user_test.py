import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    All test cases for the class user
    """
    def setUp(self):
        """
        method that runs before each testcase
        """
        self.new_user = User("Joan", "foobar")

    def test_init(self):
        """
        tests whether the object has been initialized properly
        """
        self.assertEqual(self.new_user.name, "Joan")
        self.assertEqual(self.new_user.password, "foobar")


