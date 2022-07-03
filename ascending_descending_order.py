# 1. Write a Python script to sort a dictionary in ascending and descending order.
import operator

a = {
  "cat": "bob",
  "dog": "apple",
  "apple": "mango",
  "orange": "fish",
}

def sort_values(a):
    # sorting ascending 
    sorted_asc_v = dict(sorted(a.items(), key=operator.itemgetter(1))) # by value
    print(sorted_asc_v)
    sorted_asc_k = dict(sorted(a.items(), key=operator.itemgetter(0))) # by key
    print(sorted_asc_k)
    
    # sorting descending
    sorted_des_v = dict(sorted(a.items(), key=operator.itemgetter(1), reverse=True)) # by value
    print(sorted_des_v)
    sorted_des_k = dict(sorted(a.items(), key=operator.itemgetter(0), reverse=True)) # by key
    print(sorted_des_k)

sort_values(a)
