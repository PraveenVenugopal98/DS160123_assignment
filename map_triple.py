def triple(a):
    t=int(a)*3
    return(t)
# l=[1,56,6,8,10]
l=input("Enter list of numbers to be tripled : ").split(",")
x=list(map(triple,l))
print("Tripled list : ",x)