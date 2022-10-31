"""
Recipe Cost Calculator
INGREDIENTS CALC V2 - adding the calculations
Aaliyah T

"""
item_weight_store = 1000
serving_size = int(input("please input serving size: "))
amount_ingredients_ques = int(input("""how many ingredients will you need?
(for example: flour, sugar, and milk would be 3): """))

for item in range(amount_ingredients_ques):
    ingredients_ques = input("Please input the name of the ingredients you need: ")
    amount_grams = int(input("please enter an amount for {} in grams or millilitres: ".format(ingredients_ques)))
    cost_ingredients = float(input("What is the price of {} at your local store per kg? ".format(ingredients_ques)))
    print(ingredients_ques)
    print(amount_grams)
    print(cost_ingredients)
    total_cost = amount_grams / item_weight_store * cost_ingredients
    print("total cost: ",total_cost)
    total_cost_per_serving = total_cost / serving_size
    print("total cost per serving: ", total_cost_per_serving)
