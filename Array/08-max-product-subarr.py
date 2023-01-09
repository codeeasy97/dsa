# Maximum Product Subarray
# [6, -3, -10, 0, 2]
"""
mul = 6
maxi = '-inf' #initial value
maxi = max('-inf',6) #max(maxi,mul) | 6 
mul = -18

maxi = max(6,-18) #6
mul = -18*-10 = 180

maxi = max(6,180) #180
mul = 180*0 = 0

maxi = max(180,0) #180
mul = 0*2 = 0
"""
#TC- O(N)2 SC - O(1)
def maxProduct(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        mul = arr[i]
        for j in range(i+1, len(arr)):
            maxi = max(maxi,mul)
            mul = mul*arr[j]
    return maxi

#method-2 o(n) SC- O(1)
#maxi = 20*-2 = -40
#mini = 10*-2 = -20
def maxsubarrayproduct(arr):
    n = len(arr)
    maxi = arr[0]
    mini = arr[0]
    ans = arr[0]
    # [6, -3, -10, 0, 2]
    for i in range(1,n):
        if arr[i] < 0:
            maxi,mini = mini,maxi #swap when elem is neg
        #-10 : maxi = -18, mini= -3
        maxi = max(arr[i], maxi*arr[i])#-3 | 180 | 0 | 2
        mini = min(arr[i], mini*arr[i])#-18 | -10 | 0 | 0
        ans = max(ans,maxi)#6 | 180
    return ans

arr = [6, -3, -10, 0, 2]
res = maxProduct(arr)
print("\n")
print("Max product by Method-1: ",res)
print("\n")
res = maxsubarrayproduct(arr)
print("Max product by Method-2: ",res)
print("\n")