def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10


    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]


    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1


    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr



input_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(input_array)
print("Sorted Array:", sorted_array)
