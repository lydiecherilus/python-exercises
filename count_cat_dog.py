'''Return True if the string "cat" and "dog" appear the same
number of times in the given string.'''

def count_cat_dog(str):
  count_cat = 0
  count_dog = 0
  
  for i in range(len(str) -2):
    if str[i: i+3] == 'cat':
      count_cat += 1
    if str[i: i+3] == 'dog':
      count_dog += 1
  if count_cat == count_dog:
    return True
  else:
    return False
    
print(count_cat_dog('catdog')) #→ True
print(count_cat_dog('catcat')) # → False
print(count_cat_dog('1cat1cadodog')) # → True
