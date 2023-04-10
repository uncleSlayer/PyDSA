nums = [1]

def check_avail(arr, n):
    if n == 0:
        return True
    
    status = False
    for j in arr:
        if j == n:
            status = True
        
    return status

def sort_nums():

    for i in range(len(nums) + 2):

        status = check_avail(nums, i)

        if status:
            continue

        else:
            return i




print(sort_nums())