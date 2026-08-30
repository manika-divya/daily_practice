#8.Find the Union

arr1 = list(map(int,input('Enter the values:').split()))
arr2 = list(map(int,input('Enter the values:').split()))

union = []

for nums in arr1:
    if nums not in union:
        union.append(nums)

for nums in arr2:
    if nums not in union:
        union.append(nums)

print(*union)