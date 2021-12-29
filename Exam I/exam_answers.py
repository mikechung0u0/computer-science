wallet = 70
if wallet > 90 and wallet <= 100:
    print("you can buy a snack between 90 and 100")
elif wallet > 80 and wallet <= 90: 
    print("you can buy a snack between 80 and 90")
elif wallet > 70 and wallet <= 80: 
    print("you can buy a snack between 70 and 80")
elif wallet <= 70:
    print("only buy a snack less than 70 dollars!")
else:
    print("completed)")



number = 0
while(number < 7):
    print("I know what I'm talking about, you can trust me", number)
    number = number + 1 #incrementing (0-> 1-> 2) the counter manually 


for i in range(10):
    print("I am getting smarter and smarter in everyway everyday and I love it!", i)

#ask user for input 
name = input("Enter your name: ")

#print input + string on the screen 
print("Good morning ", name)


#addition
#there are 5000 cows, 2000 chicken, 188 sheep in a farm
#how many total animals?
cows = 5000
chicken = 2000
sheep = 188 
total = cows + chicken + sheep
print("animals before slaughter", total)
#subtraction
#if 78 sheep are killed and 230 cows are also killed 
#how many are total animals are left?

killed_cows = 230
killed_sheep = 78
total_after_slaughter = total - (killed_cows + killed_sheep)
print("animals after slaughter", total_after_slaughter)