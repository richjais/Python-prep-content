def sumElement(arr,n):
    #code here
    for i in range(1,n):
        arr[0]+=arr[i]
        
    return arr[0]