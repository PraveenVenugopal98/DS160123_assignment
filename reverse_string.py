w=input("Enter the word : ")
l=len(w)
rev=""
j=1
while j<=l:
    rev=rev+w[-j]
    j+=1
print("Reversed word : "rev)