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


nums = []

while True:
    num = float(input())
    if num == -1:
        break
    nums.append(num)


sorted_nums = merge_sort_descending(nums)

if len(sorted_nums) <= 1:
    print(-1)
else:
    max_num = sorted_nums[0]
    second_max_num = sorted_nums[1]

    if max_num == second_max_num:
        print(-1)
    else:
        print(second_max_num)
