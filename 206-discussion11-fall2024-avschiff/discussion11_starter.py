import json
import unittest
import os
import re

def read_json(filename):
    '''
    Opens file filename, loads content as json object

    Parameters: 
        filename: name of file to be opened

    Returns: 
        json dictionary OR an empty dict if the file could not be opened 
    '''
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): #help from AI
        return {}


def longest_book(books):
    """
    Returns the title of longest book (in pages)

    Parameters: 
        books (dict): dict representations of a decoded JSON document

    Returns:
        string: the title of the longest book
    """
    # Get list of ISBNs from txt file. HINT: You will need this to access the relevant dictionary keys 
    with open('books.txt', 'r') as f: 
        isbns = f.readlines()
    
    # YOUR CODE HERE
    longest = max(isbns, key=lambda isbn: books[isbn]['pages'])
    return books[longest]['title']

def author_by_letter(letter, books):
    """
    Returns a dictionary where the keys are authors whose last name begins with the letter passed into the function
    and the values are the titles of their books

    Parameters: 
    books (dict): dict representations of a decoded JSON document
    letter (str): a letter from A-Z

    Returns:
        dictionary: authors whose last name begins with the letter and the titles of their books

    """
    # YOUR CODE HERE
    result = {}
    for isbn, book in books.items():
        last_name = book['author'].split()[-1]
        if last_name.startswith(letter.upper()):
            result[book['author']] = book['title']
    return result

def get_new_editions(books):
    """
    Returns a list of books published since 2020 

    Parameters: 
        books (dict): dict representations of a decoded JSON document

    Returns:
        list: a list of titles of books published since 2020
    """
    # YOUR CODE HERE
    pass


#DO NOT CHANGE TEST CASES
class TestDiscussion11(unittest.TestCase):
    def setUp(self):
        self.books = read_json('books.json')

    def test_read_json(self):
        self.assertEqual(len(self.books), 25)


    def test_longest_book(self):
        self.assertEqual(longest_book(self.books), 'Gravity\'s Rainbow (Penguin Classics Deluxe Edition)')


    def test_author_by_letter(self):
        self.assertEqual(len(author_by_letter('C', self.books)), 4)
        self.assertEqual(author_by_letter('A', self.books), {'Mona Awad': 'Bunny'})
        self.assertEqual(author_by_letter('Z', self.books), {})


    def test_get_new_editions(self):
        self.assertEqual(get_new_editions(self.books), ['The Guest', 'Bunny', 'The Nickel Boys'])


def main():
    data = read_json('books.json')
    long_book = longest_book(data)
    author_C = author_by_letter('C', data)
    new_editions = get_new_editions(data)

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)