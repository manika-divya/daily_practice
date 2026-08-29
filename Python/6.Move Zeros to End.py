#6.Move Zeros to End

arr = list(map(int,input().split()))
res = []

for num in arr:
    if num != 0:
        res.append(num)

for num in arr:
    if num==0:
        res.append(num)

print(*res)