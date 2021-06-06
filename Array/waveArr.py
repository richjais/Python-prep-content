def convertToWave(A, N):
    # Your code here
    flag = True
    for i in range(1, N):
        j = i - 1
        if flag:
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]
            flag = False
        else:
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
            flag = True


n = int(input())
arr = list(map(int, input().strip().split()))
convertToWave(arr, n)
print(*arr)
