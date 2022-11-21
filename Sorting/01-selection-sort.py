# Sort An array Using Selection Sort

#How does it work (select lowest element)
# 1. on every pass find the lowest element and swap

# Find the smallest element, and put it to the first position.
# Find the next smallest element, and put it to the second position.
# Repeat until all elements are in the right positions.

def sortArrayUsingSelection(arr, n):
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        print(arr)
    return arr

arr = [5,4,3,2,1]
result = sortArrayUsingSelection(arr, len(arr))
print(result)