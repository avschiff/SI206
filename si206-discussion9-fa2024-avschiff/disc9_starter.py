from bs4 import BeautifulSoup
import requests
import unittest

def get_emblem(soup):
    """
    Task 2: Get the source path (src) to the image for the University of Michigan's emblem.
    """
    return soup.find('img', class_='mw-file-element').get('src') 

def get_founded_year(soup):
    """
    Task 3: Get the details of the table that has the founding year of all schools/colleges at the University of Michigan and organize the information into key-value pairs in a 
    dictionary. 

    Use the structure: 
    {'school/college': founding year}

    Be sure to convert the founding year to an integer.
    """
    table = soup.find('table', class_='wikitable sortable')
    dataDict = {}
    if table:
        rows = table.find_all('tr')
        for row in rows[1:-1]:
            columns = row.find_all('td')
            school = columns[0].text.strip()
            founding_year = columns[1].text.strip()
            try:
                founding_year = int(founding_year)
                dataDict[school] = founding_year
            except ValueError:
                print(f"Invalid founding year for {school}: {founding_year}")
    return dataDict



def main():
    # Task 1: Create a BeautifulSoup object.
    
    # YOUR CODE HERE

    # Task 4: Sort the dictionary by founding year to see what the 3 newest programs are at the University of Michigan
    
    # YOUR CODE HERE
    pass



# DO NOT change anything below this
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_get_emblem(self):
        self.assertEqual(get_emblem(self.soup), '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Seal_of_the_University_of_Michigan.svg/150px-Seal_of_the_University_of_Michigan.svg.png')

    def test_get_school_founded_year(self):
        self.assertEqual(get_founded_year(self.soup)['College of Pharmacy'], 1876)

    def test_sorted_dictionary_first_three_items(self):
        sorted_founding_year = sorted(get_founded_year(self.soup).items(), key=lambda item: item[1], reverse= True)
        last_three_items = sorted_founding_year[:3]
        expected_result = [
            ('School of Kinesiology', 1984),
            ('Penny W. Stamps School of Art & Design', 1974),
            ('School of Information', 1969)
        ]
        self.assertEqual(last_three_items, expected_result)
    

if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)