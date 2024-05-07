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
        if left[i][1] > right[j][1] or (
            left[i][1] == right[j][1] and left[i][0] < right[j][0]
        ):
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


N, k = map(int, input().split())

students = []
for _ in range(N):
    code, grade = input().split()
    students.append((int(code), float(grade)))

students = merge_sort(students)

for i in range(k):
    print(students[i][0])
