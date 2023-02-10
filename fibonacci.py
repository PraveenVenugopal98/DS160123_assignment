a=0
b=1
e=int(input("Enter the end of series : "))
print(a,b,sep="\n")
while a+b<e:
    c=b
    b=b+a
    print(b)
    a=c
