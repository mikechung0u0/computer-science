#how can we test this code? 

def add (number, another_number):
    return number + another_number

#step #1 - come up with some edge cases
#a) invalid input - enter a 'char' vs. an 'int' 
#b) 

#step #2 - wrap in a try-catch block to handle any errors
try: 
    result = add('a', 9)
except Exception as error:
    print('input must be a number only')
    print(error)
else:
    print(result)

