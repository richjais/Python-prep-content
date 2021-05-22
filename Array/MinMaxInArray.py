def getMinMax( a, n):
    min=a[0]
    max=a[0]
    for elem in a:
        if min>elem:
            min=elem
        if max<elem:
            max=elem
    return min,max