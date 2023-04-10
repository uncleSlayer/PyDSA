def multiply_n_times(num):
        z = 1
        for i in range(2):
            z = z * num
        
        return z


def mySqrt(x: int) -> int:

        start = 0
        end = x

        while start <= end:

            mid = (start + end) // 2

            if multiply_n_times(mid) == x:
                return mid

            elif multiply_n_times(mid) < x:
                start = mid + 1
            
            elif multiply_n_times(mid) > x:
                end = mid - 1
            

print(mySqrt(144))