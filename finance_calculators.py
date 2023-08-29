import math

# Started Project at 17:15 22/12/2022 until 20:00 continued at 23:30 until 01:00

print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
invest_bond = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# The following block of code ensures that the correct 'investment' and 'bond' spellings are entered.
# (Error Handling by Checking)
while True:
    if invest_bond != "investment" and invest_bond != "bond":
        invest_bond = input("\nPlease enter the appropriate banking options as either 'investment' or 'bond' and "
                            "continue: ").lower()
    else:
        break
print()

# A simple if/else statement is used to decide between 'investment ' and 'bond' option.
# All other calculation blocks are nested within this if/else statement.
if invest_bond == "investment":

    # The following block is an input block in a loop for error handling purposes using try and except statement.
    # Errors to be handled are: non-numerical inputs, and numbers less than zero (negative).
    while True:
        # Referencing
        # Object-Oriented Programming in Python 1 documentation. Accessed on 12 December 2022, from
        # https: // www.cs.uct.ac.za / mit_notes / python / Errors_and_Exceptions.html

        # From the site, I learnt about the 3 different types of errors (Syntax, runtime and Logical)
        # I also learnt about intercepting code errors and handling them to avoid crashing the code.
        # Errors can be checked by a scripted code or by using error handling techniques such as the try/except block.
        # The try and except error handling technique is easy to use and results in a readable code.
        # There are various types of errors that can be raised by the compiler and, we can also raise errors.

        # From my knowledge of the try and except statements, I applied the technique for 3 different inputs
        # simultaneously to shorten the code. I also raised errors for unwanted or inappropriate input values
        try:
            pv = float(input("Please enter the amount of money you are depositing: "))
            r = float(input("Please enter the preferred interest rate: "))
            t = float(input("Please enter the time duration of investment in years: "))

            # Negative present value (pv) means you owe that money
            # Negative interest rate (r) means the creditor is loosing money and not gaining from the investment
            # Negative time period (t) means time is shrinking or counting backwards. An impossible scenario!
            if pv < 0 or r < 0 or t < 0:
                raise ValueError("All numbers must be greater or equal to '0' ")
        except ValueError as error:
            print("\nINPUT ERROR!")
            print("All input values must be numbers without text or special characters!\n%s" % error)
            print("Please try again!\n")
        else:
            break
    print()

    interest = input("Please enter either 'simple' or compound' for interest type: ").lower()

    # The loop below handles errors due to mis-spellings of 'simple' and 'compound'
    while True:
        if interest != "simple" and interest != "compound":
            interest = input("Please enter the appropriate interest options as either 'simple' or 'compound' and "
                             "continue: ").lower()
        else:
            break

    # return on investment is calculated by the block below
    i = r / 100
    if interest == 'simple':
        a = round(pv * (1 + i * t), 2)
        print(f"\nWith a SIMPLE interest rate of {r}%, an INVESTMENT of R{pv} over {t} years, will return R{a}.")
    else:
        a = round(pv * math.pow((1 + i), t), 2)
        print(f"\nAn INVESTMENT of R{pv} COMPOUNDED at {r}% over {t} years, will return R{a}.")
else:

    # The following block is an input block in a loop and is for error handling purposes using try and except statement
    while True:
        try:
            pv = float(input("Please enter the present value of the house: "))
            r = float(input("Please enter the preferred interest rate: "))
            n = float(input("Please enter the time duration of repayments in months: "))

            if pv < 0 or r < 0 or n < 0:
                raise ValueError("All numbers must be greater or equal to '0' ")
        except ValueError as error:
            print("\nINPUT ERROR!")
            print("All input values must be numbers without text or special characters!\n%s" % error)
            print("Please try again!\n")
        else:
            break
    print()

    #  A bond monthly repayment is calculated below.
    i = (r / 100) / 12
    repay = round((i * pv) / (1 - math.pow((1 + i), -n)), 2)
    print(f"A BOND of R{pv} can be paid over {n} months, at a rate of {r}% using monthly installments of R{repay}.")
