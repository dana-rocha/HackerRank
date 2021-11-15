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
        
    while (n > 0):
        n = int(n / 2) 
        remainder = n % 2
        converted.append(remainder)
        
        print("remainders: {}".format(remainder))
    
    # Save binary representation 
    
    # Count how many consecutive 1's there are
    
    # Print out how many consecutive 1's there are
