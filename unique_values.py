''' Write a Python program to print all unique values in a dictionary.'''

def unique_values(dictionary):
    dict_unique_values = set(val for dicts in dictionary for val in dicts.values())

    print(dict_unique_values)

my_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S002"},{"VIII":"S007"}]
unique_values(my_dict)
