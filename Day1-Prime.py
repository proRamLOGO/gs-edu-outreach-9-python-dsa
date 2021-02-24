n = int(input())

x = 2
while x<=n :
    i = 2
    while i < x :
        if x%i == 0 :
            break
        i += 1
    else :
        print(x)
    x += 1


