# 21. List Sorting


# key can be "asc" or "des"
def mySort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if key == "des":
        return list(reversed(arr))
    else:
        return arr
