def minMax(arr, n):
    min = arr[0]
    max = arr[0]
    for idx in range(1, n):
        if min > arr[idx]:
            min = arr[idx]
        if max < arr[idx]:
            max = arr[idx]
    return min, max


arrsize = int(input())
arr = [int(input()) for _ in range(arrsize)]
x, y = minMax(arr, arrsize)
print("min = ", x, " max = ", y)
