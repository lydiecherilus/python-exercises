''' given an array of integers, return the number of 9's in the array'''

def count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count = count + 1
  return count
