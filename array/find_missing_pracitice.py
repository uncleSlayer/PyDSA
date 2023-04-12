arr = [0,-10,1,3,-20]
n = 5

def check_present(index, nums):
    for ind in nums:

        if index == 0:
            return True
            
        if index == ind:
            continue

        else:
            return False

def solution(arr, n):

    check_arr = [0] * n

    for index in range(n):
        check_arr[index] = index
    
    for index, value in enumerate(check_arr):

        if check_present(value, arr) == True:
            continue

        else:
            return index




print(solution(arr, n))