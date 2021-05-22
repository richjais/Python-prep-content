def game_with_number (arr,  n) : 
    #Complete the function
    newarr = []
    for i in range(1,n):
        j=i-1
        newarr.append(arr[j]^arr[i])
    newarr.append(arr[-1])
    return newarr