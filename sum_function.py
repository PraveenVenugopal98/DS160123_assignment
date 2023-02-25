def add(*a):
    s=0
    for i in l:
        s=i+s
    return(s)

l=[int(x) for x in input("Enter the list of numbers to be added :").split(",")]
sm=add(l)
print("Sum of the list :",sm)