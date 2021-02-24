
def main() :
    n = int(input())
    l = list(map(int,input().split()))

    m = max(l)
    if m<0 :
        print(m)
        return

    ms,cs = 0,0
    for i in range(n) :
        cs = max(0,cs+l[i])
        ms = max(cs,ms)
    print(ms)

main()
