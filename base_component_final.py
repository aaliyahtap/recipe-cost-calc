"""
Recipe Cost Calculator
BASE COMPONENT FINAL - refining the base component for final, adding tags to label functions
Aaliyah T

"""


# not blank function to make sure input is not blank, prints error if not an int.
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# int checker ensures that input that needs to be an int will be an int, prints and error if it is not an int.
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


# float checker to check that a float is being used, error will print if input is not a float.
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
# will append the user's ingredients input into this list
ingredients_list = []
# will append the amount of these ingredients into this list
amount_ingredients_list = []
# will append the serving size that the user has input into this list
serving_size_list = []
# will append the  cost of the item/ingredient from the store per kg, into this list
item_cost_store = []
# this list holds the item cost
item_cost = []
# this list holds the item cost in the recipe
item_recipe_cost = []
count = 0
item_weight_store = 1000

# main
# introduction
print("₊˚ʚ ᗢ₊˚✧ ﾟ. RECIPE COST CALCULATOR .ﾟ ✧˚₊ᗢ ɞ˚₊")
print("""
    /)＿/)☆
⠀⠀／(๑^᎑^๑)っ ＼
／|￣∪￣￣￣￣￣￣ ￣￣￣￣￣￣ ￣￣￣￣￣￣￣￣￣￣￣ ￣￣￣|＼／
⠀     Welcome to my recipe cost calculator!
  |＿＿＿＿＿＿＿＿＿＿＿ ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿ ＿|／""")
print("")
print("""
                ˗ˏˋ ꒰ ♡ ꒱ ˎˊ˗""")


recipe_name = not_blank("""
  ∧,,,∧
(  ̳• · • ̳)
/    づ Please enter the recipe name: """,
                        "♡ Sorry - this can't be blank")
# lets the user know what recipe name they picked
print("♡ You have chosen the recipe name {}!".format(recipe_name))
# Get details

serving_size = int(int_checker("♡ Please input serving size: ",
                               "♡ That isn't a correct integer!"))
count += serving_size
serving_size_list.append(count)
print("♡ You have chosen a serving size of {}!".format(serving_size_list))

amount_ingredients_ques = int(int_checker("♡ How many ingredients will you need? "
                                          "(for example: flour, sugar, and milk would be 3): ",
                                          "♡ That isn't a correct integer!"))

# this is used to ensure the question will not go out of the range input by the user
# (user wants 2 ingredients so program will stay within 2 ingredient questions)
for item in range(amount_ingredients_ques):
    ingredients_ques = not_blank("♡ Please input the name of the ingredients you need: ",
                                 "♡ Sorry - this can't be blank")
    amount_grams = int(int_checker("♡ Please enter an amount for {} in grams or millilitres: ".format(ingredients_ques),
                                   "That isn't a correct integer"))
    cost_ingredients = float(
        float_checker("♡ What is the price of {} at your local store per kg? ".format(ingredients_ques),
                      "♡ That isn't a correct integer"))

    cost = (amount_grams / item_weight_store * cost_ingredients)
    print("♡ The cost for {} is: ${:.2f}".format(ingredients_ques, cost), ":)")

    item_cost_store.append(cost_ingredients)
    ingredients_list.append(ingredients_ques)
    amount_ingredients_list.append(amount_grams)
    item_recipe_cost.append(cost)

print("♡ ingredients: ", ingredients_list)
print("♡ amount ingredients: ", amount_ingredients_list)
print("♡ item cost per kg in store: ", item_cost_store)
print("♡ item in recipe cost: ".format(ingredients_ques), item_recipe_cost)
total_cost_recipe_ingredients = sum(item_recipe_cost)
print("♡ total cost recipe: ${:.2f}".format(total_cost_recipe_ingredients))
# this prints the total cost of the recipe times the serving size.
total_cost_per_serving = total_cost_recipe_ingredients / serving_size
print("♡ total cost per serving: ${:.2f}".format(total_cost_per_serving))

# TOTAL COST
print(""" 
/)  /) ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
( •-• ) ~  ♡ The total cost per serving is ${:.2f}! ♡""".format(total_cost_per_serving), """
/づ  づ ~ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(" ")
print(" ")
print(" ")
