import unittest

def fruits(*args):
    return list(args)



class TestFruitsList(unittest.TestCase):
    """
        Testing the function fruits.
    """

    def test_fruits(self):
        fruits_data = fruits("apple", "orange", "mango")
        for data in fruits_data:
            self.assertIn(data, fruits_data)


if __name__ == "__main__":
    unittest.main()
