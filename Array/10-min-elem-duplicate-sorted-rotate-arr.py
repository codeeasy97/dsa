#Find the Minimum element in a Duplicate 
# Sorted and Rotated Array

# [3, 3, 3, 3, 3, 3, 4, 1, 2, 3]

#method1: Linear Search
def findMin(arr, n):
    min_ele = arr[0]
    for i in range(1, n):
        if arr[i] < min_ele:
            min_ele = arr[i]
    return min_ele

#method2: Binary Search Iterative
"""
commented ele cond will uncomment for 
non-duplicate arr
ans line 24-27 commented
"""

def findMinBinaryIterative(arr, start, end):
    while(start < end):
        mid = (start + end)//2
        if arr[mid] > arr[end]:
            start = mid + 1
        # else:
        #     end = mid
        elif arr[mid] < arr[end]:
            end = mid
        else:
            end = end - 1
    return arr[start]

#method3: Binary Search Recursive
"""
49 & 51 uncommend & 42,43,48 & 50 commented when 
you do not use if cond on line 42
This cond checks if the middle elem is the pivot(small)
"""

def findMinBinaryRecursive(arr, start, end):
    if start > end:
        return arr[start]

    mid = (start + end)//2

    if arr[mid] < arr[mid-1]:
        return arr[mid]

    if arr[mid] > arr[end]:
        return findMinBinaryRecursive(arr, mid + 1, end)
    elif arr[mid] < arr[end]:
        return findMinBinaryRecursive(arr, start, mid - 1)
        # return findMinBinaryRecursive(arr, start, mid)
    return findMinBinaryRecursive(arr, mid + 1, end -1)
    # return findMinBinaryRecursive(arr, mid, end -1)
    


    #  s           m              e
arr = [3, 3, 3, 3, 3, 3, 4, 1, 2, 3]
#INDEX 0  1  2  3  4  5  6  7  8  9

#      s       m         e
# arr = [15, 18, 2, 3, 6, 12]
#INDEX 0   1   2  3  4   5 
n = len(arr)

res = findMin(arr, len(arr))
print("Linear Search: ",res)

res = findMinBinaryIterative(arr, 0, n-1)
print("Binary Search Iterative: ",res)

res = findMinBinaryRecursive(arr, 0, n-1)
print("Binary Search Recursive: ",res)