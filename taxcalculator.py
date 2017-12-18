# Import necessary packages

#This method gets all the required salary information from the user
def get_input_params():
    usr_salary = float_inp("Please enter your salary: $")

    #Ask whether or not the quoted salary value includes super
    inp_super = input("Does this value include super? (Y/N): ")
    valid = False
    while not valid:
        if inp_super in ("Y", "y"):
            has_super = True
            valid = True
        elif inp_super in ("N", "n"):
            has_super = False
            valid = True
            super_amt = 0.0
        else:
            inp_super = input("Invalid response. Please enter Y or N:")

    #Ask for the percentage of super paid
    super_amt = float_inp("What percentage super does your employer "
                          "pay? (default is 9.5): ")
    valid = False
    while not valid:
        if 0 < super_amt < 100:
            valid = True
        else:
            super_amt = float_inp("Invalid percentage. Please enter "
                                  "a value between 0 and 100: ")

    #Ask whether or not the user has a hecs debt
    inp_hecs = input("Do you have a hecs debt? (Y/N): ")
    valid = False
    while not valid:
        if inp_hecs in ("Y", "y"):
            has_hecs = True
            valid = True
        elif inp_hecs in ("N", "n"):
            has_hecs = False
            valid = True
        else:
            inp_hecs = input("Invalid response. Please enter Y or N:")

    input_params = [usr_salary, has_super, super_amt/100, has_hecs]

    return input_params
#END get_input_params()

#This method calculates the annual tax payable on a given salary
#Assumption: the salary figure does not include super
def tax_payable(inp_salary):
    income_tax_levels = (18200, 37000, 87000, 180000)
    income_tax_static = (0, 3572, 19822, 54232)
    income_tax_rates = (0.0, 0.19, 0.325, 0.37, 0.45)
    tax_amt = 0.0
    index = 0
    for level in income_tax_levels:
        if inp_salary > level:
            tax_amt = tax_amt + income_tax_static[index]
            index += 1
        else:
            tax_amt = (tax_amt + (inp_salary - income_tax_levels[index-1])
                               * income_tax_rates[index])
            return tax_amt
    tax_amt = (tax_amt + (inp_salary - income_tax_levels[index-1])
                       * income_tax_rates[index])
    return tax_amt
#END - tax_payable()

#This method calculates the annual HECS payable on a given salary
#Assumption: the salary figure does not include super
def hecs_payable(inp_salary):
    hecs_levels = (54868, 61119, 67368, 70909, 76222, 82550, 86894, 95626, 101899)
    hecs_rates = (0.0, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08)
    hecs_amt = 0.0
    index = 0
    for level in hecs_levels:
        if inp_salary > level:
            index += 1
        else:
            hecs_amt = inp_salary * hecs_rates[index]
            return hecs_amt
    hecs_amt = inp_salary * hecs_rates[index]
    return hecs_amt
#END - hecs_payable()

#This method is used to catch the user entering text before it is cast
#as a float and generates an error.
def float_inp(msgStr):
    usr_resp = input(msgStr)
    valid = False
    while not valid:
        #Strip leading dollar sign
        if usr_resp[0] == "$":
            usr_resp = usr_resp[1:]

        test_result = is_float(usr_resp)
        if test_result[1] == True:
            return test_result[0]
        else:
            usr_resp = input("The value must be a number. Please try again:")
#END float_inp

#Test a string to ensure that it can be converted to a float
def is_float(test_str):
    try:
        out_float = float(test_str)
    except ValueError:
        return [0.0, False]
    else:
        return [out_float, True]
#END is_float

if __name__ == "__main__":
    #Put the main program here

    break_line = "----------------------------------------------------------\n"

    print("This program will calculate the Australian tax payable on "
          "an individual salary.")
    tap, flg_super, super_pct, flg_hecs = get_input_params()

    #Separate super from salary
    if flg_super:
        salary = tap / (1 + super_pct)
        annual_super = tap - salary
    else:
        salary = tap
        annual_super = salary * super_pct

    #Calculate tax payable
    income_tax = tax_payable(salary)

    #Calculate HECS payable
    if flg_hecs:
        total_hecs = hecs_payable(salary)
    else:
        total_hecs = 0

    #Calculate the after tax salary
    after_tax_salary = salary - income_tax - total_hecs

    #Format and display output
    print("\nPersonal Taxation Summary")
    print(break_line)
    print("Annual Figures\n")
    print("Total Annual Package: $" + str(int(salary + annual_super)))
    print("Pre-tax salary: $" + str(int(salary)))
    print("Superannuation: $" + str(int(annual_super)))
    print("\nAfter tax salary: $" + str(int(after_tax_salary)))
    if flg_hecs:
        print("\nTotal tax: $" + str(int(income_tax + total_hecs)))
        print("Income tax: $" + str(int(income_tax)))
        print("HECS payments: $" + str(int(total_hecs)))
    else:
        print("\nIncome tax: $" + str(int(income_tax)))
    print(break_line)

    print("Monthly Figures\n")
    print("Pre-tax salary: $" + str(int(salary/12)))
    print("Superannuation: $" + str(int(annual_super/12)))
    print("\nAfter tax salary: $" + str(int(after_tax_salary/12)))
    if flg_hecs:
        print("\nTotal tax: $" + str(int((income_tax + total_hecs)/12)))
        print("Income tax: $" + str(int(income_tax/12)))
        print("HECS payments: $" + str(int(total_hecs/12)))
    else:
        print("\nIncome tax: $" + str(int(income_tax/12)))
    print(break_line)

    input("Press enter to close the window")
#END - __main__