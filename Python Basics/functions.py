def polynomial(number, anotherNumber):
   return 2 * number + 8 * anotherNumber

#test this number = 3 and anotherNumber = 5
#expect result to be 6 + 40 = 46

result = polynomial(6, 5)
print(result)


#or w/ function
def buy_things(nike_instock, hermes_instock):
    if(nike_instock and hermes_instock):
        print("buy both nike and hermes")
    elif(nike_instock or hermes_instock):
        print("buy either nike or hermes, not both")
    else:
        print("neither is in stock, srry lovely person")

#call our function
buy_things(nike_instock = False, hermes_instock = False)