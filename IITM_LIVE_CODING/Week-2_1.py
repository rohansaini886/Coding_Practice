def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return False
def findIntersection(x, y):
    x = sorted(x)
    y = sorted(y)
    z = []
    for i in x:
        if binarySearch(list(y), 0, len(list(y)) - 1, i):
            z.append(i)
    return(z)
set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
result = findIntersection(set1, set2)
result.sort()
print(*result)
