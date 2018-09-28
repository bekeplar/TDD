import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User( "Joseph Bekalaze", 25,"male","bekeplar","bekeplar@gmail.com","9bekalZ+w")

    def test_check_email(self):
        pass