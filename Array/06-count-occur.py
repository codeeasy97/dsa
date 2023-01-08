# Count number of occurrences of an elem (or frequency) in a sorted array
# arr = [1, 2, 2, 2, 2, 2, 3]

def findOcurrItrative(arr,x):
    count = 0
    for elem in arr:
        if elem == x:
            count+=1
    return count

#binary search using recursion
def findOccur(arr, low, high, x, n):
    #base case
    if high < low:
        return -1

    #calculate mid index    
    mid = (low + high)//2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        #for left array
        return findOccur(arr, low, mid -1, x, n)

    #for right array
    return findOccur(arr, mid+1, high, x, n)

#input array
arr = [1, 2, 2, 2, 2, 2, 3]
#find element
x = 5

#caaling function
n = len(arr)
mid_ind  = findOccur(arr, 0, n-1, x, n)

#logic after index
if mid_ind == -1:
    print("\n")
    print("Occurrance of "+str(x)+" using binary search approach is:", 0)
else:

    left = mid_ind -1
    count = 1

    #traverse left subarray
    while left >=0 and arr[left] == x:
        count = count + 1
        left = left -1

    #traverse right subarray
    right = mid_ind+1
    while right < n and arr[right] == x:
        count = count + 1
        right = right + 1

    print("\n")
    print("Occurrance of "+str(x)+" using binary search approach is:", count)

print("\n\n")
count = findOcurrItrative(arr,x)
print("Occurrance of "+str(x)+" using iterative approach is: ", count)
print("\n")