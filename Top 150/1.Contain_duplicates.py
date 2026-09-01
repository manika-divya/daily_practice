arr = list(map(int,input('Enter the values: ').split()))

arr.sort()

for i in range(1,len(arr)-1):
    if arr[i] == arr[i-1]:
        print("Contain Duplicates")
        break
print("Not contain any duplicates")