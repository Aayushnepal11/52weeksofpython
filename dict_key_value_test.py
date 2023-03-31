import unittest

def user_profile(**kwargs):
    return kwargs


class TestUserProfile(unittest.TestCase):
    """
        Testing the function the user_profile.
    """

    def test_user_profile_key(self):
        user_data = user_profile(name='aayush nepal', age=21, is_active=True)
        for data in user_data.keys():
            self.assertIn(data, user_data.keys())

    def test_user_profile_values(self):
        user_data = user_profile(name='aayush nepal', age=21, is_active=True)
        for data in user_data.values():
            self.assertIn(data, user_data.values())

if __name__ == '__main__':
    unittest.main()