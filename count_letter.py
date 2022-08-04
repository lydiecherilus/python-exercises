'''Write a Python program that counts occurrences of a character in a string 
and add them to a dictionary'''

string = 'hello' 

str_dict = {}
for i in string:
    str_dict[i] = str_dict.get(i, 0) + 1

print(str_dict)
