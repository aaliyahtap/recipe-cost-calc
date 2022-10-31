"""
Recipe Cost Calculator
NUMBER FUNCTION V1 - adding a number function to the int checker
to make sure that the program doesn't allow integers that are in the negatives (0 is allowed) or above 999999999999
Aaliyah T

"""


def number_checker(amount_question, error_message):
    # amount = int(input("please enter amount:"))

    x = True
    while x:

        try:
            int_num = int(input(amount_question))
            x = False

            if int_num > 999999999999:
                print(error_message)
                return
            elif int_num < 0:
                print(error_message)
                return

        except:
            print(error_message)

    return int_num


num_checker = (number_checker("enter a number: ", "Error"))
print(num_checker)
