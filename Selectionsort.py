arr=list(map(int,input().split()))
for i in range(len(arr)):
   m=i
   for j in range(i,len(arr)):
      if arr[i]>arr[j]:
        m=j
   arr[i],arr[m]=arr[m],arr[i]
print(arr) 