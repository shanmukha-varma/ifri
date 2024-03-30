arr=[3,4,12,34,22,78]
for i in range(len(arr)):
    for j in range(i):
        if arr[i]<arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print(arr)