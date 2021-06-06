# Reconstruct array obtained by doing Xor of consecutive elements in the array.
def game_with_number(arr, n):
    newarr = []
    for i in range(1, n):
        j = i - 1
        newarr.append(arr[j] ^ arr[i])
    newarr.append(arr[-1])
    return newarr


n = int(input())
arr = list(map(int, input().strip().split()))
res = game_with_number(arr, n)
print(*res)
