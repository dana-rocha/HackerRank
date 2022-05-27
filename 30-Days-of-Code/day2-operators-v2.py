# Re-starting 30 Days of Code Challenge: 5/26/22

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    # meal_cost is a float
    # tip_percent and tax_percent are both integers
    # Need to return total cost --> rounded to nearest integer

    tip_cost = meal_cost * (tip_percent/100)
    tax_cost = (tax_percent/100) * meal_cost
    
    total_cost = meal_cost + tip_cost + tax_cost
    
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)


