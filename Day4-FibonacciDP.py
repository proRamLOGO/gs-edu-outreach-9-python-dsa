
def fib_td(n,l) :
    if l[n] != -1 :
        return l[n]

    if n<2:
        l[n] = n
        # print("n=",n,'\n',l,'\n')
        return n
    
    fn = fib_td(n-1,l) + fib_td(n-2,l)
    l[n] = fn

    # print("n=",n,'\n',l,'\n')
    
    return fn

def fib_bu(n) :

    f = [0]*(n+1)
    f[1] = 1
    for i in range(2,n+1) :
        f[i] = f[i-1] + f[i-2]
    
    print("l form bottom up = ",f)
    return f[n]
    

def main() :
    n = int(input())
    l = [-1]*(n+1)
    
    print(fib_td(n,l))
    print("l form top down = ",l)
    
    print(fib_bu(n))
    
    #print(l)

main()
