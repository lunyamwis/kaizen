def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = int((low + high) / 2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19]
print(len(data))
dt = binary_search(data, 4, 1, 10)
print(dt)
