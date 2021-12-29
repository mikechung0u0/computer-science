#data validation - length check 
password = input("enter a password:")

password_length = len(password)

if(password_length < 7 or password_length > 15):
    print("your password must be between 7 - 15 characters")


    #data validation - admin password 
admin_password = input("enter your new password: ")
admin_password_length = len(admin_password)

if(admin_password_length >= 6 and admin_password_length <= 12):
    print("password is updated")
else:
    print("password must be 6 - 12 characters")


name = input("enter your name: ")
#check if user enters an empty string, out of range string 

name_length = len(name)

if(name_length == 0):
    print("You cannot enter an empty name")
elif(name_length < 3):
    print("Name must be more than three letters")
elif(name_length > 25):
    print("name must be less than 25 characters")

#write a program that takes a new pet name and validates its length
# in other words, it prints an error message to the user if...
# the name is less than 2 chars and greater than 20 chars.
# 2 < name =< 20

#1. ask user for pet name, store it in a variable
pet_name = input('Enter your pet name: ')

#2. get pet name length, store length in a new variable
pet_name_length = len(pet_name) 

#3. validate length + display messages to user
if(pet_name_length == 0):
    print("You must enter something")
elif(pet_name_length < 2):
    print("Your pet must have a name with more than 2 letters")
elif(pet_name_length >= 20):
    print("Enter a name that is less than or equal to 20 letters")


#validation task - write code that takes user input and validates its length
#ask the user for a restaurant name
#validate that the name is greater than 5 letters and less than 25 letters

#1 - get name of restaurant
resturant_name = input("Enter a restaurant name: ")
#2 - get length
restaurant_name_length = len(resturant_name)
#3 - validation
if(restaurant_name_length == 0):
    print("You must enter something")
elif(restaurant_name_length < 5):
    print("You must enter a name with more than five letters")
elif(restaurant_name_length > 25):
    print("You must enter a name with less than 25 letters")


