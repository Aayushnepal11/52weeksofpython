import unittest

def numbers(*args):
    return args


class TestNumbers(unittest.TestCase):
    """
        Testing the numbers function that returns an interger.
    """

    def test_numbers(self):
        """
            returns numbers tuples.
        """
        user_numbers = numbers(1, 2,3,4,5,6,7,8,9,10)
        for number in user_numbers:
            self.assertIn(number, user_numbers) 


if __name__ == '__main__':
    unittest.main()


