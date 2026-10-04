def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary):
    return gross_salary * 0.05


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


def main():
    employee_name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))

    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary)
    net_salary = calculate_net_salary(gross_salary, tax)

    print("\nEmployee Salary Calculator")
    print("--------------------------")
    print("Employee Name:", employee_name)
    print("Basic Salary:", basic_salary)
    print("Allowance:", allowance)
    print("Gross Salary:", gross_salary)
    print("Tax (5%):", tax)
    print("Net Salary:", net_salary)


main()