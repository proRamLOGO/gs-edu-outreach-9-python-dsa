
def pow( a, b ) :
    ans = 1
    i = 0
    while i < b :
        ans *= a
        i += 1
    return ans


def binpow( a, b ) :
    ans = 1
    i = 0
    while b!=0 :
        if b&1 :
            ans *= a
        a *= a
        b >>= 1
        i += 1
    print("i", i)
    return ans


a = int(input())
b = 10000

print(binpow(a,b))
