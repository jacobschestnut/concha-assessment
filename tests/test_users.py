import unittest
from src.views import get_all_users

class TestCaseBase(unittest, TestCase):
    def assertExists(self, user):
        if not (user['first_name']):
            userId = user['id']
            raise AssertionError(f'first_name does not exist in userId: {userId}')
        if not (user['last_name']):
            userId = user['id']
            raise AssertionError(f'last_name does not exist in userId: {userId}')
        if not (user['email']):
            userId = user['id']
            raise AssertionError(f'email does not exist in userId: {userId}')
        if not (user['address']):
            userId = user['id']
            raise AssertionError(f'address does not exist in userId: {userId}')
        if not (user['profile_image']):
            userId = user['id']
            raise AssertionError(f'profile_image does not exist in userId: {userId}')       
        
class TestUserInfo(TestCaseBase):
    def test_exists(self):
        #tests to make sure all user data exists
        users = get_all_users()
        for user in users:
            self.assertExists(user)