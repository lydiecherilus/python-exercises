''' 
Find all the pairs of two integers in a list that sum up to a given S. 
For example, if the list is [3, 5, 2, -4, 8, 11] and the sum is 7, 
your program should return [[11, -4], [2, 5]]
'''

def find_pair(list, S):
    pair=[]
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == S:
                pair.append([list[i], list[j]])
    return pair
    
# list = [3, 5, 2, -4, 8, 11]
# S = 7
# print(find_pair(list, S))
