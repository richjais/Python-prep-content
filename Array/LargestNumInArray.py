def largest( arr, n):
    largest = -1
    if n!=0:
        for x in arr:
            if largest<x:
                largest =x
                
    return largest