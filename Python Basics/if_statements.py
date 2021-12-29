#programs make decisions based on control logic (control flow)
student_grade = 93

if student_grade > 90:
    print("Your grade is A")
elif student_grade < 90 and student_grade > 80:
    print ("Your grade is a B")
elif student_grade < 80 and student_grade > 70:
    print("Your grade is a C")
else: 
    print("Your grade is a D or F")

#write a program using if-elif-else that....
#looks at a variable for temperature = 20C
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, and it's above 5C, print it's cold
#else print "bring an umbrella just in case"


is_CJHS_student = True #boolean
is_enrolled_history = False
#boolean operators - and, or, not 
#and - True and True = True Ex. True and False = False
#or - True or True = True Ex. True or False = True 
#not - not True = False Ex. not False = True 

#control flow using boolean operators(If-Elif-else)

#and
if(is_CJHS_student and is_enrolled_history):
    print("You are an MAK student in history")
elif(is_CJHS_student and not is_enrolled_history):
    print("You are an CJHS student not enrolled in history")


