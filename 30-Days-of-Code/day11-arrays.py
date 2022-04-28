#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # print(arr)
    
    # Need to calculate every 3 indices row-wise and column-wise, step-wise

    # print(arr[3][3]) # prints 4
    # print(arr[3][2]) # prints 2
    s = []
    
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            count = 0
            count += (arr[j][k] + arr[j + 1][k] + arr[j + 2][k])
            
            s.append(count)
    
    print(s)

        
