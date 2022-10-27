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


def float_checker(amount_question, error_message):
    x = True
    while x:

        try:
            float_num = float(input(amount_question))
            x = False

        except:
            print(error_message)

    return float_num


def cost_to_make():
    print("cost to make")


# function to calculate total cost of meal
def cost_of_meal():
    print("cost of meal")


# function to calculate cost per serving
def cost_per_serving():
    print("cost per serving")


# lists

ingredients_list = []
amount_ingredients_list = []
serving_size_list = []
item_cost_store = []
item_cost = []
count = 0
item_weight_store = 1000
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

amount_ingredients_ques = int(int_checker("how many ingredients will you need? "
                                          "(for example: flour, sugar, and milk would be 3): ",
                                          "Error"))

for item in range(amount_ingredients_ques):
    ingredients_ques = not_blank("Please input the name of the ingredients you need: ",
                                 "Error")
    amount_grams = int(int_checker("please enter an amount for {} in grams: ".format(ingredients_ques),
                                   "sorry - this is not an integer "))
    cost_ingredients = float(
        float_checker("What is the price of {} at your local store per kg? ".format(ingredients_ques),
                      "sorry - that is not an integer"))
    item_cost_store.append(cost_ingredients)
    ingredients_list.append(ingredients_ques)
    amount_ingredients_list.append(amount_grams)
    print("ingredients: ", ingredients_list)
    print("amount ingredients: ", amount_ingredients_list)
    print("item cost per kg in store: ", item_cost_store)
    # idx = ingredients_list.index(ingredients_ques)
    # price = item_cost_store # [idx]
    # weight = item_weight_store # [idx]
    # amount = amount_ingredients_list

    # cost = amount / weight * price

    # print(cost)
