array = [64, 23, 89, 6, 5, 1, 12, 33]


def binary_three():
    array = [64, 23, 89, 6, 5, 1, 12, 33]
    array.sort()
    print(array)

    desired_num = 98

    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != desired_num and low <= high:
        if desired_num > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high)// 2
    if low > high:
        print('no l')
    else:
        print('index:',mid)
binary_three()