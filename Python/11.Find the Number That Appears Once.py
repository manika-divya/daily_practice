#11.Find the Number That Appears Once

def NumberThatAppearsOnce():
    arr = list(map(int,input().split()))
    res = 0

    for num in arr:
        res = res^num

    return res

NumberThatAppearsOnce()