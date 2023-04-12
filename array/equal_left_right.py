arr = [1,3,5,2,2]
n = 5


left_sum = 0
right_sum = 0
arr_sum = 0

for number in arr:
        arr_sum += number
        
for index, number in enumerate(arr):
    right_sum = arr_sum - (left_sum + number)
    
    if right_sum == left_sum:
        print(arr[index - 1])
        break
        
    else:
        left_sum += number
    