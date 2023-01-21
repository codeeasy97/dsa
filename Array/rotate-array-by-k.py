
# Cyclic Rotate an Array By k place 

#Method 1 : SC - O(N) , TC - O(N)

def rotateArray(arr, n, k):
    temp = [0]*n
    for i in range(n):
        temp[(i+k)%n] = arr[i]
        arr = temp
    return arr

#Method 2 : SC - O(1) , TC - O(N)
def  roateArrayOptimize(arr, n , k):
    k = k % n # 3%1 = 1
    l , r = 0, n - 1
    while l < r:
        arr[l],arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
    # [10,9,8,7,6,5,4,3,2,1]

    l , r = 0, k -1
    while l < r:
        arr[l],arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1

    # [8,9,10, 7,6,5,4,3,2,1]
    l, r = k, n - 1 
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r -1
    # [8,9,10, 1,2,3,4,5,6,7]


arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [-1]
k = 3
n = len(arr)

# res = rotateArray(arr, n, k)
# print(res)


roateArrayOptimize(arr, n , k)
print(arr)
