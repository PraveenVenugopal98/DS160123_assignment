#Food ordering Application named #FOODIE
#Enable Admin to Add, Edit & Remove food items, Display the menu
#Enables users to Sign-up and login
#Enables authorized user to order ther food based on food id as input
#Displays the order food and ask for confirmation to place order
#Generates bill for the order, considering the discount 
#Reduces the stock number as orders are placed and removes item from menu once stock become "0"
#Display order history
#log out of the session and relogin as new user and carry out the above functions, with updated data

class admin:
    def __init__(self):
        self.food={1:{"Name":"Tandoori Chicken","Quantity":"4 pieces","Price":240,"Discount":0,"Stock":20},2:{"Name":"Vegan Burger","Quantity":"1 pieces","Price":320,"Discount":10,"Stock":10},3:{"Name":"Truffle Cake","Quantity":"500 gm","Price":900,"Discount":15,"Stock":5}}
        self.foodid=3
        
    def add_item(self):
        self.foodid=self.foodid+1
        self.name=input("Enter Food Name : ")
        self.quantity=input("Enter Quantity : ")
        self.price=int(input("Enter Price in INR : "))
        self.discount=int(input("Enter Discount in % : "))
        self.stock=int(input("Enter Stock in nos. : "))
        self.item={"Name":self.name,"Quantity":self.quantity,"Price":self.price,"Discount":self.discount,"Stock":self.stock}
        self.food[self.foodid]=self.item
        print("\n#---Item Added Succesfully---#\n")
        print(self.food)
        
    def edit_item(self):
        print(self.food.keys())
        edit=int(input("Enter Food ID to Edit : "))
        self.food[edit]["Name"]=input("Enter Food Name : ")
        self.food[edit]["Quantity"]=input("Enter Quantity : ")
        self.food[edit]["Price"]=int(input("Enter Price in INR : "))
        self.food[edit]["Discount"]=int(input("Enter Discount in % : "))
        self.food[edit]["Stock"]=int(input("Enter Stock in nos. : "))
        print("#---Item Edited Succesfully---#")
        print("Edited Item \n", self.food[edit])
        
    def view_item(self):
       for i in self.food:
           print("\nFood ID : ",i)
           for j in self.food[i]:
               print(f"# {j} : {self.food[i][j]}")
               
    def remove_item(self):
        rem=int(input("Enter Food ID to be delited : "))
        if rem in self.food:
            del self.food[rem]
            print("#---Item removed succesfully---#")
            print("Remaining items are : ", self.food)
        else:
            print("\nItem not available to delit")
        
class user(admin):
    def __init__(self):
        super().__init__()
        self.user_data={"user@123":{"Full Name":"Tommy","Address":"Pondicherry","Phone Number":"9597183510","Email ID":"user@123","Password":"123","Order History":{}}}
        #self.orderedfood={}
        
    def registration(self):
        self.name=input("Enter Full Name : ")
        self.phone=input("Enter Phone number : ")
        self.email=input("Enter Email ID : ")
        self.address=input("Enter Address : ")
        self.password=input("Enter Password : ")
        self.user_info={"Full Name":self.name,"Phone Number":self.phone,"Email ID":self.email,"Address":self.address,"Password":self.password,"Order History":{}}
        self.user_data[self.email]=self.user_info
        print("\n###--Registration succesful--###\n")
        print(self.user_info)
        
    def login(self):
        while True:
            self.em=input("Enter Email ID : ")
            loginpword=input("Enter Password : ")
            if self.em in self.user_data.keys():
                if loginpword==self.user_data[self.em]["Password"]:
                   return(self.user_data[self.em]["Full Name"])
                else:
                    print("\nIncorrect Password")
                    break
            else:
                print("\nEmail ID not registered")
                break
            
    def place_order(self):
        while True:
            print("\nPlease make your order by Food Id")
            self.od=[int(k) for k in input("\nEnter Food Id of Item to be ordered : ").split(",")]
            self.odr=[]
            if (set(self.od)).issubset(set(admin.food)):
                for fod in self.od:
                    self.odr.append(admin.food[fod]["Name"])
                print("\nYour have ordered\n")
                for i in self.odr:
                    print(i)
                break
            else :
                print("\n##-- Items you chose not available --##\n Please make other choice")
            
        while True:
            print("\n###--- Please Confirm Your order ---###\n\n #--- 1 Yes\n #--- 2 NO")
            o=int(input("\nEnter your choice : "))
            if o==1:
                #self.orderedfood={}
                time=dt.now().strftime("%d %m %Y %H:%M:%S")
                self.user_data[self.em]['Order History'][time]=self.odr
                print("\nYour Order is Placed\n")
                print(self.user_data[self.em]["Order History"][time])
                user.bill()
                break
            elif o==2:
                print("\nYour Order is Cancelled")
                break
            else:
                print("Please enter correct input")
                
    def bill(self):
        bills=0
        dbills=0
        print("\n\n$$$$$-----BILL-----$$$$$\n")
        for i in self.od:
            print(f"{admin.food[i]['Name']} --- {admin.food[i]['Quantity']} --- {admin.food[i]['Price']}INR --- {admin.food[i]['Discount']}% Discount --- Offer Price : {(admin.food[i]['Price'])*(1-0.01*(admin.food[i]['Discount']))}")
            bills= admin.food[i]["Price"] + bills
            dbills= (admin.food[i]["Price"])*(1-0.01*(admin.food[i]["Discount"]))+dbills
            admin.food[i]["Stock"]=admin.food[i]["Stock"]-1
            if admin.food[i]["Stock"]==0:
                del admin.food[i]                
        print("\nActual Bill     : INR ",bills)
        print("Discounted Bill : INR ",dbills)
        
    def order_history(self):
        print("\n**ORDER HISTORY**\n")
        for i in self.user_data[self.em]["Order History"]:
            print(f"{i} : {self.user_data[self.em]['Order History'][i]}")
        
    def update_profile(self):
        print("\nYour Profile")
        print("Available data :",self.user_data[self.em].keys())
        data=input("Enter the data to be edited : ")
        edit=input(f"Enter {data} : ")
        self.user_data[self.em][data]=edit
    

from datetime import datetime as dt
admin=admin()
user=user()
while True:
    print("\n####--------Welcome to FOODIE--------####")
    print("\nLogin as :\n           #1--- Admin\n           #2--- User\n")
    log=input("Enter your choice : ")
    print("")
    while True:
        if log =="1":
            print("\nWelcome ADMIN")
            print("\n #1--- Add Food items\n #2--- Edit Food items\n #3--- View items\n #4--- Remove Food item\n #5--- Exit\n")
            a=input("Enter Your Choice : ")
            print("")
            if a=="1":
                admin.add_item()
            elif a=="2":
                admin.edit_item()
            elif a=="3":
                admin.view_item()
            elif a=="4":
                admin.remove_item()
            elif a=="5":
                print("\n\n###--- Thank You ---###")
                break
            else:
                print("Please enter correct input")
        elif log=="2":
            print("\nAlready an registered user ?\n #1--- Login\n #2--- Sign-up\n #3--- Exit\n")
            b=input("Enter Your Choice : ")
            if b=="1":
                logusr=user.login()
                if logusr!=None:
                    print(f"\n###--- Welcome {logusr} ---###")
                    while True:                      
                        print("\n #1--- Place new order\n #2--- Order History\n #3--- Update Profile\n #4--- Logout\n")
                        c=input("Enter Your Choice : ")
                        if c=="1":
                            admin.view_item()
                            user.place_order()
                        elif c=="2":
                            user.order_history()
                        elif c=="3":
                            user.update_profile()
                        elif c=="4":
                            print("\n###---Your Session Succesfully Ended---###")
                            break
                        else:
                            print("\n$$$--Please enter correct input---$$$")                    
            elif b=="2":
                user.registration()
            elif b=="3":
                break
            else:
                print("\n$$$--Please enter correct input---$$$")
        else:
            print("\n$$$--Please enter correct input---$$$")
            break