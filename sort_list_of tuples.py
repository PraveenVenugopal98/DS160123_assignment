# l=[(4,9,1),(14,8,0),(1,3),(5,6)]
# l.sort(key=lambda x:x[-1])
# print(l)

# l=[(4,9,1),(14,8,0),(1,3),(5,6)]
# def last(a):
#     return a[-1]
# l.sort(key=last)
# print(l)


# l=[(4,9,1),(14,8,0),(1,3),(5,1),(0,)]
n=int(input("Enter the number of elements in list : "))
l=[]
for i in range(n-1):
    t=[int(x) for x in input().split(",")]
    t=tuple(t)
    l.append(t)
print("Entred list of tuples : ",l)

sorted=[]
for j in range(len(l)):
    s=l[0][-1]
    m=0
    for i in range(len(l)):
        g=l[i][-1]
        if g<s:
            s=g
            m=i
    z=l.pop(m)
    sorted.append(z)
print("Sorted list of tuples : ",sorted)