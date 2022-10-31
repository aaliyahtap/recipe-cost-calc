"""
Recipe Cost Calculator
BASE COMPONENT V2 - trying to implement most of the simple components into this base component (not calculations)
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

# function to calculate total cost to make the recipe (inactive - will not be using in later components)
def cost_to_make():
    print("cost to make")


# function to calculate total cost of meal (inactive - will not be using in later components)
def cost_of_meal():
    print("cost of meal")


# function to calculate cost per serving (inactive - will not be using in later components)
def cost_per_serving():
    print("cost per serving")


# lists

ingredients_list = []
amount_ingredients_list = []
serving_size_list = []
count = 0
serving_size = ""
# main
recipe_name = not_blank("Recipe name: ",
                        "Error")
# Get details
serving_size = int(int_checker("Please input serving size: ",
                               "Error"))
count += serving_size
print("You have chosen a serving size of {}".format(count))
serving_size_list.append(count)
print(serving_size_list)

amount_ingredients_ques = int(int_checker("how many ingredients will you need? (for example: flour, sugar, and milk would be 3): ",
                                          "error"))

for item in range(amount_ingredients_ques):
    ingredients_ques = not_blank("Please input the name of the ingredients you need: ",
                                 "error")
    amount_grams = int(int_checker("please enter an amount for {} in grams: ".format(ingredients_ques),
                                   "sorry - this is not an integer "))
    ingredients_list.append(ingredients_ques)
    amount_ingredients_list.append(amount_grams)
    print("ingredients: ", ingredients_list)
    print("amount ingredients: ", amount_ingredients_list)
