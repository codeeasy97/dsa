# Sort an array in wave form

def sortArrToWave(arr, n):
    for i in range(1, n, 2):
        if i < n-1 and arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
        if arr[i] > arr[i-1]:
            arr[i],arr[i-1] = arr[i-1], arr[i]
    return arr
                                
# arr = [10, 5, 6, 3, 2, 20, 100, 80]
#     #    10, 5, 6, 2, 20, 3, 100, 80
         
arr = [2,6]

n = len(arr)
res = sortArrToWave(arr, n)
print("Wave arr is: ", res)