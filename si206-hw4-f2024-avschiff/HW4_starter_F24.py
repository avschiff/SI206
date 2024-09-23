# SI 206 HW4
# Your name: Avery Schiff
# Your student id: 35947681
# Your email: avschiff@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

# --- ARGUMENTS & EXPECTED RETURN VALUES PROVIDED --- #
# --- SEE INSTRUCTIONS FOR FULL DETAILS ON METHOD IMPLEMENTATION --- #

import unittest


class User:
    def __init__(self, name, employer_id=None, account=15):
        '''
        ARGUMENTS: 
            self: the current object

            name: a string representing a user's name

            employer_id: integer representing ID of the service the user works for (default = None)

            account: integer showing how many credits the user currently has
        
        RETURNS: None
        '''
        self.name = name
        self.employer_id = employer_id
        self.account = account


    def __str__(self):
        '''
        ARGUMENTS: 
            self: the current object

        RETURNS: a string
        '''
        return f'My name is {self.name}, and I have {self.account} credits in my account'


    def add_credits(self, credits):
        '''
        ARGUMENTS: 
            self: the current object

            credits: an integer showing how many credits are needed to request the service
            
        RETURNS: a float
        '''
        self.account += credits


    def request_service(self, vendor, request):
        '''
        ARGUMENTS: 
            self: the current object

            vendor: a Vendor object

            request: a nested dictionary -> KEYS - Service objects; VALUES - another dictionary 
            with keys of duration and priority

        RETURNS: a Boolean value (True or False)
        '''
        pass


class Service:
    def __init__(self, name, price):
        ''' 
        ARGUMENTS: 
            self: the current object

            name: a string representing the name of the service

            price: a float representing the regular price of a service

        RETURNS: None
        '''
        self.name = name
        self.price = price

    def __str__(self):
        ''' 
        ARGUMENTS: 
            self: the current object

        RETURNS: a string
        '''
        return f"{self.name} costs ${self.price} per hour"


class Vendor:
    def __init__(self, name, vendor_id, income=0):
        ''' 
        ARGUMENTS: 
            self: the current object

            name: a string representing the name of the service

            vendor_id: an integer representing the ID of the vendor;(used for users who are also 
            employees to track who they work for)

            income: a float representing the income the vendor has collected

            capacity: a dictionary which holds the Service objects as the keys 
            and the available number of hours for that service from this vendor as the value

        RETURNS: None
        '''
        self.name = name
        self.vendor_id = vendor_id
        self.income = income
        self.capacity = {}

    
    def __str__(self):
        '''
        ARGUMENTS: 
            self: the current object

        RETURNS: a string
        '''
        return f"Hello we are {self.name}. This is the current capacity {self.capacity}"

    
    def accept_payment(self, amount):
        '''
        ARGUMENTS: 
            self: the current object

            amount: total cost of a request (as a float) added to the vendor's income

        RETURNS: a float
        '''
        self.income += amount

    
    def calculate_service_cost(self, service_obj, duration, priority, user):
        '''
        ARGUMENTS: 
            self: the current object

            service_obj: Service object

            duration: number of hours (requested from service)

            priority: Boolean variable specifying if a priority request was made

            user: User object (the user who made a request)

        RETURNS: a float

        ***If a priority request is made, a 50% surcharge is added.***

        EXTRA CREDIT: If the user works for the vendor, then they receive a 20% discount
        on the service. They also still pay the 50% surcharge for priority requests.
        '''
        pass


    def add_duration(self, service_obj, duration):
        ''' 
        ARGUMENTS: 
            self: the current object

            service_obj: Service object

            duration: number of hours (requested from service)
        
        RETURNS: None
        '''
        pass


    def process_request(self, request):
        '''
        ARGUMENTS: 
            self: the current object

            request: a nested dictionary -> KEYS: Service objects; VALUES: another dictionary 
            with keys of duration and priority

        RETURNS: a Boolean value (True or False)
        '''
        pass


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.cleaning = Service('Cleaning', 25.00)
        self.gardening = Service('Gardening', 40.00)
        self.tutoring = Service('Tutoring', 50.00)
        self.babysitting = Service('Babysitting', 30.00)

        self.handy_helpers = Vendor(name="Handy Helpers", vendor_id=1)
        self.super_services = Vendor(name="Super Services", vendor_id=2)

        self.bob = User(name='Bob', employer_id=None)
        self.alice = User(name='Alice', employer_id=17, account=125)
        self.charlie = User(name='Charlie', employer_id=1, account=200)

    # Check the constructors
    def test_user_constructor(self):
        self.assertEqual(self.bob.name, 'Bob')
        self.assertEqual(self.bob.account, 15)

    def test_service_constructor(self):
        self.assertEqual(self.tutoring.name, 'Tutoring')
        self.assertAlmostEqual(self.tutoring.price, 50.00, 2)
        self.assertEqual(self.babysitting.name, 'Babysitting')
        self.assertAlmostEqual(self.babysitting.price, 30.00, 2)

    def test_vendor_constructor(self):
        self.assertEqual(self.handy_helpers.name, "Handy Helpers")
        self.assertEqual(self.handy_helpers.income, 0)
        self.assertEqual(self.super_services.name, "Super Services")
        self.assertEqual(self.super_services.capacity, {})

    # Check the add_credits method for user
    def test_user_add_credits(self):
        self.alice.add_credits(100)
        self.assertAlmostEqual(self.alice.account, 225, 1)

    # Check the calculate_service_cost for vendor
    def test_vendor_calculate_service_cost(self):
        self.assertAlmostEqual(self.handy_helpers.calculate_service_cost(
            self.tutoring, 2, False, self.alice), 100.00, 2)

        # Check if discount is applied
        self.assertAlmostEqual(self.super_services.calculate_service_cost(
            self.cleaning, 3, False, self.alice), 75, 2)

        # Check if priority requests are billed correctly
        self.assertAlmostEqual(self.super_services.calculate_service_cost(
            self.babysitting, 4, True, self.alice), 180.00, 2)

    # Check the accept_payment method for vendor
    def test_vendor_accept_payment(self):
        self.super_services.accept_payment(500)
        self.assertAlmostEqual(self.super_services.income, 500.00, 2)

    # Check the add_duration method for vendor
    def test_vendor_add_duration(self):
        self.super_services.add_duration(self.cleaning, 40)
        self.super_services.add_duration(self.gardening, 20)
        self.assertEqual(self.super_services.capacity, {
                         self.cleaning: 40, self.gardening: 20})

        self.handy_helpers.add_duration(self.tutoring, 30)
        self.handy_helpers.add_duration(self.babysitting, 50)
        self.assertEqual(self.handy_helpers.capacity, {
                         self.tutoring: 30, self.babysitting: 50})

    # Check the request_service method for user
    def test_user_request_service(self):
        pam = User(name='Pam', employer_id=19)
        services_r_us = Vendor(name="Services R Us", vendor_id=14)

        services_r_us.add_duration(self.babysitting, 10)
        services_r_us.add_duration(self.cleaning, 15)

        # Scenario 1: user doesn't have enough credits in their account

        # Scenario 2: vendor doesn't have enough capacity left

        # Scenario 3: vendor doesn't offer that service type

    # Fix the test cases for test_user_request_service_2
    def test_user_request_service_2(self):
        ali = User(name='Ali', employer_id=47, account=300)
        dunder_services = Vendor(name="Dunder Services", vendor_id=19)
        dunder_services.add_duration(self.tutoring, 20)
        dunder_services.add_duration(self.gardening, 30)

        self.assertTrue(ali.request_service(dunder_services, {
            self.tutoring: {
                "duration": 2,
                "priority": False
            },
            self.gardening: {
                "duration": 3,
                "priority": True
            }}
        ))
        self.assertAlmostEqual(ali.account, 15, 2)  
        self.assertAlmostEqual(dunder_services.income, 0, 2)


def main():
    pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    main()