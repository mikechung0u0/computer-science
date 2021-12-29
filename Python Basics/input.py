#write code to ask for the users name
#print the message good morning + that person's name
#output the message on the screen
name = input("Enter your name: ")

#output the user input on the screen
print("Good morning", name)


#get and store user input 
name = input("Enter your name: ")

#output the user input on the screen
print("Good morning", name)

#ask user to enter a number (integer)
#save it in a variable called "number"
user_input = int(input("Enter a number:")) 

#defining a new function called "get_square"
#it takes one value and returns value * value (square)
def get_square (number):
    return number * number

# call the get_square function, pass "number" as argument
# save the result in a variable called "square"
# print the "square" variable on screen 
square = get_square(user_input)
print(square)