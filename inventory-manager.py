import json
import os
def save_data(data):
    with open("products.tmp","w") as file:
        json.dump(data,file,indent=4)
    os.replace("products.tmp","products.json")

def see_category(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        print("Categories available:")
        for key in data:
            print(key.title())
        print("Enter the category name below:")
        ent_cate=input("Enter the category name:").strip().lower()
        if not ent_cate:
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate in data:
            print(data[ent_cate])
            break
        else:
            print("This category doesn`t exist!")

def see_product(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        print("Categories available:")
        for key in data:
            print(key.title())
        ent_cate=input("Enter the product`s category:").strip().lower()
        if not ent_cate:
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate not in data:
            print("Such Category doesn`t exist!!")
        else:
            while True:
                ent_pro=input("Enter product`s name:").strip().lower()
                if not ent_pro:
                    print("Enter a Product name!!")
                elif ent_pro=="cancel":
                    print("The task has been cancelled!")
                    break
                elif ent_pro not in data[ent_cate]:
                    print("Such Product doesn`t exist!!")
                else:
                    print("Quantity Available:",data[ent_cate][ent_pro])
                    break
            break
def update_products(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        print("Categories Available:")
        for key in data:
            print(key.title())
        ent_cate=input("Enter the category:").strip().lower()
        if ent_cate=="":
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate not in data:
            print("This category doesn`t exist!!")
        else:
            while True:
                ent_pro=input("Enter product`s name:").strip().lower()
                if not ent_pro:
                    print("Enter a product name!!")
                elif ent_pro=="cancel":
                    print("The task has been cancelled!")
                    break
                elif ent_pro not in data[ent_cate]:
                    print("Such product doesn`t exist!!")
                else:
                    while True:
                       raw=input("Enter quantity of product:").strip().lower()
                       if raw=="":
                           print("Enter a number!!")
                       elif raw=="cancel":
                           print("The task has been cancelled!")
                           break
                       else:
                            try:
                               ent_quan=int(raw)
                            except ValueError:
                               print("Enter a number for quantity!!")
                               continue
                            if ent_quan<0:
                               print("Product`s quantity must be 0 or greater!!")
                            else:
                               data[ent_cate][ent_pro]=ent_quan
                               save_data(data)
                               print("Products updated successfully.")
                               break
                    break
            break

def add_category(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        ent_cate=input("Enter new category name:").strip().lower()
        if not ent_cate:
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate in data:
            print(f"{ent_cate} category already exists!")
        else:
            while True:
                ent_pro=input("Enter new category`s product:").strip().lower()
                if not ent_pro:
                    print("Enter a Product name!!")
                elif ent_pro=="cancel":
                    print("The task has been cancelled!")
                    break
                else:
                    while True:
                       raw=input("Enter quantity of product:").strip().lower()
                       if raw=="":
                            print("Enter a number!!")
                       elif raw=="cancel":
                           print("The task has been cancelled!")
                           break
                       else:
                            try:
                                ent_quan=int(raw)
                            except ValueError:
                                print("Enter a number for quantity!!")
                                continue
                            if ent_quan<0:
                                print("Product`s quantity must be 0 or greater!!")
                            else:
                               data.update({ent_cate:{ent_pro:ent_quan}})
                               save_data(data)
                               print("New Category created successfully!")
                               break
                    break
            break

def create_new_product(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        ent_cate=input("Enter category name:").strip().lower()
        if not ent_cate:
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate not in data:
            print("Enter a valid category!")
        else:
            while True:
                ent_pro=input("Enter new product`s name:").strip().lower()
                if not ent_pro:
                    print("Enter a Product name!!")
                elif ent_pro=="cancel":
                    print("The task has been cancelled!")
                    break
                elif ent_pro in data[ent_cate]:
                    print(f"This product already exist in {ent_cate}")
                else:
                    while True:
                        raw=input("Enter quantity of product:").strip().lower()
                        if raw=="":
                            print("Enter a number!!")
                        elif raw=="cancel":
                            print("The task has been cancelled!")
                            break
                        else:
                            try:
                                ent_quan=int(raw)
                            except ValueError:
                                print("Enter a number for quantity!!")
                                continue
                            if ent_quan<0:
                                print("Product`s quantity must be 0 or greater!!")
                            else:
                                data[ent_cate][ent_pro]=ent_quan
                                save_data(data)
                                print(f"New Product created in {ent_cate} successfully.")
                                break
                    break
            break

def delete_category(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
            ent_cate=input("Enter category name:").strip().lower()
            if not ent_cate:
                print("Enter a category name!!")
            elif ent_cate=="cancel":
                print("The task has been cancelled!")
                break
            elif ent_cate not in data:
                print(f"{ent_cate} category doesn`t exist!")
            else:
                del data[ent_cate]
                save_data(data)
                print(f"{ent_cate} category deleted successfully!")
                break
def delete_product(data):
    print("If you want to cancel this task, just enter (cancel) in any input line. ")
    while True:
        ent_cate=input("Enter category name:").strip().lower()
        if not ent_cate:
            print("Enter a category name!!")
        elif ent_cate=="cancel":
            print("The task has been cancelled!")
            break
        elif ent_cate not in data:
            print(f"{ent_cate} category doesn`t exist!")
        else:
            while True:
                ent_pro=input("Enter product name :").strip().lower()
                if not ent_pro:
                    print("Enter a Product name!!")
                elif ent_pro=="cancel":
                    print("The task has been cancelled!")
                    break
                elif ent_pro not in data[ent_cate]:
                    print(f"This product doesn`t exist in {ent_cate} category!")
                else:
                    del data[ent_cate][ent_pro]
                    save_data(data)
                    print("Product deleted successfully!")
                    break
            break

def menu():
    
    print("~"*25)
    print("WELCOME TO THE INVENTORY")
    print("~"*25)
    while True:
        print("1.See Whole Inventory.")
        print("2.See a category.")
        print("3.See a product.")
        print("4.Update inventory.")
        print("5.Create a new category.")
        print("6.Delete a category/product.")
        print("7.Create a new Product.")
        print("8.Exit.")
        choice=input("Enter your choice:").strip()
        try:
            with open("products.json","r") as file:
                    data=json.load(file)
            if choice=="":
                print("A Choice must be entered!")
            elif choice=="1":
                for key,value in data.items():
                    print(f"{key}-->{value}")
            elif choice=="2":
                see_category(data)
            elif choice=="3":
                see_product(data)
            elif choice=="4":
                update_products(data)
            elif choice=="5":
                add_category(data)
            elif choice=="6":
                while True:
                    print("If you want to cancel this task, just enter (cancel) in any input line. ")
                    print("1.Delete a category.")
                    print("2.Delete a product.")
                    choice2=input("Enter your choice:").strip().lower()
                    if choice2=="":
                        print("Enter a valid number from above as your choice!!")
                    elif choice2=="cancel":
                        print("This task has been cancelled!!")
                        break
                    elif choice2=="1":
                        delete_category(data)
                        break
                    elif choice2=="2":
                        delete_product(data)
                        break
                    else:
                        print("Enter a number!!")
            elif choice=="7":
                create_new_product(data)
            elif choice=="8":
                print("Thank you!")
                break
            else:
                print("Enter a valid choice!!")
        except FileNotFoundError:
            print("The Products file isn`t found!")
            break
        except (json.JSONDecodeError,UnicodeDecodeError):
            print("The Products file is Damaged!")
            break
menu()

