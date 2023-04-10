nums = [1,1,1,1,1]
sumnum = 0

def sum(arr, sumnum):
    for idx, i in enumerate(nums):

        nums[idx] = sumnum + i
        sumnum += i
    
    print(nums)


sum(nums, sumnum)