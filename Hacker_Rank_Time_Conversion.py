#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    a = s[0] + s[1]
    if s[8] == 'P' and int(a) < int(12):
        a = (int(a) + 12)%24
        string = str(a)
        return string +s[2:8]
    if s[8] == 'P' and int(a)==int(12):
        return s[0:8]
    if s[8] == 'A' and int(a) < int(12):
        return s[0:8]
    if s[8] == 'A' and int(a) == int(12):
        return '00'+s[2:8]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
