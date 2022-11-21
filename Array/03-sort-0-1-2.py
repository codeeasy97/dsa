# Sort an array of 0s, 1s and 2s |
# Dutch National Flag problem

"""
Step-1:  take 3 pointer low, mid, high
            Initialize low = mid =0 and high = n-1
Step-2: start loop untill mid<= high

Step3:  if array mid is == 0: 
            swap(arr[low], arr[mid])
            low = low + 1
            mid = mid + 1
        elif array mid is == 1:
            mid = mid + 1
        elif array mid is == 2:
            swap(arr[mid], arr[hight])
            high = high - 1
return arr
"""

def solveDutchFlagProblem(arr):
    n = len(arr)
    low = mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr

arr = [0, 1, 2, 0, 1, 2]
result = solveDutchFlagProblem(arr)
print("Sorted array is:", result)