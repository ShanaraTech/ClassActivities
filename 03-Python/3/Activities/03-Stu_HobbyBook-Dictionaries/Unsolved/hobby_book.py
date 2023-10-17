# @TODO: Your code here
Name = {
    "Shanara":["22","Basketball Mom","Mon,Tues,Thurs","5:00am"],
    "Jason": ["31","video games, concerts, cooking","tuesday,wednesday,thursday,07:30"],   
     "Aaron": ["31", "Big Daddy", "Everyday Hustler", "A Mac", "Monday, Wednesday", "5:30am"],
         }
print(Name)
print(Name)
# Print the third actor
print(f'{Name["Aaron"][2]}')
# Print the second actor
print(f'{Name["Jason"][1]}')

# Simple function with one parameter
def welcome_message(message):
    print(message)
welcome_message("Hello, World!")

# Functions can have more than one parameter
def make_quesadilla(protein, topping):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)
          
make_quesadilla("carne", "queso")
make_quesadilla("steak", "pico de gallo")



# Functions can have more than one parameter
def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla) 
    
    
make_quesadilla("chicken")


def square_num(number):
    return number * number
squared_value = square_num(7)

print(squared_value)

def avg_function(total, n):
    return (total/n)

avg = avg_function(9,3)

print(avg)

    
    