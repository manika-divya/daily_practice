arr = list(map(int,input("Enter the values: ").split()))

j = 0

for i in range(1, len(arr)):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

print(arr[:j + 1])
