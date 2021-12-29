#Dictionaries or Hashmaps have fast lookup due to how they're stored in memory

#create a dicionary (key-value pairs) aka "HashMap, Map, HashTable"
assignment_scores = { "Mars": 90, "Amy": 93, "Rain": 98, "Charlie": 98 }
amy_assignment_score = assignment_scores.get("Amy")
print("Amy assignment score", amy_assignment_score)

#create a dictionary using built in dict function (same thing, different way to write it)
exam_scores = dict(Mars=90, Amy=93, Rain=98, Charlie=98)
mars_score = exam_scores.get("Mars")
print("Mars exam score", mars_score)

#iterate over the keys in the dictionary
for key in exam_scores:
    print(key)


#key - student name | value - boolean (True/False) represents whether or not the student has a pet
has_pets = {"Mars": False, "Henry": False, "Barbie": True, "Adrian": True, "Angelina": False}
    
#data structure operations - add, delete, search, sort
student_has_pet = has_pets.get("Barbie")
print("The student has a pet: ", student_has_pet)

#traverse the dictionary 
for student in has_pets:
    print(student, 'has a pet: ', has_pets.get(student))

#remove method - pop()
student_removed = has_pets.pop("Adrian")
print(student_removed)
print(has_pets)


#create a dictionary (key-value pair)
#key = student name
#value = list of scores (numbers)

student_scores = {
    "Adrian": [90, 91, 88], 
    "Charlie": [88, 99, 100],
    "Mandy": [90, 95, 99],
    "Yujing": [100, 99, 95],
    "Angelina": [99, 98, 99],
    "Mr. Amini": [50, 99, 99],
    "Howard": [99, 100, 97]
}

student_score = student_scores.get("Howard")
for score in student_score:
    print(score)


#dictionary to represent sibling names of students

student_siblings = {
    "Howard": ["Barbie", "Anthony", "Annie"],
    "Barbie": ["Howard", "Anthony", "Annie"],
    "Adrian": ["girl_Adrian", "another_girl_Adrian", "boy_Adrian"],
    "Mike": ["Angel"],
    "Yujing": ["Jimmy"]
}

student_brothers_sisters = student_siblings.get("Howard")
student_brothers_sisters.sort()
for sibling in student_brothers_sisters:
    print(sibling)


has_been_nice = {
            "Mr. Amini": False, 
            "Mike": True,   
            "Adrian": False, 
            "Henry": False,
            "Yujing": True,
            "Angelina": True,
            "Leon": True,
            "Charlie": True,
            "Mars": True
            }

gets_a_gift = has_been_nice.get("Mr. Amini")
print("This person has a gift: ", gets_a_gift)

#create a dictionary to represent Secret Santa
#Ex {"Mr. Amini": "Peter", "Ms. Jen": "Ms. Ana"}
#Ex {"Mr. Amini": ["Peter", "Jen"]}

secret_santa = {
    "Mr. Amini": "Teacher Peter", 
    "Ms. Jen": "Ms. Ana"
    }
recipient = secret_santa.get("Mr. Amini")
print(recipient)