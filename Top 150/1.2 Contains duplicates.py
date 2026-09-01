#1.2 Contains duplicates -> using hash set

def Contain_dupli(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        seen.add(num)

    return False

arr = list(map(int,input("Enter the values: ").split()))
Contain_dupli(arr)