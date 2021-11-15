#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    converted = [] 
    
    # Convert to binary
        # Divide the base-10 number by 2 and keep the remainder
        # Repeat until you reach 0
    # Save binary representation 
        
    while (n > 0):
        n = int(n / 2) 
        remainder = n % 2
        converted.append(remainder)
        
    # Count how many consecutive 1's there are
    consecutive = 1
    
    for i in range(len(converted)):
        if converted[i] == 1:
            if (converted[i+1] == 1):
                consecutive += 1
    
    # Print out how many consecutive 1's there are
    print(consecutive)
