"""
Recipe Cost Calculator
BASE COMPONENT V4 - starting to add calculations
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


# lists

ingredients_list = []
amount_ingredients_list = []
serving_size_list = []
item_cost_store = []
item_cost = []
item_recipe_cost = []
count = 0
item_weight_store = 1000

# main
# introduction
print("✭✭✭✭✭✭✭✭RECIPE COST CALCULATOR✭✭✭✭✭✭✭✭")
print("")
print("Welcome to my recipe cost calculator :)")

print("")
print("")
recipe_name = not_blank("Please enter the recipe name: ",
                        "Sorry - this can't be blank")
# Get details
serving_size = int(int_checker("Please input serving size: ",
                               "That isn't a correct integer"))
count += serving_size
print("You have chosen a serving size of {}".format(count))
serving_size_list.append(count)
print(serving_size_list)

amount_ingredients_ques = int(int_checker("how many ingredients will you need? "
                                          "(for example: flour, sugar, and milk would be 3): ",
                                          "That isn't a correct integer"))

for item in range(amount_ingredients_ques):
    ingredients_ques = not_blank("Please input the name of the ingredients you need: ",
                                 "Sorry - this can't be blank")
    amount_grams = int(int_checker("please enter an amount for {} in grams or millilitres: ".format(ingredients_ques),
                                   "That isn't a correct integer"))
    cost_ingredients = float(
        float_checker("What is the price of {} at your local store per kg? ".format(ingredients_ques),
                      "That isn't a correct integer"))

    cost = (amount_grams / item_weight_store * cost_ingredients)
    print("The cost for {} is: ${:.2f}".format(ingredients_ques, cost), ":)")

    item_cost_store.append(cost_ingredients)
    ingredients_list.append(ingredients_ques)
    amount_ingredients_list.append(amount_grams)
    item_recipe_cost.append(cost)
    print("ingredients: ", ingredients_list)
    print("amount ingredients: ", amount_ingredients_list)
    print("item cost per kg in store: ", item_cost_store)
    print("item in recipe cost: ".format(ingredients_ques), item_recipe_cost)
    total_cost_recipe_ingredients = sum(item_recipe_cost)
    print("total cost recipe: ${:.2f}".format(total_cost_recipe_ingredients))

    total_cost_per_serving = total_cost_recipe_ingredients / serving_size
    print("total cost per serving: ${:.2f}".format(total_cost_per_serving))

