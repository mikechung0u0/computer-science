#user input error - this throws an exception if a string is given by user
#age = int(input("Enter your age:"))


#try-catch block 
try: 
    age = int(input("Enter your age:"))
except ValueError as error:
    print("please enter a number only")
    print(error)
else:
    print("no exceptions were thrown, excute this")



#try-catch block 
try: 
    age = int(input("Enter your age:"))
    calculation = 10/age
except (ValueError, ZeroDivisionError) as error:
    print("Please enter a valid")
    print(error)

print("if this is executed the pgrom didn't stop running")