
from database import *
class Order:
    def __init__(self):
        self.data = Database()
        self.welcome()

    def order_item(self):
        menu = self.data.show_menu()
        print("\n=========== MENU ===========")
        for item in menu:
            print(f"ID: {item[0]} | Item: {item[1]} | Price: ₹{item[2]}")
        print("============================\n")
    

    def login(self):
        password = "123@123"
        while True:
            print("=== Welcome Admin ===")
            passwd = input("Enter password: ")
        
            if passwd == password:
                print("Login Successful")
                while True:  
                    print("====================================")
                    print("Perform changes you want")
                    print("1.View Menu\n2.Insert Menu\n3.Update Menu\n4.Delete Menu\n5.Logout")
                    print("====================================")
                
                    m = int(input("Choose one: "))
                    if m==1:
                        self.order_item()
                    elif m == 2:

                        self.data.insert()
                    elif m == 3:
                        self.data.update()
                    elif m == 4:
                        self.data.delete()
                    elif m == 5:
                        print("Logging out from Admin panel...\n")
                        return  
                    else:
                        print("Enter a valid option")
            else:
                print("Wrong Password. Try Again")


    def welcome(self):
        while True:
            print("****************************** WELCOME *******************************")
            print("1.Customer\n2.Admin\n3.Exit")
            n = int(input("Choose an option: "))
            if n == 1:
                while True:
                    self.order_item()
                    print("=============================")
                    print("Order the dishes")
                    print("1.Single item\n2.Multiple Items")
                    n=int(input("pick one:"))
                    print("=====================================")
                    if n==1:
                        self.data.ord_item()
                    elif n==2:
                        self.data.customer_order()
                    else:
                        print("invalid")
                    again=input("Do You want anything else (yes/no):")
                    if again=="yes": continue
                    else: break
            elif n == 2:
                self.login()
            elif n==3:
                print("Thank You")
                break
            else:
                print("Choose a valid option")
obj=Order()