'''Given a list of integers length 3, figure out which is larger, the first or last element in the list,
and set all the other elements to be that value. 
Return the changed list.'''

def max_first_last(nums):
    i = max(nums[0], nums[2])
    return [i, i, i]

print(max_first_last([1, 2, 3])) #→ [3, 3, 3]
print(max_first_last([11, 5, 9])) #→ [11, 11, 11]
print(max_first_last([2, 11, 3])) #→ [3, 3, 3]
