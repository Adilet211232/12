array = [64, 23, 89, 6, 5, 1, 12, 33]


def quick_sort(array):
    if len(array) <= 1:
        return array
    element = array[0]
    left = list(filter(lambda num: num<element, array))
    center = [nums for nums in array if nums == element]
    righ = list(filter(lambda num: num > element, array))

    return quick_sort(left) + center + quick_sort(righ)


print(f'sorted list:{quick_sort(array)}')


