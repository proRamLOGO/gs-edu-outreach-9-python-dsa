def f(x,n) :
    if x==n :
        return
    print(x)
    x += 1
    f(x,n)


def main() :
    i = 0
    while i < 10 :
        i += 1
    print("-------------")
    f(0,10)

main()
