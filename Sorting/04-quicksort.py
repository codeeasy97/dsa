# Sort an Array using the Quicksort algorithm	

"""
1.  take 1st elem as pivot
2.  count all elem which is less then the pivot
3.  place pivot on its correct place
4.  make sure left of pivot is smaller and right is greater then the pivot elem
6. return pivot index
"""

def partition(arr, low, high):
    print("low:{} high:{}".format(low,high))
    pivot = arr[low] #take 1st elem as pivot
    
    #this is used to store count of elem which 
    # is smaller then pivot
    count = 0
    
    # find elem which is smaller then pivot
    for x in range(low+1, n):
        if arr[x] < pivot:
            count = count + 1
    print("low:{} count:{}".format(low,count))
    #updated pivot ind
    pivotInd = low + count

    #swap pivot on right place
    arr[pivotInd], arr[low] = pivot, arr[pivotInd]
    print("\n")
    print("pivot place for low:{} high:{} & arr ".format(low,high),arr)
    print("\n")
    # Now place smaller elem is left of pivot and greater elem 
    # is at right of pivot
    i = low
    j = high
    print("arr[i]:{} arr[j]:{} i:{} j:{} pivotInd:{} pivot:{}".format(arr[i], arr[j], i, j, pivotInd, pivot))
    print("\n")

    #start loop for left and right part sorting
    while i < pivotInd and j >= pivotInd:
        #left part and smaller to pivot, 
        while arr[i] < pivot:
            i = i + 1
        #right part and greater to pivot,
        while arr[j] > pivot:
            j = j - 1
        print("arr[i]:{} arr[j]:{} i:{} j:{}".format(arr[i],arr[j],i,j))
        print("-------------\n")
        #this cond comes when either left part elem 
        # is bigger and right part elem is small then pivot
        if i < pivotInd and j > pivotInd:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
        print(arr)
        print("arr[i]:{} arr[j]:{} i:{} j:{} pivotInd:{} pivot:{}".format(arr[i], arr[j], i, j, pivotInd, pivot))
        print("=================\n")
    return pivotInd

def quickSort(arr, low, high):
    if low >= high:
        # print("call cond low:{} high:{}".format(low,high))
        return

    p = partition(arr, low, high)
    quickSort(arr, low, p - 1)
    print("call right:p:{} low:{} high:{}".format(p+1,low,high))
    quickSort(arr, p+1, high)

arr = [8,10,2,1,3,4,6,5,7,9]

n = len(arr)
quickSort(arr, 0, n-1)
print("\n")
print("final result: ",arr)