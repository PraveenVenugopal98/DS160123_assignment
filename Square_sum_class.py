class Point:
    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def sq_sum (self):
        output=self.x**2+self.y**2+self.z**2
        return (output)


x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
z=int(input("Enter 3rd number : "))
obj= Point(x,y,z)
ans=obj.sq_sum()
print(f"The sum of squares of [{obj.x}, {obj.y}, {obj.z}] is : {ans}")

print("\nGenerating output for different set of preset inputs")

obj1= Point(5,2,13)
ans1=obj1.sq_sum()
obj2= Point(1,3,1)
ans2=obj2.sq_sum()
print(f"The sum of squares of [{obj1.x}, {obj1.y}, {obj1.z}] is : {ans1}")
print(f"The sum of squares of [{obj2.x}, {obj2.y}, {obj2.z}] is : {ans2}")