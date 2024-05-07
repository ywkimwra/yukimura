def odd_even_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] % 2 == 0 and arr[j] % 2 == 0 and arr[i] > arr[j]) or (
                arr[i] % 2 != 0 and arr[j] % 2 != 0 and arr[i] < arr[j]
            ):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


N = int(input())
arr = list(map(int, input().split()))

sorted_arr = odd_even_sort(arr)

for num in sorted_arr:
    print(num, end=" ")
