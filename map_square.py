def square(a):
    s=int(a)**2
    return(s)
# l=[1,56,6,8,10]
l=input("Enter list of numbers to be squared : ").split(",")
x=list(map(square,l))
print("Squared list : ",x)