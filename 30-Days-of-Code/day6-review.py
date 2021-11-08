# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

for i in range(0, test_cases):
    string_in = input()

    for k in range(0, len(string_in)):
        if (k % 2 == 0):
            print(string_in[k], end = '')
            
    print(" ", end = '')
    
    for j in range(0, len(string_in)):
        if (j % 2 != 0):
            print(string_in[j], end = '')
    
    print(" ")
        
