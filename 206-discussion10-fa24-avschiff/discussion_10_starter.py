from bs4 import BeautifulSoup
import requests
import regex as re 
import unittest

# TASK 2: PROCESS LANDMARK DATA
def get_landmark_data(soup) -> dict[dict]:
    '''
    creates a nested dictionary of landmarks and their data

    the outer keys are the landmark names
    the inner keys are information about the landmark 
        - data designated
        - location 
        - county
        - description 

    returns a nested dictionary
    '''
    landmarks_data = {}
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 5:
            name = cols[0].text.strip()
            date_designated = cols[1].text.strip()
            location = cols[2].text.strip()
            county = cols[3].text.strip()
            description = cols[4].text.strip()

            landmarks_data[name] = {
                'date_designated': date_designated,
                'location': location,
                'county': county,
                'description': description
            }

    return landmarks_data

# TASK 3: GET PROPER NOUNS
def get_proper_noun_phrases(landmarks_dict:dict[dict], target_landmark:str) -> list[str]:
    '''
    extracts all proper noun phrases from the description field of the target landmark 

    proper noun phrase = multiple consecutive capitalized worlds (e.g. 'Great Lakes' or 'Michigan State')

    returns a list with all proper nounts
    '''
    pass


def main():
    #TASK 1: GET DATA FROM WIKIPEDIA
    url = 'https://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Michigan'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    landmark_data = get_landmark_data(soup)
    
    example_phrases = get_proper_noun_phrases(landmark_data, 'Bay View')
    print("Proper noun phrases for 'Bay View':", example_phrases)


# DO NOT MODIFY TEST CASES
class TestAllFunctions(unittest.TestCase):
    def setUp(self):
        soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Michigan").text, 'html.parser')
        self.landmarks_data = get_landmark_data(soup)

    def test_get_landmark_data(self):
        self.assertEqual(len(self.landmarks_data), 42)
        self.assertTrue('USS Silversides (Submarine)' in self.landmarks_data)

        self.assertEqual(self.landmarks_data['Bay View']['county'], 'Emmet')
        self.assertEqual(self.landmarks_data['Cranbrook']['county'], 'Oakland')

    def test_get_proper_noun_phrases(self):
        bay_view = get_proper_noun_phrases(self.landmarks_data, 'Bay View')
        self.assertEqual(bay_view, [])

        gm = get_proper_noun_phrases(self.landmarks_data, 'General Motors Building')
        self.assertEqual(gm, ['General Motors'])

        guardian_building = get_proper_noun_phrases(self.landmarks_data, 'Guardian Building')
        self.assertEqual(guardian_building, ['Union Trust', 'Union Trust Company'])


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)