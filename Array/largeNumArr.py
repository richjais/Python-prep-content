def largeNum(arr, n):
    if n == 0:
        return -1
    maxnum = arr[0]
    for idx in range(1, n):
        if maxnum < arr[idx]:
            maxnum = arr[idx]
    return maxnum


arrsize = int(input())
arr = [int(input()) for _ in range(arrsize)]
print("largeNum = ", largeNum(arr, arrsize))
