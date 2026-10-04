def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


def main():
    employee_name = input("Enter employee name: ")

    basic_salary = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    tax_rate = float(input("Enter tax rate (%): "))

    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary, tax_rate)
    net_salary = calculate_net_salary(gross_salary, tax)

    print("\nEmployee Salary Details")
    print("-------------------------")
    print("Employee Name:", employee_name)
    print("Basic Salary:", basic_salary)
    print("Allowance:", allowance)
    print("Gross Salary:", gross_salary)
    print("Tax:", tax)
    print("Net Salary:", net_salary)


main()