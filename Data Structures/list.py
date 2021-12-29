#initalize a list (linkedlist)
student_names = ["Mike", "Amy", "Charlie", "Marco", "David", "Leon", "Rain", "Angelina", "Yujing", "Henry", "Barbie", "Johnathan"]

#add a name to our list
student_names.append("Mars")
student_names.insert(0, "Mr. Amini") #insert at index (0) first position

#delete a name
student_names.remove("Charlie")

#iterate over our list
for name in student_names:
    print(name)

#get the length of the list
length = len(student_names)
print(length)

#sort list using built in list method .sort
student_names.sort()
for name in student_names:
    print(name)

#Character (letter) list
letter_grades = ["A", "A-", "A", "B", "B", "C", "C-", "A-", "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")

#count number of people with grade A 
number_of_A_grades = letter_grades.count("A")
print("number of grades A:", number_of_A_grades)

#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]
#count number of zeros
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)
#sort list
numbers.sort()
#print each item in list (iteration)
for number in numbers:
    print(number)

#boolean list
has_completed_homework = [True, True, False, True, False, False, True]
number_of_completed_homeworks = has_completed_homework.count(True)
print("Number of people who did homework", number_of_completed_homeworks)

#combine two lists
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
combined_list = letters + numbers
print(combined_list)

#lists - create a list of integers to represent the daily temperature of a single week
#temperature in celsius 

temperature = [22, 24, 23, 30, 28, 27, 23]
print(temperature)
#Add - the temperature 33 to the list (adds to the end)
temperature.append(33)
print(temperature)
#Find - the index of value 33 in the list
index = temperature.index(33)
print(index)
#Delete - the value 22 from the list
temperature.remove(33)
print(temperature)
#Access value by index
sunday_temp = temperature[0] 
print(sunday_temp)
#Sort the list
temperature.sort()
print(temperature)
#get and print the highest temperature
highest_temp = temperature.pop()
print(highest_temp)
