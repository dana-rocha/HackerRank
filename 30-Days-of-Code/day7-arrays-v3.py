#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    # Time Complexity: O(N) where N is the integers of the array A
    for i in arr[::-1]:
        print(i, end = " ")