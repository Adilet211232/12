array = [64, 23, 89, 6, 5, 1, 12, 33]


def bubble_sort(array):
    swapped = False
    for num_1 in range(len(array) - 1, 0, -1):
        for num_2 in range(num_1):
            if array[num_2] > array[num_2 + 1]:
                array[num_2], array[num_2 + 1] = array[num_2 + 1], array[num_2]
                swapped = True
        if swapped:
                swapped = False
        else:
            break
    return array


print(f'sorted list:{bubble_sort(array)}')

