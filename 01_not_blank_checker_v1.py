"""
Recipe Cost Calculator
NOT BLANK CHECKER V1 - simple function to help with ensuring the users are not using blank input.
Aaliyah T

"""


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# main routine
recipe_name = not_blank("recipe: ",
                        "error")
print(recipe_name)
