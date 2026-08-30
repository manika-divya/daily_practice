#9.Find Missing Number in an Array

def missing_num(arr):
    n = len(arr)

    expected_sum = n*(n+1)//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [3,0,1]
missing_num(arr)