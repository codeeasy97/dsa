# Find a peak element which is not smaller than its neighbours
# An element is called a peak element when both left and right
# of an element is smaller


# 1. Naive Approach - Time complexity: O(n),Auxiliary Space: O(1)
def findPeakElem(arr, n):
    peak_el = arr[0]
    if n == 1:
        return arr[0]

    for i in range(n-1):
        if arr[i] < arr[i+1] and peak_el < arr[i+1]:
            peak_el = arr[i+1]
    return peak_el


# 2. Binary Search - Time complexity: O(logN), Auxiliary Space: O(1)
def findPeakElemBinarySearch(arr, start, end, n):
    #1st get the mid element ind
    mid = (start+end)//2

    # if mid elem is the 1st elem the there is no elem 
    # left of it, then we only have to check for right side
    # nebour elem of it, if it is < then mid lem the mid 
    # is the peak elem.
    if mid == 0 and arr[mid] > arr[mid+1]:
        return arr[mid]
    
    # if mid elem is the last elem the there is no elem 
    # right of it, then we only have to check for left side
    # nebour elem of it, if it is < then mid lem the mid 
    # is the peak elem.
    elif mid == n-1 and arr[mid] > arr[mid -1]:
        return arr[mid]

    # if mid elem is the any elem except 1st & last and 
    # left & right elem is lesser then mid then mid is the
    # peak elem.
    elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    
    # below cond. check if left elem is > mid elem then 
    # we have search in left subarray, because there can 
    # be a chance to find the bigger elem in the left side
    # of the arr
    elif mid > 0 and arr[mid] < arr[mid-1]:
        return findPeakElemBinarySearch(arr, start, mid-1, n)
    else:
        return findPeakElemBinarySearch(arr, mid+1, end, n)

arr = [15,35,85,82,5,6,8,7]
n = len(arr)
res = findPeakElem(arr, n)
print("Peak elem from Naive Approach is: ", res)

res = findPeakElemBinarySearch(arr, 0, n-1, n)
print("Peak elem from Binary Search Approach is: ", res)