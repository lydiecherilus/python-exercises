'''Return the number of times "code" appears anywhere in a given string, 
except any letter will be accepted for 'd', so "cope" and "cooe" count.'''

def count_code(str):
  if len(str) < 4:
    return 0
  elif (str[0] == 'c' and str[1] == 'o' and str[2].isalpha() is True and str[3] == 'e'):
    return 1 + count_code(str[1:])
  else:
    return 0 + count_code(str[1:])

print(count_code('aaacodebbb')) #→ 1
print(count_code('codexxcode')) #→ 2
print(count_code('cozexxcope')) #→ 2
