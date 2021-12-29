#data types
#1 write a variable that stores a boolean value 
is_prepared_for_class = True 
pays_attention_in_class = False
sleeps_in_class = False

#2 write a variable that stores an integer
class_average = 88

#3 write a variable that stores a floating point number
weight = 70.0

#loops
#1. write a for loop that says "happy birthday Barbie + Howard" 14x

for i in range(14):
    print("happy birthday barbie and howard") 


#while loop
#1. write a while loop to print ("goodmorning") 4x

count = 0

while(count < 4):
    print("good morning")
    count = count + 1


#functions

#write a function that takes in two arguments 
#and returns the sum of those two args

def addition (number, another_number):
    return number + another_number

print(addition(10,10))

#random number generation
import random 
random_number = random.randint(1,99)
print(random_number)