import sys
n = int(input())
arr = [int(i) for i in input().split()]
max_end = 0
max_so_far = -sys.maxsize - 1
for j in range(n):
    max_end += arr[j]
    if max_so_far < max_end:
        max_so_far = max_end
    if max_end < 0:
        max_end = 0
print(max_so_far)