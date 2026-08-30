arr = list(map(int, input("Enter the array: ").split()))
target = int(input("Enter the element to search: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        break
else:
    print("Element not found")