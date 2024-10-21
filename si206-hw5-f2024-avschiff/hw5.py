# Name: 
# Student ID: 
# Email: 
# List who you have worked with on this homework: 
# List any AI tool (e.g. ChatGPT, GitHub Copilot): 

import re
import os
import unittest
from datetime import datetime
import tempfile

def get_user_info(file_name: str) -> list:
    """
    This function reads the file and returns a list of strings.
    Each string should contain all the information about one user.

    Args:
        file_name (str): The name of the file containing user data.

    Returns:
        user_data (list): A list of strings with each user's information.
    """
    file = open(file_name, 'r')
    user_info = []
    for line in file:
        user_info.append(line.strip())
    file.close()
    return user_info

def create_age_dict(user_data: list) -> dict:
    """
    This function takes a list of user information strings and returns a dictionary
    using usernames as keys and storing their birthday and age as of October 25, 2024.

    Args:
        user_data (list): A list of strings with each user's information.

    Returns:
        age_dict (dict): A dictionary with usernames as keys and a tuple of 
                         (birthday, age) as values.
    """
    user_dict = {}
    for user in user_data:
        username = re.search(r'@cc0uNT;(\w+)', user).group(1)
        birthday_str = re.search(r'birthday seems to be (\d{2}/\d{2}/\d{4})', user).group(1)
        birthday = datetime.strptime(birthday_str, '%m/%d/%Y')
        age = (datetime(2024, 10, 25) - birthday).days // 365
        user_dict[username] = (birthday_str, age)
    return user_dict

def check_password_strength(user_data: list) -> tuple:
    """
    This function evaluates each user's password strength and returns a tuple containing
    the password and its strength classification.

    Args:
        user_data (list): A list of strings with each user's information.

    Returns:
        password_strengths (tuple): A tuple with passwords and their strength classification.
    """
    password_strengths = []
    for user in user_data:
        password = re.search(r'P455W0RD:([a-zA-Z0-9!@#$%^&*()]+)', user).group(1)
        if len(password) >= 10 and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*()]', password):
            strength = 'strong'
        elif len(password) >= 8 and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
            strength = 'medium'
        elif len(password) >= 6:
            strength = 'weak'
        else:
            strength = 'very weak'
        password_strengths.append((password, strength))
    return tuple(password_strengths)

def sort_email_domain(user_data: list) -> dict:
    """
    This function extracts email addresses and returns a sorted dictionary
    where the domain name is the key and the count is the value.

    Args:
        user_data (list): A list of strings with each user's information.

    Returns:
        email_data (dict): A dictionary sorted by domain frequency in descending order.
    """
    # TODO: implement this function
    pass


################## EXTRA CREDIT ##################
def validate_michigan_number(user_data: list) -> list:
    """
    This function checks for southeast Michigan phone numbers and returns a list of valid numbers.

    Args:
        user_data (list): A list of strings with each user's information.

    Returns:
        michigan_numbers (list): A list of valid southeast Michigan phone numbers.
    """
    # TODO: implement this function
    pass


class TestAllFunc(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()

        # Paths for test files
        self.test_files = {
            "test1.txt": os.path.join(self.test_dir.name, "test1.txt"),
            "test2.txt": os.path.join(self.test_dir.name, "test2.txt"),
            "test3.txt": os.path.join(self.test_dir.name, "test3.txt"),
            "test4.txt": os.path.join(self.test_dir.name, "test4.txt")
        }

        # Sample data to write to files
        sample_data = [
            "username: janeaccount\nP455W0RD: janeaccount123\n@cc0uNT:janeaccount\nBirthday: 06/28/2003\nEmail: jane@gmail.com\nPhone: 313-555-1234\n",
            "username: johnbanking\nP455W0RD: password\n@cc0uNT:johnbanking\nBirthday: 04/05/2004\nEmail: john@bank.net\nPhone: 734-987-1234\n",
            "",
            "username: emthompson\nP455W0RD: Thompson!321\n@cc0uNT:emthompson\nBirthday: 05/11/2002\nEmail: em@google.com\nPhone: 313-123-4567\n"
        ]

        # Write data to test files
        with open(self.test_files["test1.txt"], 'w') as f:
            f.write(sample_data[0])
        with open(self.test_files["test2.txt"], 'w') as f:
            f.write(sample_data[0] + '\n\n' + sample_data[1])
        with open(self.test_files["test3.txt"], 'w') as f:
            f.write(sample_data[2])
        with open(self.test_files["test4.txt"], 'w') as f:
            f.write('\n\n'.join(sample_data))

    def test_get_user_info(self):
        # TODO: implement this test case
        pass

    def test_create_age_dict(self):
        # TODO: implement this test case
        pass

    def test_check_password_strength(self):
        # TODO: implement this test case
        pass

    def test_sort_email_domain(self):
        # TODO: implement this test case
        pass

    ############ EXTRA CREDIT ############
    def test_validate_michigan_number(self):
        # TODO: implement this test case
        pass


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
