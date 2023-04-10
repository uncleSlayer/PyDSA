arr = [1, -1, 3, 2, -7, -5, 11, 6]

n = len(arr)

def sort_it(nums):

    ans = []

    for i in nums:
        if i > 0:
            ans.append(i)

    for i in nums:
        if i < 0:
            ans.append(i)
        
    print(ans)


sort_it(arr)