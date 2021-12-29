#return length of a string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet) 
print(alphabet_length)

#advanced application 
for count in range(alphabet_length):
    print("this is printed same # times as the length alphabet ", count)

#convert char to ASCII code 
english_a = "a"
ASCII_a = ord(english_a)
print (ASCII_a)

#convert ASCII to a_z character
ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)

#return index (position) of a letter in a string
a_z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position_of_a = a_z.find("A")
print(position_of_a)

#change from UPPERCASE to lowercase 
a_z_lowercase = a_z.lower() 
print(a_z_lowercase)

#adding two strings together
string_one = "You are a "
string_two = "Rockstar"
combined = string_one + string_two
print(combined)

#functions + strings 
def combine_strings(string_one, string_two):
    return string_one + " " + string_two

result = combine_strings("Hello", "my neighbors")
print(result)

#if else and strings
string = "true"

if("true"):
    print("yes")
elif("false"):
    print("no")


#string operations - 

#convert character to it's ASCII code - ord ()
english_a = "a"
ASCII_a = ord(english_a)
print (ASCII_a)

#convert ASCII to a_z character - chr()
ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)

#add two strings together
string_one = "good morning"
string_two = "my neighbor"
combined = string_one + " " + string_two
print(combined)

#return the position of a specific letter
#012345678910111213141516171819202122232425 (26 total)
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_d = alphabet.index("d") 
print(position_of_letter_d + 1)


