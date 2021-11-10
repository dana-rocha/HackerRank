# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

dictionary_size = int(input())

phonebook = {}


for i in range(0, dictionary_size):
    in_string = input().split()
    
    phonebook[in_string[0]] = in_string[1]


while True: 
    try:
        name = input()
        
        if (name in phonebook):
            print("{}={}".format(name, phonebook[name]))
        else:
            print("Not found")
        
    except EOFError:
        break
    
