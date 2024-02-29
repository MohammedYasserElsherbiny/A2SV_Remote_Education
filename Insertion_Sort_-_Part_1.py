#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    for i in range(1,n):
        val=arr[i]
        j=i-1
        
        while j>=0 and val<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print(' '.join(map(str,arr)))
            
        arr[j+1]=val
        #print(arr)
    print(' '.join(map(str,arr)))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
