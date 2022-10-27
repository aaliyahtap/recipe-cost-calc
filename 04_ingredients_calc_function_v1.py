"""
Recipe Cost Calculator
INGREDIENTS CALC V1 - asking the user for the numbers
Aaliyah T

"""

amount_ingredients_ques = int(input("""how many ingredients will you need?
(for example: flour, sugar, and milk would be 3): """))

for item in range(amount_ingredients_ques):
    ingredients_ques = input("Please input the name of the ingredients you need: ")
    amount_grams = int(input("please enter an amount for {} in grams or millilitres: ".format(ingredients_ques)))
    cost_ingredients = float(input("What is the price of {} at your local store per kg? ".format(ingredients_ques)))
    print(ingredients_ques)
    print(amount_grams)
    print(cost_ingredients)
