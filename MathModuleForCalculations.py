"""
  Asks the user for a number as input.
  Uses the math module to calculate the:
  Square root of a number, natural logarithm of the number,
  sine of the number in radians.
"""
import math

number = int(input("Enter a number: "))
square_root= math.sqrt(number)
print(f"Square root: {square_root}")
logOfNumber= math.log(number)
print(f"Logarithm: {logOfNumber}")
sineOfNumber= math.sin(number)
print(f"Sine: {sineOfNumber}")
