# def insertion_sort_descending(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] < key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_descending(left)
    right = merge_sort_descending(right)

    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


N = int(input())
arr = list(map(int, input().split()))

arr = merge_sort_descending(arr)

print(" ".join(map(str, arr)))
