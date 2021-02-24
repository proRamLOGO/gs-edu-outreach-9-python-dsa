n = int(input())


#def <fn_name>( [ <arg1>, <arg2>, ... ] ) :
    # statements

def prime( num ) :
    i = 2
    while i < num :
        if num%i == 0 :
            return False
        i += 1
    else :
        return True

x = 2
while x<=n :
    if prime(x) :
        print(x, end=", ")
    x += 1


