import unittest
import sqlite3
import hashlib

# Import the LoginService class from your module
from LoginService import LoginService

class TestLoginService(unittest.TestCase):
    def setUp(self):

        self.login_service = LoginService()



    def test_verify_correct_password(self):
        self.assertTrue(self.login_service.verify_password('testUser1', 'password'))

    def test_verify_incorrect_password(self):
        self.assertFalse(self.login_service.verify_password('testUser1', 'wrong_password'))

    def test_verify_nonexistent_user(self):
        self.assertFalse(self.login_service.verify_password('nonexistent_user', 'any_password'))

if __name__ == '__main__':
    unittest.main()
