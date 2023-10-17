# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    indx = candy_list.index(candy)
    print(f"[{indx}] {candy}")

# grab a user input - number like 0 or 1 or 5
# using that number, grab the associated candy, save to new variable
# add to the end (append) of the candy_cart list, that chosen candy
# loop it 5 times

for x in range(allowance):
    # get user value
    user_val = input("Which candy would you like to purchase? Please select a number 0-8: ")

    # cast to int
    user_val = int(user_val)

    # fail gracefully
    if (user_val < 0) or (user_val > 8):
        print("Hey! I said choose a number between 0-8 please... >:(")
    else:
        # use as index, get value from list
        chosen_candy = candy_list[user_val] # candy_list[0] -> "Snickers"
        print(f"You chose {chosen_candy}")

        # append to cart list
        candy_cart.append(chosen_candy)
        print(candy_cart)
