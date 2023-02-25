def classify(*a):
    for i in sent:
        if ord(i) in range(65,91):
            u.append(i)
        elif ord(i) in range(97,123):
            l.append(i)
        else:
            o.append(i)

sent=input("Enter the sentance : ")
u=[]
l=[]
o=[]
classify(sent)
print("Upper case letter are : ", u, "Total no. of upper case letters : ",len(u))
print("Lower case letter are : ", l, "Total no. of lower case letters : ",len(l))
print("Other letter are : ", o, "Total no. of other letters : ",len(o))
