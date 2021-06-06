# Find minimum value that can be added to an element so that array become balanced.
def minValueToBalance(a, n):
    left = sum(a[:n // 2])
    right = sum(a[n // 2:])
    return abs(left - right)

n = int(input())
arr = list(map(int, input().strip().split()))
res = minValueToBalance(arr, n)
print(res)