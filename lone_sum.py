'''Given 3 integers, a b c, return their sum. 
However, if two of them have the same value, 
they do not count towards the sum.'''

def lone_sum(a, b, c):
  sum = 0
  if a not in [b,c]:
    sum += a  
  else:
    sum = sum
  if b not in [a,c]:
    sum += b  
  else:
     sum = sum
  if c not in [a,b]:
    sum += c 
  else:
    sum = sum
  return sum

print(lone_sum(1, 2, 3)) #→ 6
print(lone_sum(3, 7, 3)) #→ 7
