#3.Two sum problem 

def TwoSum():
    arr = list(map(int,input('Enter the values: ').split()))
    target = int(input('Enter the target value: '))

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return i ,j

    return 
        

TwoSum()