# Your name: Avery Schiff
# Your student id: 35947681
# Your email: avschiff@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): 
# If you worked with generative AI also add a statement for how you used it.
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code 


import csv
import unittest

def csv_reader(filename):
    """
    Load employee data from a CSV file.
    """
    employees = {}
    inFile = open(filename)
    csv_reader = csv.reader(inFile)

    header = next(csv_reader)

    for row in csv_reader:
        emp_id = row[0]
        employee_data = {
            'gender': row[1],
            'race': row[2],
            'hire_year': int(row[3])
        }
        
        if len(row) > 4: #added to handle extra credit csv
            employee_data['role'] = row[4]
            employee_data['salary'] = float(row[5])

        employees[emp_id] = employee_data
    
    inFile.close()
    return employees    

def split_by_hire_year(employees, split_year):
    """
    Split employee data into two dictionaries based on hire year.
    """
    before_split = {}
    after_split = {}

    for emp_id, data in employees.items():
        if data['hire_year'] < split_year:
            before_split[emp_id] = data
        else:
            after_split[emp_id] = data
    
    return before_split, after_split    

def count_race_or_gender(employees):
    """
    Count the number of employees belonging to each race and gender category.
    """
    race_counts = {}
    gender_counts = {}

    for data in employees.values():
        race = data['race']
        race_counts[race] = race_counts.get(race, 0) + 1

        gender = data['gender']
        gender_counts[gender] = gender_counts.get(gender, 0) + 1

    return {'race': race_counts, 'gender': gender_counts}

def count_race_and_gender(employees):
    """
    Count the number of employees within each combination of race and gender.
    """
    combined_counts = {}

    for data in employees.values():
        combination = f"{data['race']}&{data['gender']}"
        combined_counts[combination] = combined_counts.get(combination, 0) + 1

    return combined_counts

def csv_writer(data, filename):
    """
    Write data to a CSV file.
    """
    outFile = open(filename, mode='w', newline='')
    writer = csv.writer(outFile)
    
    writer.writerow(['Combination', 'Count'])
    
    for key, value in data.items():
        writer.writerow([key, value])

    outFile.close()

def reduce_company_costs(employees, target_reduction):
    """
    EXTRA CREDIT OPTION ONE
    Create your own algorithm to reduce company payroll costs. 
    """
    total_payroll = sum(data.get('salary', 0) for data in employees.values()) #help from AI
    reduced_employees = {}
    sorted_employees = sorted(employees.items(), key=lambda x: x[1]['salary']) #help from AI
    current_reduction = 0

    for emp_id, data in sorted_employees:
        salary = data.get('salary', 0)
        if salary == 0:
            continue
        if current_reduction < target_reduction:
            potential_new_salary = salary - (target_reduction - current_reduction)
            if potential_new_salary < 5000:
                potential_new_salary = 5000
            actual_reduction = salary - potential_new_salary
            current_reduction += actual_reduction
            reduced_employees[emp_id] = {**data, 'salary': potential_new_salary} #learned **data from AI
        else:
            reduced_employees[emp_id] = data

    return reduced_employees

class TestEmployeeDataAnalysis(unittest.TestCase):

    def setUp(self):
        """
        - Set up any variables you will need for your test cases
        - Feel free to use 'smaller_dataset.csv' for your test cases so that you can verify 
        the correect output. 
        """

        self.filename = '/Users/averyschiff/Documents/SI206/project1-fall24-avschiff/smaller_dataset.csv' #Using only "smaller_dataset.csv" does not work
        self.employees = csv_reader(self.filename)

        self.extra_credit_filename = '/Users/averyschiff/Documents/SI206/project1-fall24-avschiff/GM_employee_data_extra_credit.csv'
        self.employees_extra_credit = csv_reader(self.extra_credit_filename)

    def test_load_csv(self):
        # Your test code for load_csv goes here
        employees = csv_reader(self.filename)
        self.assertIsInstance(employees, dict)
        self.assertGreater(len(employees), 0)
        self.assertIn('gender', employees[list(employees.keys())[0]])

    def test_split_by_hire_year(self):
        # Your test code for split_by_hire_year goes here
        before, after = split_by_hire_year(self.employees, 1964) #help from AI
        self.assertIsInstance(before, dict)
        self.assertIsInstance(after, dict)
        self.assertGreater(len(before), 0)
        self.assertGreater(len(after), 0)
        for emp in before.values():
            self.assertLess(emp['hire_year'], 1964)
        for emp in after.values():
            self.assertGreaterEqual(emp['hire_year'], 1964)

    def test_count_race_or_gender(self):
        # Your test code for count_race_or_gender goes here
        counts = count_race_or_gender(self.employees)
        self.assertIsInstance(counts, dict)
        self.assertIn('race', counts)
        self.assertIn('gender', counts)
        self.assertEqual(counts['race']['White'], 13)
        self.assertEqual(counts['gender']['Male'], 9)

    def test_count_race_and_gender(self):
        # Your test code for count_race_and_gender goes here
        combined_counts = count_race_and_gender(self.employees)
        self.assertIsInstance(combined_counts, dict) #help from AI
        self.assertGreater(len(combined_counts), 0)
        self.assertIn('Black&Female', combined_counts)
        self.assertEqual(combined_counts['Black&Female'], 6)

    def test_reduce_company_costs(self):
        # Your test code for reduce_company_costs goes here
        target_reduction = 5000000
        reduced_employees = reduce_company_costs(self.employees_extra_credit, target_reduction)

        for emp_id, emp_data in reduced_employees.items():
            self.assertGreaterEqual(emp_data['salary'], 5000)

        new_payroll = sum(emp['salary'] for emp in reduced_employees.values())
        initial_payroll = sum(emp['salary'] for emp in self.employees_extra_credit.values())

        self.assertLessEqual(initial_payroll - new_payroll, target_reduction)


def main():
    # Load employee data from the CSV file
    employee_data = csv_reader('/Users/averyschiff/Documents/SI206/project1-fall24-avschiff/GM_employee_data.csv') #just using "GM_employee_data.csv" does not work for me

    # Task 1: Split employees by hire year
    employees_before_1964, employees_after_1964 = split_by_hire_year(employee_data, 1964)

    # Task 2: Count employees by race or gender before and after layoffs
    race_gender_counts_total = count_race_or_gender(employee_data)
    race_gender_counts_after_layoffs = count_race_or_gender(employees_before_1964)

    # Task 3: Count employees by race and gender combinations before and after layoffs
    gendered_race_counts_total = count_race_and_gender(employee_data)
    gendered_race_counts_after_layoffs = count_race_and_gender(employees_before_1964)

    # Print and interpret the results
    print("Analysis Results:")
    print("--------------------------------------------------------")

    # Task 1: Splitting employees
    print("Task 1: Split Employees by Hire Year")
    print(f"Number of employees hired total: {len(employee_data)}")
    print(f"Number of employees after layoffs: {len(employees_before_1964)}")
    print("--------------------------------------------------------")

    # Task 2: Comparing race or gender of all employees before and after layoffs
    print("Task 2: Comparing Race and Gender Before and After Layoffs")
    print("Category: Before Layoffs ---> After Layoffs")
    print("Race:")
    for category, count_before in race_gender_counts_total['race'].items():
        count_after = race_gender_counts_after_layoffs['race'].get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("Gender:")
    for category, count_before in race_gender_counts_total['gender'].items():
        count_after = race_gender_counts_after_layoffs['gender'].get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("--------------------------------------------------------")

    # Task 3: Comparing race and gender combinations before and after layoffs
    print("Task 3: Comparing Gendered Race Combinations Before and After Layoffs")
    print("Category: Before Layoffs ---> After Layoffs")
    print("Gendered races:")
    for category, count_before in gendered_race_counts_total.items():
        count_after = gendered_race_counts_after_layoffs.get(category, 0)
        print(f"\t{category}: {count_before} ---> {count_after}")

    print("--------------------------------------------------------")

    csv_writer(gendered_race_counts_total, "GM_employee_data_before_layoffs.csv")
    csv_writer(gendered_race_counts_after_layoffs, "GM_employee_data_after_layoffs.csv")



if __name__ == "__main__":    
    main()
    unittest.main(verbosity=2)


