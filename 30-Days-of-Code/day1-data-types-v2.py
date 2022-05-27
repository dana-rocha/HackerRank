i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.
try:
    second_integer = int(input())
except ValueError:
    print("Please input the correct data type.")
    
try:
    second_double = float(input())
except ValueError:
    print("Please input the correct data type")
    
try:
    second_string = str(input())
except ValueError:
    print("Please input the correct data type")

# Print the sum of both integer variables on a new line.
print(i + second_integer)
# Print the sum of the double variables on a new line.
print(format(d + second_double, ".1f"))
# Concatenate and print the String variables on a new line
print(s + second_string)
# The 's' variable above should be printed first.