def prime( num ) :
    i = 2
    print("sqrt of num : ",num**0.5)
    while i <= num**0.5 :
        print(i, (i <= num**0.5) )
        if num%i == 0 :
            return False
        i += 1
    else :
        return True

print("Prime" if prime( int(input()) ) else "NOT PRIME" )


