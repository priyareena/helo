def findMin(arr, low, high):
    min = arr[low]
    i = low
    for i in range(high+1):
        if arr[i] > min:
            min = arr[i]
    return min
arr = [1, 30, 40, 50, 60, 70, 23, 20]
n = len(arr)
print ("The min element is %d"%
        findMin(arr, 0, n-1))
 
