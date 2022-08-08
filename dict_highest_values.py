'''Write a Python program to find the highest values in a dictionary'''

from heapq import nlargest

def largest(dictionary, n=2):  
    the_largest = nlargest(n, dictionary, key=dictionary.get)
    print(the_largest) 

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
largest(my_dict)
