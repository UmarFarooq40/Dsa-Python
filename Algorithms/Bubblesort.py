arr=[12,3,4322,123,1234,1323,133,1,23]
n=len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)

