# Find the minimum and maximum element in an array

def findMinMax(arr, n):
    min = float('inf')
    max = float('-inf')
    for x in range(0,n):
        if arr[x] < min:
            min = arr[x]
        if arr[x] > max:
            max = arr[x]
    return [min,max]

arr = [1,340, 240, 20, 560]
n = len(arr)
res = findMinMax(arr, n)
print("Min value is:", res[0])
print("Max value is:", res[1])