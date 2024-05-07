def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def find_median(arr):
    sorted_arr = merge_sort(arr)
    n = len(sorted_arr)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        median = sorted_arr[mid]

    return median


N = int(input())
arr = list(map(int, input().split()))

median = find_median(arr)
print(median)
