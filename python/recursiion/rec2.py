def Sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([3,4,5]))

