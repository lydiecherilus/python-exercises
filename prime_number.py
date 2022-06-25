''' the programs takes a number and return True if the number is a prime number
and False otherwise'''

def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
          
