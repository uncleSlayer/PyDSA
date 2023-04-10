def twoSum(nums, target):

        for r in range(len(nums)):

            for xr in range(len(nums)):

                if r == xr:
                    pass
                
                else:
                    if nums[r] + nums[xr] == target:
                        return [r, xr]
                    
print(twoSum([2,7,11,15], 9))