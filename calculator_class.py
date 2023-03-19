class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        return self.num2/self.num1
    
num1=float(input("Enter num1 : "))
num2=float(input("Enter num2 : "))

obj=Calculator(num1,num2)
ans1=obj.add()
ans2=obj.sub() 
ans3=obj.mul()
ans4=obj.div()

print(f"\nOUTPUT     [{obj.num1},{obj.num2}]\nSum        = {ans1}\nDifference = {ans2}\nProduct    = {ans3}\nQuotent    = {ans4}")

print("\n\nGenerating outputs for pre-set inputs")
obj1=Calculator(1,5.5)
ans11=obj1.add()
ans12=obj1.sub() 
ans13=obj1.mul()
ans14=obj1.div()

obj2=Calculator(20,10)
ans21=obj2.add()
ans22=obj2.sub()
ans23=obj2.mul()
ans24=obj2.div()

print(f"\nOUTPUT     [{obj1.num1},{obj1.num2}]\nSum        = {ans11}\nDifference = {ans12}\nProduct    = {ans13}\nQuotent    = {ans14}")
print(f"\nOUTPUT     [{obj2.num1},{obj2.num2}]\nSum        = {ans21}\nDifference = {ans22}\nProduct    = {ans23}\nQuotent    = {ans24}")