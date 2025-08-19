import functools


@functools.lru_cache(maxsize=None)
def max_subarray_sum(arr):
    if not arr:
        return 0

    current_sum = max_sum = arr[0]
    max_subarray = [arr[0]]

    for num in arr[1:]:
        if num > current_sum + num:
            current_sum = num
            max_subarray = [num]
        else:
            current_sum += num
            max_subarray.append(num)
            max_sum = max(max_sum, current_sum)
    return max_sum, max_subarray


arreglo = tuple([1, -2, 3, 10, -4, 7, 2, -5])
resultado, subarray = max_subarray_sum(arreglo)
print("Suma máxima:", resultado)
print("Subarreglo:", subarray)
