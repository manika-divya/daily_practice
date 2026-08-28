arr = list(map(int,input('enter the values: ').split()))

lar = arr[0]

for num in arr:
    if num>lar:
        lar = num

print('Largest number is ',lar)