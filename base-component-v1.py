"""
Recipe Cost Calculator
BASE COMPONENT V1 - trying to implement most of the simple components into this base component.
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

        ingredients_list.append(int_num)
    return int_num


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

recipe_name = not_blank("Recipe name: ",
                        "Error")



ingredients_ques = not_blank("Please input the name of the ingredients you need: ",
                             "Error")
ingredients_list.append(ingredients_ques)
print(ingredients_list)

returned_num = int_checker("please enter an amount in grams: ", "sorry - this is not an integer ")
