# Write a program to reverse the array

def reverseSlicing(arr):
    new_arr = arr[::-1]
    return new_arr

def reverseItrate(arr):
    n = len(arr)
    mid = n//2
    print(mid, arr[mid])

    for x in range(0, mid):
        arr[x], arr[n-(x+1)] = arr[n-(x+1)], arr[x]
    return arr


arr = [1,2,3,4,5,6]

result = reverseItrate(arr)
print("Reverse element is:", result)