def factorial(n) :
    if n==0 :
        return 1
    return n * factorial(n-1)



def main() :
    n = int(input())
    ans = n
    for i in range(2,n) :
        ans *= i
    print(n,"! =",ans)
    print(n,"! =",factorial(n))
    

main()
