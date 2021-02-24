def binarySearch( l, num ) :
    lo = 0
    hi = len(l)-1

    while lo <= hi :
        mid = (lo+hi)//2
        if l[mid]==num :
            return mid
        elif l[mid] > num :
            hi = mid-1
        else :
            lo = mid+1
    else :
        return -1

print(binarySearch( [6,2,3,4,5,1], 6 ))
