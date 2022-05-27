# Re-starting 30 Days of Code Challenge: 5/26/22

# Task
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and 
# odd-indexed characters as 2 space-separated strings on a single line (see the Sample below 
# for more detail).

# Note: 0 is considered to be an even index.

# Example
# s = adbecf
# Print abc def

# Input Format:
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a string, S.

# Constraints: 1 <= T <= 10, 2 <= length of S <= 10000

# Output Format:
# For each String (Sj) (where 0 <= j <= T-1), print (Sj's) even-indexed characters, 
# followed by a space, followed by 's odd-indexed characters.




# Enter your code here. Read input from STDIN. Print output to STDOUT



# Input: number of test cases, strings
# Output: characters of the input string on one line with even-indexed characters on 
# first half and odd-indexed characters on second half.

# Example Input: s = adbecf
# Example Output: r = abc def

# test_cases = int(input())



# Overall Time Complexity: O(N*T) where T = number of test cases and N = length of string S
# Time Complexity of each string: O(N) where N = length of string S


for i in range(int(input())):
    input_string = input()

    even_letters = ""
    odd_letters = ""


    for ind in range(len(input_string)):
        
        if (ind % 2 == 0):
            even_letters += input_string[ind]
        else:
            odd_letters += input_string[ind]

    print(even_letters + " " + odd_letters)