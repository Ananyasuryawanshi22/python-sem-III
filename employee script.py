import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        name = employee["Name"]
        monthly_salary = int(employee["MonthlySalary"])

        annual_salary = monthly_salary * 12

        print("Name:", name)
        print("Annual Salary:", annual_salary)

        if monthly_salary > 50000:
            print("Monthly salary is above ₹50,000")

        print()