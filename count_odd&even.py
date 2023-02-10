s=[1,2,5,9,45,65,85,4,42,0,66,97]
odd=[]
even=[]
for i in s:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Odd : ",odd,"Even : ",even)
print("Total no. of odd numbers : ",len(odd))
print("Total no. of even numbers : ",len(even))
