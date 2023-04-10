def multiply_n_times(val, n):
    z = 1

    for i in range(n):
        z = z * val

    return z

def find_nth_root(m, n):

    start = 1
    end = m

    while start <= end:

        mid = (start + end) // 2

        if multiply_n_times(mid, n) == m:
            return mid
        
        elif multiply_n_times(mid, n) < m:
            start = mid + 1

        else:
            end = mid - 1

print(find_nth_root(64, 2))
