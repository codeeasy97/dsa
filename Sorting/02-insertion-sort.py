# Insertion Sort

# Time Complexity : O(n2)
# Space Complexity: O(1)
"""
1. compare first two element, swap if 2nd is large
[5, 6, 4, 3, 2, 1]
Note : save curr index value
run a inner loop untill curr index value > 0
So, for 1st pass inner loop will not run ,  0>0 = False
2. compare 2nd and 3rd, swap if 3rd is large
[5, 4, 6, 3, 2, 1] => [5, 4, 6, 3, 2, 1]
Here curr index is 1
Run inner loop and compare elem with all its prev elem
Here 4 < 5, a swap happen and curr ind decrease by 1
[5, 4, 6, 3, 2, 1] => [4, 5, 6, 3, 2, 1]
3. Do this for rest of the array
"""

def insertionSort(arr, n):
    for x in range(n-1):
        if arr[x] > arr[x+1]:
            arr[x], arr[x+1] = arr[x+1], arr[x]
        j = x
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1
    return arr

arr = [6, 5, 4, 3, 2, 1]

n = len(arr)
result = insertionSort(arr, n)
print("Sorted Array is:", result)