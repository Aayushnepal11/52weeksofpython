import unittest

def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

class TestFormattedName(unittest.TestCase):
    """
        Testing the function formatted name
    """

    def test_formatted_name(self):
        """
            return: first_name and last_name
        """
        name = formatted_name("aayush","nepal")
        self.assertEqual(name, "Aayush Nepal")
    
    def test_formatted_name_middle(self):
        """
            rteuns: first_name middle_name last_name
        """
        name = formatted_name("ram", "dhakal", "parsad")
        self.assertEqual(name, "Ram Parsad Dhakal")

if __name__ == '__main__':
    unittest.main()



