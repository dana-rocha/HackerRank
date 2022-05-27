# Re-starting 30 Days of Code Challenge: 5/26/22


# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input: number of test cases, strings
# Output: characters of the input string on one line with even-indexed characters on first half and odd-indexed characters on second half

# Example Input: s = adbecf
# Example Output: r = abc def

test_cases = int(input())

input_list = []

for i in range(test_cases):
    input_string = input()
    input_list.append(input_string)


for ele in input_list:
    even_letters = ""
    odd_letters = ""    
    
    for i in range(len(ele)):
        # if-statements --> index is odd or even
        if i % 2 == 0:
            even_letters += ele[i]
        else:
            odd_letters += ele[i]
        
    print(even_letters + " " + odd_letters)