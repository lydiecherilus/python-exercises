''' Write a program that prints the solution to the FizzBuzz game.
Replace all integers that are evenly divisible by 3 with "fizz"
Replace all integers evenly divisible by 5 with "buzz"
Replace all integers evenly divisible by both 3 and 5 with "fizzbuzz" '''

def fizzbuzz(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
            numbers[i] = "fizzbuzz"
        elif numbers[i] % 3 == 0:
            numbers[i] = "fizz"
        elif numbers[i] % 5 == 0:
            numbers[i] = "buzz"
        else:
            numbers[i] = numbers[i]
    print(numbers)

fizzbuzz([45, 22, 14, 65, 97, 72])
