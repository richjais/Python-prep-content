def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

def rotateClockwise(arr,d,n):
    if d == 0:
        return
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

t=int(input())
while t:
    t-=1
    arrsize,d=map(int,input().split())
    arr=[]
    arr=input().split()
    rotateClockwise(arr,d,arrsize)
    for x in arr:
        print(x,end=" ")
    print()