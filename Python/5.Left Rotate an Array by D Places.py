#5.Left Rotate an Array by D Places

arr = list(map(int,input().split()))
d = int(input())

for num in range(d):
    i = arr.pop(0)
    arr.append(i)

print(*arr)