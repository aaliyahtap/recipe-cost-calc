"""
Recipe Cost Calculator
INT CHECKER v1 -
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


number = int(int_checker("enter a number: ", "error"))
