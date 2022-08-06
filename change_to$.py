'''Write a Python program to get a string from a given string where all occurrences of its first char 
have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'''

new_str = ''
def change_second_occurence(str):
    for i in str[1:]:
        if i == str[0]:
            new_str = str.replace(i, '$')
            new_str = str[0] + new_str[1:]
    return new_str



new_str = ''
def change_second_occurence2(str):
    char = str[0]
    str = str.replace(char, '$')
    new_str = char + str[1:]
    return new_str
