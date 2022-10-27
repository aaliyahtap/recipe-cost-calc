"""
Recipe Cost Calculator
INT CHECKER v2 - implementing more specific
Aaliyah T

"""


def int_checker(amount_question, error_message):
    # amount = int(input("please enter amount:"))

    x = True
    while x:

        try:
            int_num = int(input(amount_question))
            x = False
        except:
            print(error_message)

    return int_num


number = int(int_checker("Please enter an integer: ", "This is not an integer - please enter an integer"))
print("You have chosen the number: {}".format(number))
