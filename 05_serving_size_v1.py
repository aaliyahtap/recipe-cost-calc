"""
Recipe Cost Calculator
SERVING SIZE WHILE LOOP v1 - helps the user input the serving size for the recipe easily
Aaliyah T

"""
serving_size = ""
count = 0
serving_size_list = []


while serving_size != "xxx":
    # Get details
    serving_size = int(input("Please input serving size: "))
    count += serving_size
    print("You have chosen a serving size of {}".format(count))
    serving_size_list.append(count)
    print(serving_size_list)

else:
    print("This must be input.")











