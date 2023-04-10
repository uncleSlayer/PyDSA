nums = [3, 5, 2, 1, 4]

def sort_nums():

    for idx, i in enumerate(nums):

        if i == nums[i - 1]:
            continue

        else:

            temp = i
            nums[idx] = nums[i - 1]
            nums[i - 1] = temp

    print(nums)


sort_nums()