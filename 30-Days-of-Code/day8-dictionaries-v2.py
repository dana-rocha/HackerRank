# Enter your code here. Read input from STDIN. Print output to STDOUT

# Task
# Given n names and phone numbers --> dictionary that maps names to phone numbers
# If name is not in phone book --> print "Not found"
# If name is in phone book --> print each entry on a new line in the format: name=phoneNumber


# Input format:
# First line: an integer, n, representing the number of entries in phone book
# Each line of n --> one line of 2 values, separated by a space where the first value is the friend's name and the second value is the phone number
# Unknown number of lines of queries --> need to read each line until there's no name to look up

# Names consits of lowercase English alphabetic letters and first names only

phone_book = {}

for i in range(int(input())):
    entry = input().split(" ")
    
    phone_book[entry[0]] = entry[1]


while True:
    try: 
        query = str(input().strip())
    
        if phone_book.get(query):
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break