def majorityElement(nums):

        min_val = min(nums)
        max_val = max(nums)

        range_val = (max_val - min_val) + 1

        freq = [0] * range_val

        for val in nums:

            fidx = val - min_val

            freq[fidx] += 1

        max_val_in_freq = freq[0]
        freq_index = None

        for idx, i in enumerate(freq):
            
            if i >= max_val_in_freq:

                max_val_in_freq = i
                freq_index = idx

        return freq_index + min_val


print(majorityElement([2,2,1,1,1,2,2]))