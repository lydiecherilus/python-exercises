'''Return the sum of the numbers in a list, except ignore sections of numbers 
starting with a 6 and extending to the next 7.
'''

def sum67(nums):
  sum = 0
  i = 0
  while( i < len(nums)):
    if nums[i] == 6:
        while(nums[i] != 7):
          i += 1
    else:
      sum += nums[i]
    i += 1
  return sum

print(sum67([1, 1, 6, 100, 8, 15, 7, 2])) #→ 4
