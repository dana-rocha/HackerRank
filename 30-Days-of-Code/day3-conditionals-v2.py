# Re-starting 30 Days of Code Challenge: 5/26/22

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    if (N % 2 == 0):
        if N in range(2, 5+1):
            print("Not Weird")
        elif N > 20:
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")  