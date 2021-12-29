#1 Data Types and variables

#a) Write a boolean to represent whether or not you will pass the exam
passed_exam = True

#b) Write an integer variable to represent your score on the exam
my_score = 93

#c) Write a floating point variable to represent the class average on the exam
class_average = 87.5

#d) Write a string variable to represent something you'd say to your friend in the morning
message = "good morning my neighbor"


#Programming Concepts

# Definite iteration using for loops 
    #a) write a for loop that prints "I am a polite and kind person" 10x
for i in range(10):
    print("I am a polite and kind person", i)

    #b) write a while loop that prints "I know computer science" 7x
counter = 0
while(counter < 10):
    print("I know computer science", counter)
    couter = couter + 1


#control flow - write a program for the following situation..
#a) if student has a grade of 90-100 print "you're a rockstar student"
#b) elif student has a grade of 80-90 print "you're amazing, keep leveling up"
#c) elif student has a grade of 70-80 print "not bad, keep working"
#d) else if student has a grade of less than 70 print "keep working champ"
# > < >= and or not if-elif-else 
student_grade = 99

if student_grade > 90 and student_grade <= 100:
    print("you're a rockstar student")
elif student_grade > 80 and student_grade <=90:
    print("you're amazing, keep leveling up")
elif student_grade > 70 and student_grade <= 80:
    print("not bad, growth mindset, you got it")
else:
    print("you can always do more and become more, growth mindset")

# arithemtic operations  
# write code to complete the following arithmetic operations 
# print the results on the screen 

1 + 5 
99999 - 9494
38484 * 999
24 / 2
90 % 10

a = 1 
b = 5
c = a + b
print(c)

d = 99999
e = 9494
f = d - e
print(f)

g = 38484
h = 999
i = g * h 
print(i)


j = 24
k = 2
l = j / k
print(l)

m = 90
n = 10
o = m % n 
print(o)

#how much money does the class have in total
students = 21
money_per_student = 15.5
total = students * money_per_student
print(total)

#string operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#write a line of code to find the length of this string
#print the length on the screen
length = len(alphabet)
print(length)

#write code to find the index (position) of the letter "t"
#print the index on the screen

position = alphabet.find('t')
print(position)

#write code to ask for the users name
#print the message hello to that person's name
name = input("Enter your name: ")

#output the user input on the screen
print("Good morning", name)

#arithmetic operations - addition, subtraction, multiplication, division, modulus operator

#write code to solve this - 
#there are 22 students in class
#each student has 92.5 NTD in their wallet
#how much total money do all the students have combined?

#multiplication
students = 22
amount_per_student = 92.5
total = students * amount_per_student
print(total)

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

#write code to ask for the users name
#print the message good morning + that person's name
#output the message on the screen
name = input("Enter your name: ")

#output the user input on the screen
print("Good morning", name)


