arr = list(map(int,input('enter the values: ').split()))

lar = arr[0]
sec = arr[1]

if lar < sec:
    lar, sec = sec, lar

for i in arr:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec and i != lar:
        sec = i

print("Second largest:", sec)
