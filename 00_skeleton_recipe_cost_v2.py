"""
Recipe Cost Calculator
Skeleton v2 - start to add the loops into the base
Aaliyah T

"""


# set up functions**********************************************

# function to check for integers. will loop until an integer is input
def number_checker():
    print("placeholder")


# function to check string is within an allowable list. Will loop until an allowable word is input
def string_checker(list_of_allowable):
    print("placeholder")


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# main routine


# set up lists and constants************************************
calc_total_cost = []

chosen_recipe_list = []
ingredients_list = []
max_list_length = 10
#  main***************************************************
while len(chosen_recipe_list) != max_list_length:
    print("placeholder")
    # ask users for input
    print("**")
    print("** Welcome to my recipe cost calculator")
    recipe_name = not_blank("What recipe are you going to need the cost for? ", "This cannot be blank")
    chosen_recipe_list.append(recipe_name)
    print(chosen_recipe_list)
