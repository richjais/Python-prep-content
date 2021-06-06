# In sorted array A of size N. Find number of elements which are less than or equal to given element X.
# As the whole array is sorted: use binary search to find result.

def smallElementToX(arr, n, X):
    beg = 0
    end = n - 1
    count = 0
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] < X:
            beg = mid + 1
            count = mid + 1
        else:
            end = mid - 1
    return count


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
X = int(input())
res = smallElementToX(arr, n, X)
print(res)
