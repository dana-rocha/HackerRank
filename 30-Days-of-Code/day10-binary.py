#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    
    consecutive = 0
    max_num = 0
    # Convert to binary
        # Divide the base-10 number by 2 and keep the remainder
        # Repeat until you reach 0
    while (n > 0):
        
        if n % 2 == 1:
            consecutive += 1
            max_num += 1
            
            if max_num > consecutive:
                max_num = consecutive
            
        else:
            consecutive = 0
            
        n = n // 2
    
    print(max_num)
        
