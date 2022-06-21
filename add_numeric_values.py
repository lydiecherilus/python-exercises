'''Given an dictionary with keys and values that consist of both strings and integers, 
design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the followin dictionary as input: '''
a = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
''' The algorithm should return 41, the sum of the values 23 and 18.'''

def sum_values(a):
    sum = 0
    for value in a.values():
        if isinstance(value, int):
            sum+= value
    return sum

print(sum_values(a))
