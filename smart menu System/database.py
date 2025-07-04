import pymysql
class Database:
    def __init__(self):
        pass

    def connect(self):
        self.con = pymysql.connect(
            host="localhost",
            user="root",
            password="root123",
            database="project"
        )
        self.cur = self.con.cursor()


    
    def insert(self):
        print("Menu Insertion Tool")
        print("Enter items to add to the menu.")
        print("Type 'done' when finished.\n")

        item_id = input("Enter item ID (or type 'done' to finish): ")

        while item_id!= 'done':
            item_name = input("Enter item name: ")
            item_price = input("Enter item price: ")

            self.connect()
            query=("INSERT ignore INTO menu (id, item_name, price)VALUES (%s, %s, %s)")
            values = (int(item_id), item_name, float(item_price))
            self.cur.execute(query,values)
            self.con.commit()
            self.cur.close()
            self.con.close()

            print(f"Added: {item_name} (₹{item_price})\n")

            item_id = input("Enter next item ID (or type 'done' to finish): ")

        print("Menu insertion completed.")

    def delete(self):
        print("Menu Deletion Tool")
        print("Type 'done' to stop deleting.\n")
        item_id = input("Enter item ID to delete (or type 'done' to finish): ")
        while item_id!="done":
            self.connect()
            self.cur.execute("SELECT * FROM menu WHERE id = %s", (item_id,))
            item = self.cur.fetchone()

            if item:
                self.cur.execute("DELETE FROM menu WHERE id = %s", (item_id,))
                self.con.commit()
                print(f"Deleted item with ID {item_id}\n")
            else:
                print(f"No item found with ID {item_id}\n")
            item_id=input("Enter item ID to delete (or type 'done' to finish): ")
        print("Menu deletion completed ")
       
    def update(self):
        item_id=input("Enter item ID to update (or type 'done' to finish): ")
        while item_id!="done":
            self.connect()
            print("\n1.price\n2.items")
            option=int(input("choose one:"))
            if option==1:
                self.cur.execute("select * from menu where id=%s",{item_id})
                item=self.cur.fetchone()
                if item:
                    n_price=input("enter new price: ")
                    self.cur.execute("update  menu set price=%s  where id=%s",(n_price,item_id))
                    self.con.commit()
                    print("price updated succesfully")
                else:
                    print(f"No item found with ID {item_id}\n")
            elif option==2:
                self.cur.execute("select * from menu where id=%s",{item_id})
                item=self.cur.fetchone()
                if item:
                    n_item=input("enter new item: ")
                    self.cur.execute("update  menu set item_name= %s  where id=%s",(n_item,item_id))
                    self.con.commit()
                    print("item updated succesfully")
                else:
                    print(f"No item found with ID {item_id}\n")
            else:
                print("choose the valid one")
            item_id=input("Enter item ID to update (or type 'done' to finish): ")
        print("menu updated succesfully")

                             
    def show_menu(self):
        self.connect()
        self.cur.execute("SELECT * FROM menu")
        data = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return data
    def ord_item(self):
        item_id=input("choose the item_id: ")
        self.connect()
        self.cur.execute("select * from menu where id=%s",{item_id})
        data=self.cur.fetchone()
        if data:
            print(f" Item: {data[1]} | Price: ₹{data[2]}")
        else:
            print("Item not found.")
        self.cur.close()
        self.con.close()
        
    def customer_order(self):
        print(" Welcome to the Food Ordering System")
        print("================================================")
        self.connect()
        self.cur.execute("SELECT * FROM menu")
        items = self.cur.fetchall()

        if not items:
            print("No items available right now.")
            return
        else:
            print("\nEnter the item IDs you want to order (comma-separated):")
            selected_ids = input().split(",")

        total = 0
        ordered_items = []

        for item_id in selected_ids:
            self.cur.execute("SELECT * FROM menu WHERE id = %s", (item_id,))
            item = self.cur.fetchone()
            if item:
                ordered_items.append(item)
                total += item[2]  

        if ordered_items:
            print(" You ordered:")
            for item in ordered_items:
                print(f"- {item[1]} - ₹{item[2]}")
            print(f" Total Amount: ₹{total}")
            print("=================================================")
            print(" Thank you! Visit again!")
            print("=============================================")
        else:
            print(" No valid items selected.")

        
        
            
