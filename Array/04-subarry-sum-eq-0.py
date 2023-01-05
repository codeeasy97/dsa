# Find if there is any subarray with a sum equal to zero

def subArraySumZero(arr, n):
    
    for i in range(0,n):
        sum = arr[i]
        for j in range(i+1, n):
            sum = sum + arr[j]
            if sum == 0:
                return True
    return False


# sum every element and put sum in set and check if sum already exist in set, 
# if yes the there can be a zero sum
# why check in set ?
# Because if sum present in set then there is a possibility 
# that the arr has subarray which has 0 sum


def subArraySumZero2(arr, n):
    sum = 0
    s = set()
    for i in range(n):
        sum +=arr[i] #sum = sum + arr[i]
        if sum == 0 or sum in s:
            return True
        s.add(arr[i])
    return False




arr = [4, 2, -3, 1, 6]

# arr = [3, -1, -2, 5]
n = len(arr)
res = subArraySumZero2(arr, n)

if res:
    print("Yes")
else:
    print("No")