# Re-starting 30 Days of Code Challenge: 5/28/22

#!/bin/python3

import math
import os
import random
import re
import sys

# Task
# Given an array, A , of N integers, print A's elements 
# in reverse order as a single line of space-separated numbers.

# Example:
# A = [1, 2, 3, 4]
# Print: 4 3 2 1 where each integer is separated by one space

# Constraints:
# 1 <= N <= 1000
# 1 <= A[i] <= 10000 where A[i] is the ith integer in the array



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    
    result = ""
    for i in range(len(arr) -1 , -1 , -1):
        result += str(arr[i]) + " "

    print(result.rstrip())