#10.Maximum Consecutive Ones

def FindMaxConsecutiveOnes():
    arr = list(map(int,input().split()))

    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count+=1
            maximum = max(maximum,count)
        else:
            count = 0
    return maximum

FindMaxConsecutiveOnes()