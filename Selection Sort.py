arr = list(map(int,input().split(' ')))
print (arr)
for i in range(len(arr)):
    min = i 
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min],arr[i]
print (arr)
