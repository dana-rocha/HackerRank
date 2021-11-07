# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

test_strings = []

for i in range(0, test_cases):
    s = input()
    test_strings.append(s)

# print(test_strings)
even_strings = ""
odd_strings = ""

for i in range(0, len(test_strings) + 1):
    print(i)
    
    # for j in range(0, len(test_strings[i])):
    #     print(j)
    # if (j == 0 or j % 2 == 0):
    #     even_strings += test_strings[i][j]
    # else:
    #     odd_strings += test_strings[i][j]
    # print(test_strings[i][j])
    # even_strings += test_strings[i][j]

    # odd_strings += test_strings[i][j]

# print("{} {}".format(even_strings, odd_strings))
# print(even_strings)
