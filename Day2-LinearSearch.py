n = int(input())

#def <fn_name>( [ <arg1>, <arg2>, ... ] ) :
    # statements

l = []
i = 0
while i<n :
    l.append(int(input()))
    i += 1
print(l)

num = int(input())

# print( num in l )

i = 0
while i<n :
    if l[i] == num :
        print("Number in List")
        break
    i += 1
else :
    print("Number NOT FOUND!")

