'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : xyc abz'''

def swap_first_char(str1, str2):
    temp = str2[0:2] + str1[-1]
    str2 = str1[0:2] + str2[-1]
    return temp + ' ' + str2
