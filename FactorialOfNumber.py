"""Defines a function named factorial that takes a number as an argument
   and calculates its factorial using a loop or recursion.
   Returns the calculated factorial.
   Calls the function with a sample number and prints the output.
"""
def factorial(num):
    if num == 1:
        return 1
    else:
         fact=num * factorial(num-1)
         return fact

num= int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")



