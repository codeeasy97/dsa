# Find the Largest sum contiguous Subarray

#Time complexity: O(n)2
def largestSumSubArray(arr, n):
    max = float('-inf')
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j] #sum = sum + arr[j]
            if sum > max:
                max = sum
    return max

sum = 7
max = 7

"""
# 1st
{-2},{-2,-3},{-2,-3,4},{-2,-3, 4,-1}, {-2,-3,4,-1,-2},
{-2,-3,4,-1,-2, 1},{-2,-3,4,-1,-2,1,5},
{-2,-3,4,-1,-2,1,5,-3}
#2nd
{-3},{-3,4},{-3,4,-1},{-3,4,-1,-2},{-3,4,-1,-2,1},
{-3,4,-1,-2,1,5},{-3,4,-1,-2,1,5,-3}
# 3rd
{4},{4,-1},{4-1,-2},{4,-1,-2,1},{4,-1,-2,1,5},
{4,-1,-2,1,5,-3}
# 4th
{-1},{-1-2},{-1,-2,1},{-1,-2,1,5},{-1,-2,1,5,-3}
# 5th
{-2},{-2,1},{-2,1,5},{-2,1,5,-3}
# 6th
{1},{1,5},{1,5,-3}
# 7th
{5},{5,-3}
# 8th
{-3}
"""
# arr = [-2,-1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-1, 1 , 1, 1, 1, -1, -5, 10,9,-6,-1,10]

#Time complexity: O(n)
#kadane's Algo
"""
sum = sum+arr[i]
update maxi: maxi=max(maxi,sum)
if sum < 0: sum = 0 (do not take subarray which has sum < 0 start from new)
"""
def largestSumSubArray2(arr, n):
    sum = 0
    maxi = float('-inf')
    for i in range(n):
        sum = sum + arr[i]
        maxi = max(maxi,sum)
        if sum < 0:
            sum = 0

    return maxi

sum = 0 | 0 | 4 | 3 | 1 | 2 | 7 | 4
maxi = -2 | 4 | 7

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
res = largestSumSubArray(arr, n)
print(res)

