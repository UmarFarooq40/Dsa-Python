arr=[12,3,4322,123,1234,1323,133,1,23]
target=1323

def BinarySearch():
    arr.sort()
    s=0
    n=len(arr)-1
    while s<n:
        mid=(s+n)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            s=mid+1
        else:
            n=mid-1
    return -1
print(BinarySearch())

