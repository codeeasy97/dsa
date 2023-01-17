#Find the Minimum element in a Sorted 
# and Rotated Array

#method 1: Linear Search 
# TC- O(N) SC- O(1)
def findMin(arr, n):
    min_ele = arr[0] #4| 1
    for i in range(1,n):
        if arr[i] < min_ele:
            min_ele = arr[i]
    return min_ele


#                        m s|e    
#arr =   [4, 5, 6, 7, 8, 9, 1, 2, 3] #sorted rotated arr
#  INDEX: 0  1  2  3  4  5  6  7  8  
#method2: Binary Search Iterative 
# TC- O(logN) SC- O(1)
def findMinBinaryIterative(arr,start, end):
    while start < end:
        mid = (start + end)//2 #4 | 6
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid
    return arr[start]

#                        s  m      e  
#arr =   [4, 5, 6, 7, 8, 9, 1, 2, 3] #sorted rotated arr
#  INDEX: 0  1  2  3  4  5  6  7  8
#method 2: Binary Search
# TC- O(logN) SC- O(N)
def findMinBinaryRecursion(arr, start, end):
    if start > end:
        return arr[start]

    mid = (start+end)//2 #4

    if arr[mid] < arr[mid-1]:
        return arr[mid]

    if arr[mid] > arr[end]:
        return findMinBinaryRecursion(arr, mid + 1, end)
    return findMinBinaryRecursion(arr, start, mid - 1)

# arr = [1,2,3,4,5,6]
# [6,1,2,3,4,5]
# [5,6,1,2,3,4]

arr =   [4, 5, 6, 7, 8, 9, 1, 2, 3] #sorted rotated arr
# INDEX: 0  1  2  3  4  5  6  7  8  
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] sorted arr
# arr = [15, 18, 2, 3, 6, 12]
      # 0   1  2  3  4   5
n = len(arr)


res = findMin(arr, len(arr))
print("Linear Search: ",res)

res = findMinBinaryIterative(arr, 0, n-1)
print("Iterative Binary: ",res)

res = findMinBinaryRecursion(arr, 0, n-1)
print("Recursion Binary: ",res)