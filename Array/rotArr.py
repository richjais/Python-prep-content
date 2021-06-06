def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def rotateD(arr,n,d):
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

arrsize = int(input())
arr = [int(input()) for _ in range(arrsize)]
d = int(input())
rotateD(arr,arrsize,d)
print(arr)