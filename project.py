import pandas as pd
import os
import bcrypt
import pickle
import getpass
import pytz
import datetime
from rich.console import Console
from rich.align import Align
import time
console = Console()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
timezone = (pytz.timezone('Asia/Kolkata'))
class Administration_Member:
    def __init__(self,name:str):
        self.name=name
    def add_to_menu(self,category:str,item_name:str,price:int)->bool:
        menu_dict={"category": [category],
                   "name":[item_name],
                   "price":[price]}
        try:
            df2=pd.DataFrame(menu_dict,index=None)
            if "menu.csv" in os.listdir():
                df1= pd.read_csv("menu.csv")
                item_index=df1.index[(df1["category"]==category) & (df1["name"]==item_name)].to_list()
                if item_index!=[]:
                    clear()
                    console.print(Align.center(f"[bold italic underline red]\nThe Item You Are Trying To Add Already Exists In The Menu[/]"))
                    console.print(Align.center(f"[bold italic underline blue]You Probably Need To The Update The Price,\nTo Do So Please Use The Update Price Function[/]"))
                    time.sleep(3)
                    
                    return False
                else:
                    if df1.empty:
                        mdf=df2
                    else:
                    
                        mdf=pd.concat([df1,df2])
                        mdf= mdf.drop_duplicates()
                    mdf.to_csv("menu.csv",index=False)            
            else:
                df2.to_csv("menu.csv",index=False)
            return True
        except Exception as e :
            print(e)
            return False    
    def remove_from_menu(self,category:str,item_name:str)->bool:
        try:
            if "menu.csv" not in os.listdir():
                console.print(Align.center("[bold italic underline red]Please First Add Something To The Menu[/]"))
                time.sleep(2)
                
                return False
            else:
                df1=pd.read_csv("menu.csv")
                if df1.empty:
                    clear()
                    console.print(Align.center("[bold italic underline red]\nPlease First Add Something To The Menu[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    item_index=df1.index[(df1["category"]==category) & (df1["name"]==item_name)].to_list()
                    if item_index==[]:
                        clear()
                        console.print(Align.center("[bold italic undeline red]\nThe Item You Are Trying To Remove Do Not Exist In The Menu[/]"))
                        time.sleep(2)
                        
                        return False
                    else:
                        df1=df1.drop(index=item_index[0])
                        df1.to_csv("menu.csv",index=False)
                        return True
        except Exception as e:
            print(e)
            return False            
    def update_price(self,category:str,item_name:str,new_price:int)->bool:
        try:
            if "menu.csv" not in os.listdir():
                console.print(Align.center("[bold italic underline red]Please First Add Something To The Menu[/]"))
                time.sleep(2)
                return False
            else:
                df1=pd.read_csv("menu.csv")
                if df1.empty:
                    console.print(Align.center("[bold italic underline red]Please First Add Something To The Menu[/]"))
                    
                    return False
                else:
                    item_index=df1.index[(df1["category"]==category) & (df1["name"]==item_name)].to_list()
                    if item_index==[]:
                        clear()
                        console.print(Align.center("[bold italic underline red]\nThe Item Whose Price You Are Trying To Update Do Not Exist In Menu[/]"))
                        time.sleep(2)
                        
                        return False
                    else:
                        df1.loc[item_index,"price"]=new_price
                        df1.to_csv("menu.csv",index=False)
                        return True
        except Exception as e:
            print(e)
            return False            
    def add_new_coupon(self,coupon_name:str,discount:int)->bool:
        coupon_dict={"coupon name":[coupon_name],
                     "discount":[discount]}
        try:
            df2=pd.DataFrame(coupon_dict,index=None)
            if "discount.csv" in os.listdir():
                df1= pd.read_csv("discount.csv")
                item_index=df1.index[(df1["coupon name"]==coupon_name) & (df1["discount"]==discount)].to_list()
                if item_index!=[]:
                    clear()
                    console.print(Align.center(f"[bold italic underline red]\nThe Coupon You Are Trying To Add Already Exists.[/]"))
                    time.sleep(3)
                    
                    return False
                else:
                    if df1.empty:
                        mdf=df2
                    else:
                    
                        mdf=pd.concat([df1.df2])
                        mdf=mdf.drop_duplicates()
                    mdf.to_csv("discount.csv",index=False)            
            else:
                df2.to_csv("discount.csv",index=False)
            return True
        except Exception as e :
            print(e)
            return False
    def remove_coupon(self,coupon_name:str)->bool:
        try:
            if "discount.csv" not in os.listdir():
                console.print(Align.center("[bold italic underline red]Please First Add Any Coupon To Remove It[/]"))
                time.sleep(2)
                
                return False
            else:
                df1=pd.read_csv("discount.csv")
                if df1.empty:
                    clear()
                    console.print(Align.center("[bold italic underline red]\nPlease First Add Any Coupon To Remove It[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    item_index=df1.index[(df1["coupon name"]==coupon_name)].to_list()
                    if item_index==[]:
                        clear()
                        console.print(Align.center("[bold italic undeline red]\nThe Coupon You Are Trying To Remove Do Not Exist[/]"))
                        time.sleep(2)
                        
                        return False
                    else:
                        df1=df1.drop(index=item_index[0])
                        df1.to_csv("discount.csv",index=False)
                        return True
        except Exception as e:
            print(e)
            return False
    def check_menu(self)->bool:
        try:            
            if "menu.csv" in os.listdir():
                df1= pd.read_csv("menu.csv")
                if df1.empty:
                    console.print(Align.center(f"[bold italic underline red]Please First Add Something To Menu To Check.[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    console.print(Align.center(f"[bold italic underline magenta]{df1}[/]"))             
                    return True
            else:
                console.print(Align.center(f"[bold italic underline red]Please First Add Something To Menu To Check.[/]"))
                time.sleep(2)
                return False
        except Exception as e :
            print(e)
            return False
    def check_reviews(self)->bool:
        try:            
            if "reviews.csv" in os.listdir():
                df1= pd.read_csv("reviews.csv")
                if df1.empty:
                    console.print(Align.center(f"[bold italic underline red]No Reviews To Show[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    console.print(Align.center(f"[bold italic underline magenta]{df1}[/]"))             
                    return True
            else:
                console.print(Align.center(f"[bold italic underline red]No Reviews To Show[/]"))
                time.sleep(2)
                return False
        except Exception as e :
            print(e)
            return False
    def check_coupons(self)->bool:
        try:            
            if "discount.csv" in os.listdir():
                df1= pd.read_csv("discount.csv")

                if df1.empty:
                    console.print(Align.center(f"[bold italic underline red]No Discount Coupons To Show[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    console.print(Align.center(f"[bold italic underline magenta]{df1}[/]"))             
                    return True
            else:
                console.print(Align.center(f"[bold italic underline red]No Discount Coupons To Show[/]"))
                time.sleep(2)
                return False
        except Exception as e :
            print(e)
            return False
    def check_sales(self)->bool:
        try:            
            if "sales.csv" in os.listdir():
                df1= pd.read_csv("sales.csv")
                if df1.empty:
                    console.print(Align.center(f"[bold italic underline red]No Sales To Show[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    console.print(Align.center(f"[bold italic underline magenta]{df1}[/]"))             
                    return True
            else:
                console.print(Align.center(f"[bold italic underline red]No Sales To Show[/]"))
                time.sleep(2)
                return False
        except Exception as e :
            print(e)
            return False

class Customer:
    def __init__(self,name:str,phone_number:int):
        self.name=name
        self.phone_number=phone_number
    def place_order(self)->bool:
        try:
            clear()
            bill={"item name":[],
                    "quantity":[],
                    "price":[]}
            
            
            df1=pd.read_csv("menu.csv")
            index_list=df1.index.to_list()
            if df1.empty:
                console.print(Align.center(f"[bold italic underline red]\nOh Oh!!!\n No Items In The Menu To Order[/]"))
                time.sleep(2)
                
                return False
            else:                        
                while True:
                    
                    if self.check_menu():
                        item_index_cond=False
                        while item_index_cond==False:                                    
                            console.print(Align.center(f"[bold italic underline blue]\nEnter Item's Index Number To Order[/]"))
                            print("\033[34m")
                            item_index=console.input("[bold italic underline blue]")
                            if item_index.isdigit() :
                                item_index=int(item_index)
                                if item_index in index_list:
                                    item_index_cond=True
                                    break
                            clear()
                            console.print(Align.center("[bold italic underline red]\nOh Oh !!! \nLooks Like You Entered An Invalid [/]"))
                            console.print(Align.center("[bold italic underline red]Please Try Entering The Exact Index Number From The Menu.[/]"))
                        item_quantity_cond=False
                        while item_quantity_cond==False:                                    
                            console.print(Align.center(f"[bold italic underline blue]\nEnter Item's Quantity To Order[/]"))
                            print("\033[34m")
                            quantity=console.input("[bold italic underline blue]")
                            if quantity.isdigit() :
                                quantity=int(quantity)
                                if quantity>0:
                                    item_quantity_cond=True
                                    
                                    break
                            clear()
                            
                            console.print(Align.center("[bold italic underline red]\nOh Oh !!! \nLooks Like You Entered An Invalid [/]"))
                            console.print(Align.center("[bold italic underline red]Please Try Entering The Exact Quantity Number To Order[/]"))
                        price=(df1["price"][item_index])*quantity
                        bill["item name"].append(df1["name"][item_index])
                        bill["price"].append(price)
                        bill["quantity"].append(quantity)

                        
                        clear()
                        console.print(Align.center(f"[bold italic underline green]\nYou Successfully Placed Order Of [bold italic underline green]{quantity} Quantity Of {df1['name'][item_index]} In The Cart[/]"))
                        print("\033[34m")
                        order_complete_cond=console.input(Align.center("[bold italic underline blue]\nPlease Enter 'Q' To End Adding Items To Cart And Place Order. [/]"))
                        print("\033[0m")
                        if order_complete_cond.lower()=="q":
                            print("\033[34m")
                            discount_coupon=console.input(Align.center("[bold italic underline blue]\nPlease Enter The Discount Coupon To Apply.\n(If Any, Else Press Enter) [/]"))
                            print("\033[0m")
                            try:
                                if "discount.csv" not in os.listdir():
                                    clear()
                                    console.print(Align.center("[bold italic underline red]\n\nOh Oh!!\nLooks Like There Are No Active Discount Coupons For Now.[/]"))
                                    time.sleep(2)                                    
                                else:
                                    df1=pd.read_csv("discount.csv")
                                    if df1.empty:
                                        clear()
                                        console.print(Align.center("[bold italic underline red]\n\nOh Oh!!\nLooks Like There Are No Active Discount Coupons For Now.[/]"))
                                        time.sleep(2)
                                    else:
                                        if discount_coupon!="":
                                            item_index=df1.index[(df1["coupon name"]==discount_coupon)].to_list()
                                            if item_index==[]:
                                                clear()
                                                console.print(Align.center("[bold italic undeline red]\nThe Coupon You Are Trying To Use Do Not Exist[/]"))
                                                time.sleep(2)
                                            else:
                                                discount=df1["discount"][item_index[0]]
                                                clear()
                                                console.print(Align.center("[bold italic undeline green]\nThe Coupon Is Successfully Availed.[/]"))
                                                time.sleep(2)
                                        else:
                                            discount=0
                            except Exception as e:
                                print(e)
                                

                            current_time=datetime.datetime.now(timezone)
                            formatted_time=current_time.strftime("%d-%m-%y -->%H:%M:%S[/]")
                            bill_df=pd.DataFrame(bill)
                            total_price=sum((bill["price"]))
                            discounted_price=total_price*(1-(discount/100))
                            complete_bill={"customer name":[customer.name], 
                        "contact number":[customer.phone_number], "order":[bill],                    "total amount":[total_price],"discounted amount":discounted_price,"time":[formatted_time]}
                            # print("test1")
                            sales_df=pd.DataFrame(complete_bill)
                            
                            if "sales.csv" in os.listdir():
                                all_sales_df=pd.read_csv("sales.csv")
                                if all_sales_df.empty:
                                    mdf=sales_df
                                else:
                                
                                   mdf=pd.concat([all_sales_df,sales_df])
                               
                                mdf.to_csv("sales.csv",index=False)
                            else:
                                sales_df.to_csv("sales.csv",index=False)

                            clear()
                            console.print(Align.center(f"[bold italic underline blue]\n Your BIll:\n[/]"))
                            console.print(Align.center(f"[bold italic underline blue] Name:{customer.name}\n[/]"))
                            console.print(Align.center(f"[bold italic underline blue] Contact Number:{customer.phone_number}\n[/]"))
                            console.print(Align.center(f"[bold italic underline magenta]{bill_df}\n[/]"))
                            console.print(Align.center(f"[bold italic underline blue] Your Total Bill Amount Is:{discounted_price}\n[/]"))

                            stop_cond=console.input(Align.center("[bold italic underline cyan]Press Enter To Continue.[/]"))
                            return True
                          
                    else:
                            clear()
                            console.print(Align.center("[bold italic underline red]\nOh Oh !!!\n We Are Facing Some Troubles In Displaying The Menu For Now \nPlease Try Again Later.[/]"))
                            
                            time.sleep(2)
                            
                            return False
                            

        except Exception as e:
            print(e)
            return False
    def check_menu(self)->bool:
        try:            
            if "menu.csv" in os.listdir():
                df1= pd.read_csv("menu.csv")
                if df1.empty:
                    console.print(Align.center(f"[bold italic underline red]Please Wait For Manager To Put Some Items On The Menu[/]"))
                    time.sleep(2)
                    
                    return False
                else:
                    console.print(Align.center(f"[bold italic underline magenta]{df1}[/]"))             
                    return True
            else:
                console.print(Align.center(f"[bold italic underline red]Please Wait For Manager To Put Some Items On The Menu[/]"))
                time.sleep(2)
                return False
        except Exception as e :
            print(e)
            return False
    def write_review(self,review:str,time:str)->bool:
        review_dict={"name": [self.name],
                   "contact number":[self.phone_number],
                   "review":[review],
                   "time":[time]}
        try:
            df2=pd.DataFrame(review_dict,index=None)
            if "reviews.csv" in os.listdir():
                df1= pd.read_csv("reviews.csv")
                if df1.empty:
                    mdf=df2
                else:
                    mdf=pd.concat([df1,df2])
                    mdf=mdf.drop_duplicates()
                mdf.to_csv("reviews.csv",index=False)            
            else:
                df2.to_csv("reviews.csv",index=False)
            return True
        except Exception as e :
            print(e)
            return False  
clear()
console.print("\n\n\n\n")
console.print(Align.center(f"[bold italic underline green]*** This Digital Cafe Was Designed And Developed By --Shaurya Garg ***[/]"))
time.sleep(1)
while True:
        files=os.listdir()
        if ("admin.pkl" not in files) and any(("menu.csv" in files,"sales.csv" in files,"reviews.csv" in files,"discount.csv" in files,"sales.csv" in files)):
            clear()
            console.print("\n\n\n\n")
            console.print(Align.center(f"[bold italic underline red]Security Breach Detected\nSystem Is Turning Off\nPlease Contact The Developers Immidiately[/]"))
            break
        clear()
        console.print("\n\n\n\n")
        console.print(Align.center(f"[bold italic underline cyan]***  Welcome To The Royal Cafe  ***[/]"))
        time.sleep(1)
        user_cond=False
        clear()
        console.print("\n\n\n\n")
        while user_cond==False:
            console.print(Align.center(f"[bold italic underline magenta]Please Choose From The Following Options\n\n[/]"))
            console.print(Align.center(f"[bold italic underline cyan]1) Administration Member\n2)Customer\n3)Exit\n\n-->[/]"))
            print("\033[1;3;36m")
            user=console.input("[bold italic underline cyan]")
            print("\033[0m")
            if user.isdigit():
                user=int(user)
                if any((user ==1,user==2,user==3)):
                    user_cond=True
            if user_cond==True:
                break
            clear()
            console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
            console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
            console.print(Align.center("[bold italic underline red]Please Try Entering The Option Number Only .[/]"))
            console.print("\n")
        clear()
        console.print("\n\n")    
        if user==1:
            admin_cond=False
            if "admin.pkl" in os.listdir():
                log_cond=False
                while log_cond==False:
                    console.print(Align.center(f"[bold italic underline blue]\nPlease Enter Your Name\n-->[/]"))
                    print("\033[1;3;34m")
                    administrator_name=console.input("[bold italic underline cyan]")
                    
                    console.print(Align.center(f"[bold italic underline blue]Please Enter Your Logging In Password\n-->[/]"))
                    print("\033[1;3;34m")
                    administrative_password=getpass.getpass(prompt="",echo_char="*")
                    
                    with open("admin.pkl","rb") as admin_file:
                        
                        log_detail=pickle.load(admin_file)
                        
                        
                        if bcrypt.checkpw(administrator_name.encode("utf-8"),log_detail["Admin Name"])  and  bcrypt.checkpw(administrative_password.encode("utf-8"),log_detail["Administrative Password"]) :
                            admin_cond=True
                            log_cond=True
                            break
                    clear()
                    console.print(Align.center(f"[bold italic underline red]\nOh Oh !!! Looks Like You Entered Wrong Logging In Details.[/]"))
                    console.print(Align.center(f"[bold italic underline red]Please Enter 'q' To stop Administrative Options\n(Else press Enter To Continue To Try Logging In Again.) \n-->[/]"))
                    print("\033[1;3;34m")
                    stop=console.input()
                    if stop.lower()=="q":
                        break
            else:
                console.print(Align.center(f"[bold italic underline blue]Please Enter Your Name\n-->[/]"))
                print("\033[1;3;34m")
                administrator_name=console.input("[bold italic underline cyan]")
                password_cond=False
                while password_cond==False:
                    console.print("\n")
                    console.print(Align.center(f"[bold italic underline blue]Please Enter Your Signing In Password\n-->[/]"))
                    print("\033[1;3;34m")
                    administrative_password=getpass.getpass(prompt="",echo_char="*")
                    have_digit=False
                    have_lower=False
                    have_upper=False
                    have_length=False
                    have_special_char=False
                    for character in administrative_password:
                        if character.isdigit():
                            have_digit=True
                        if character.isupper():
                            have_upper=True
                        if character.islower():
                            have_lower=True
                        if character in "@#$~*?><|":
                            have_special_char=True
                        if len(administrative_password)>=8:
                            have_length=True
                    password_cond=all((have_digit,have_lower,have_upper,have_length,have_special_char))
                    if password_cond==True: 
                        hashed_name=bcrypt.hashpw(administrator_name.encode("utf-8"),bcrypt.gensalt())
                        hashed_password=bcrypt.hashpw(administrative_password.encode("utf-8"),bcrypt.gensalt())

                        with open("admin.pkl","wb") as admin_file:
                            pickle.dump({"Admin Name":hashed_name,"Administrative Password":hashed_password},admin_file)
                        admin_cond=True
                        break
                    
                    clear()
                    console.print("\n")
                    console.print(Align.center("[bold italic underline red]\nOops!!!\nThe Password Do Not Fullfill The Minimum Security Requirements:\n~Should Have Atleast 8 Character Length\n~Should Have Atleast An UpperCase Letter\n~Should Have Atleast A LowerCase Letter\n~Should Have Atleast A Digit\n~Should Have Atleast A Special CHaracter(@#$~*?><|)[/]"))
                    
            while admin_cond==True:
                clear()
                administrator=Administration_Member(administrator_name)
                administrator_option_cond=False
                while administrator_option_cond==False:
                    console.print(Align.center(f"[bold italic underline blue]\nPlease Choose From The Following Options\n[/]"))
                    console.print(Align.center(f"[bold italic underline cyan]1) Add New Item To The Menu\n2) Remove Item From The Menu \n3) Update Price Of An Item In Menu\n4) Add Discount Coupon\n5) Remove Discount Coupon\n6) Check Menu\n7) Check Discount Coupons\n8) Check Sales\n9) Check Reviews\n10) Exit\n\n-->[/]"))
                    administrator_option_cond=False
                    print("\033[1;3;36m")
                    administrator_option=console.input("[bold italic underline cyan]")
                    print("\033[0m")
                    if administrator_option.isdigit():
                        administrator_option=int(administrator_option)
                        if administrator_option in range(1,11):
                            administrator_option_cond=True
                            
                            break                
                    clear()
                    console.print("\n")
                    console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
                    console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
                if administrator_option_cond==True:
                    if administrator_option==1:
                        clear()
                        while True :
                            clear()
                            category_option_cond=False
                            while category_option_cond==False:
                                console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Category Of Item:\n1)Snacks\n2)Beverages\n3)Desserts\n4)Exit\n-->[/]"))
                                print("\033[1;3;34m")
                                category_option=console.input("[bold italic underline blue]")
                                print("\033[0m")
                                if category_option.isdigit():
                                    category_option=int(category_option)
                                    if any(((category_option)==1,(category_option)==2,(category_option)==3,(category_option)==4)):
                                        category_option_cond=True
                                        break
                            
                                clear()
                                console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
                                console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
                                
                            if category_option_cond==True:
                                clear()
                                if (category_option)==4:
                                    break
                                else:
                                    console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Item Name\n-->[/]"))
                                    print("\033[1;3;34m")
                                    item_name=console.input("[bold italic underline blue]")
                                    print("\033[0m")
                                    item_price_digit_cond=False
                                    while item_price_digit_cond==False:
                                         console.print(Align.center(f"[bold italic underline blue]Please Enter The Item's Price\n-->[/]"))
                                         print("\033[1;3;34m")
                                         item_price=console.input("[bold italic underline blue]")
                                         print("\033[0m")
                                         if item_price.isdigit() :
                                            item_price=int(item_price)
                                            if ((item_price)>0):
                                                
                                                item_price_digit_cond=True
                                                break
                                         clear()
                                         console.print(Align.center(f"[bold italic underline red]\nOh Oh!!!\n You Entered An Invalid Price Amount\n(Try ENtering Digits Only)[/]"))
                                    category="Snacks" if (category_option)==1 else "Beverages" if (category_option)==2 else "Desserts"
                                    if (administrator.add_to_menu(category,item_name,item_price)):
                                        clear()
                                        console.print(Align.center(f"[bold italic green]\nThe Item:{item_name} Was Succesfully Added To Menu[/]"))
                                        console.print(Align.center(f"[bold italic green]You Can Add More Items[/]"))
                                        time.sleep(2)
                                        

                                    else:
                                        clear()
                                        console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty Adding The Item To The Menu\nPlease Try Again Later.[/]")) 
                                        time.sleep(2)    
                    elif administrator_option==2:
                        clear()
                        while True :
                            clear()
                            category_option_cond=False
                            while category_option_cond==False:
                                console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Category Of Item:\n1)Snacks\n2)Beverages\n3)Desserts\n4)Exit\n-->[/]"))
                                print("\033[1;3;34m")
                                category_option=console.input("[bold italic underline blue]")
                                print("\033[0m")
                            
                                if category_option.isdigit():
                                    category_option=int(category_option)
                                    if any(((category_option)==1,(category_option)==2,(category_option)==3,(category_option)==4)):
                                        category_option_cond=True
                                        break
                            
                                clear()
                                console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
                                console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
                                
                            if category_option_cond==True:
                                clear()
                                if category_option==4:
                                    break
                                else:
                                    console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Item Name\n-->[/]"))
                                    print("\033[1;3;34m")
                                    item_name=console.input("[bold italic underline blue]")
                                    print("\033[0m")
                                    category="Snacks" if category_option==1 else "Beverages" if category_option==2 else "Desserts"
                                    if (administrator.remove_from_menu(category,item_name)):
                                        clear()
                                        console.print(Align.center(f"[bold italic green]\nThe Item:{item_name} Was Succesfully Removed From The Menu[/]"))
                                        time.sleep(2)
                                        

                                    else:
                                        clear()
                                        console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty Removing The Item From The Menu\nPlease Try Again Later.[/]"))
                                        time.sleep(2)
                    elif administrator_option==3:
                        clear()
                        while True :
                            clear()
                            category_option_cond=False
                            while category_option_cond==False:
                                console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Category Of Item:\n1)Snacks\n2)Beverages\n3)Desserts\n4)Exit\n-->[/]"))
                                print("\033[1;3;34m")
                                category_option=console.input("[bold italic underline blue]")
                                print("\033[0m")
                            
                                if category_option.isdigit():
                                    category_option=int(category_option)
                                    if any(((category_option)==1,(category_option)==2,(category_option)==3,(category_option)==4)):
                                        category_option_cond=True
                                        break
                            
                                clear()
                                console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
                                console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
                                
                            if category_option_cond==True:
                                clear()
                                if category_option==4:
                                    break
                                else:
                                    console.print(Align.center(f"[bold italic underline blue]\nPlease Enter The Item Name\n-->[/]"))
                                    print("\033[1;3;34m")
                                    item_name=console.input("[bold italic underline blue]")
                                    print("\033[0m")
                                    item_price_digit_cond=False
                                    while item_price_digit_cond==False:
                                         console.print(Align.center(f"[bold italic underline blue]Please Enter The Item's New Price\n-->[/]"))
                                         print("\033[1;3;34m")
                                         new_price=console.input("[bold italic underline blue]")
                                         print("\033[0m")
                                         if new_price.isdigit() :
                                             new_price=int(new_price)
                                             if (int(new_price) >0):
                                                item_price_digit_cond=True
                                                break
                                         clear()
                                         console.print(Align.center(f"[bold italic underline red]\nOh Oh!!!\n You Entered An Invalid Price Amount\n(Try ENtering Digits Only)[/]"))
                                    category="Snacks" if category_option==1 else "Beverages" if category_option==2 else "Desserts"
                                    if (administrator.update_price(category,item_name,int(new_price))):
                                        clear()
                                        console.print(Align.center(f"[bold italic green]\nThe Item:{item_name}'s Price Was Succesfully Updated In The Menu[/]"))
                                        
                                        time.sleep(2)
                                        

                                    else:
                                        clear()
                                        console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty Updating The Item's In The Menu\nPlease Try Again Later.[/]"))
                                        time.sleep(2)
                    elif administrator_option==4:
                        clear()
                        console.print(Align.center(f"[bold italic underline cyan]\nPlease Enter Name Of The New Discount Coupon\n-->[/]"))
                        print("\033[1;3;36m")
                        discount_coupon=console.input("[bold italic underline cyan]")
                        print("\033[0m")
                        discount_digit_cond=False
                        while discount_digit_cond==False:
                            console.print(Align.center(f"[bold italic underline cyan] Please Enter The Discount Percentage Of The New Discount Coupon\n-->[/]"))
                            print("\033[1;3;36m")
                            discount_percent=console.input("[bold italic underline cyan]")
                            print("\033[0m")
                            if discount_percent.isdigit() and (int(discount_percent)>0):
                                discount_digit_cond=True
                                break
                            clear()
                            console.print(Align.center(f"[bold italic underline red]\nOh Oh!!!\n You Entered An Invalid Price Amount\n(Try ENtering Digits Only)[/]"))
                        if administrator.add_new_coupon(discount_coupon,int(discount_percent)):
                            clear() 
                            console.print(Align.center(f"[bold italic underline green]\nNew Discount Coupon :{discount_coupon} Was Successfully Added[/]"))
                            time.sleep(2)
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty Adding The Discount Coupon\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif administrator_option==5:
                        clear()
                        console.print(Align.center(f"[bold italic underline cyan]\nPlease Enter Name Of The Discount Coupon To Be Removed\n-->[/]"))
                        print("\033[1;3;36m")
                        discount_coupon=console.input("[bold italic underline cyan]")
                        print("\033[0m")
                        if administrator.remove_coupon(discount_coupon):
                            clear() 
                            console.print(Align.center(f"[bold italic underline green]\nDiscount Coupon:{discount_coupon} Was Successfully Removed[/]"))
                            time.sleep(2)
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty Removing The Discount Coupon\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif administrator_option==6:
                        clear()
                        if administrator.check_menu():
                            
                            console.print(Align.center(f"[bold italic underline green]\nPlease Press Enter To Continue[/]"))
                            stop_cond=console.input()
                            
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty To Display The Menu\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif administrator_option==7:
                        clear()
                        if administrator.check_coupons():
                            
                            console.print(Align.center(f"[bold italic underline green]\nPlease Press Enter To Continue[/]"))
                            stop_cond=console.input()
                            
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty To Display The Discount Coupons Details.\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif administrator_option==8:
                        clear()
                        if administrator.check_sales():
                            
                            console.print(Align.center(f"[bold italic underline green]\nPlease Press Enter To Continue[/]"))
                            stop_cond=console.input()
                            
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty To Display The Sales Details\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif administrator_option==9:
                        clear()
                        if administrator.check_reviews():
                            
                            console.print(Align.center(f"[bold italic underline green]\nPlease Press Enter To Continue[/]"))
                            stop_cond=console.input()
                            
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty To Display The Reviews\nPlease Try Again Later.[/]"))
                            time.sleep(2)                    
                    elif administrator_option==10:
                        clear()
                        console.print("\n\n\n")
                        console.print(Align.center(f"[bold italic underline magenta]**  BYE BYE !!!  **\n\n[/]"))
                        time.sleep(3)
                        break

        elif user==2:
            console.print(Align.center(f"[bold italic underline magenta]** Customer Is King!!! **\n\n[/]"))
            if any(("admin.pkl" not in os.listdir(),"menu.csv" not in os.listdir())):
                clear()
                console.print("\n\n\n")
                console.print(Align.center(f"[bold italic underline red]Oh Oh!!![/]"))
                console.print(Align.center(f"[bold italic underline blue]We Love Early Customers But Unfortunately You Are Earlier Than The Manager Itself[/]"))
                console.print(Align.center(f"[bold italic underline blue]Please Wait A Little For Our Manager To Sign In And Add Items To The Menu[/]"))
            else:
                customer_option_cond=False
                while customer_option_cond==False:
                    console.print(Align.center(f"[bold italic underline blue]Please Choose From The Following Options\n[/]"))
                    console.print(Align.center(f"[bold italic underline cyan]1) Check Items In The Menu\n2) Place Order Of Your Yummy Cravings\n3) Write Us A Review For Future Improvements\n4)Exit\n\n-->[/]"))
                    
                    print("\033[1;3;36m")
                    customer_option=console.input("[bold italic underline cyan]")
                    print("\033[0m")
                    if customer_option.isdigit():
                        customer_option=int(customer_option)
                        if any((customer_option==1 , customer_option==2 , customer_option==3 ,customer_option==4)):
                            customer_option_cond=True
                            break
                    clear()
                    console.print(Align.center("[bold italic underline red]\nOh Oh![/]"))
                    console.print(Align.center("[bold italic underline red]Looks Like You Entered An Invalid Option[/]"))
                    
                if customer_option_cond==True:
                    clear()
                    console.print("\n\n")
                    console.print(Align.center("[bold italic underline cyan]Please Enter Your Name:[/]"))
                    print("\033[34m")
                    customer_name=console.input("[bold italic underline cyan]")
                    print("\033[0m")
                    clear()
                    phone_number_cond=False
                    while phone_number_cond==False:
                        console.print(Align.center("[bold italic underline cyan]\nPlease Enter Your Contact Number:[/]"))
                        print("\033[34m")
                        phone_number=console.input("[bold italic underline cyan]")
                        if phone_number.isdigit() and len(phone_number)==10:
                            print("\033[0m")
                            phone_number=int(phone_number)
                            phone_number_cond=True
                            break
                        clear()
                        console.print("\n\n")
                        console.print(Align.center("[bold italic underline red]Oh Oh!!!\nLooks Like There Is Some Problem With Your Entered Number\nPlease Enter Your Phone Number Without Country Code.\n[/]"))
                    customer=Customer(customer_name,phone_number)
                    if customer_option==1:
                        clear()
                        if customer.check_menu():                            
                            console.print(Align.center(f"[bold italic underline green]\nPlease Press Enter To Continue[/]"))
                            stop_cond=console.input()                                               
                        else:
                            clear()
                            console.print(Align.center(f"[bold italic red]\nOh Oh !\nLooks Like We Encountered Some Difficulty To Display The Menu\nPlease Try Again Later.[/]"))
                            time.sleep(2)
                    elif customer_option==2:
                        if customer.place_order():
                            clear()
                            console.print(Align.center("[bold italic underline magenta]\n\n We Would Be Happy To See You Here Again.[/]"))
                            console.print(Align.center("[bold italic underline magenta]BYE BYE !!!.[/]"))
                            time.sleep(3)
                        else:
                            clear()
                            console.print(Align.center("[bold italic underline red]\nWe Are Extremely Sorry For The Inconvenience Caused From Our Side.[/]"))

                            time.sleep(2)
                    elif customer_option==3:
                        clear()
                        console.print("\n\n")
                        console.print(Align.center("[bold italic underline cyan]Please Write The Review\n(Do Not Press Enter Till You Complete)[/]"))
                        print("\033[35m")
                        review=console.input("[bold italic underline magenta]")
                        current_time=datetime.datetime.now(timezone)
                        formatted_time=current_time.strftime("%d-%m-%y -->%H:%M:%S")
                        if customer.write_review(review,formatted_time):
                            clear()
                            console.print(Align.center("[bold italic underline green]\nThanks For Writing Us The Review.\n We Will Surely Work On Your Recommendations.[/]"))
                            time.sleep(3)
                        else:
                            console.print(Align.center("[bold italic underline red]Oops!! We Are Really Sorry We Could Not Record Your Review At The Time .[/]"))
                            console.print(Align.center("[bold italic underline blue]It would Be Really Good Of You If You Could Write It Again To Us After Sometime.[/]"))
                            
                            time.sleep(4)                        
                    elif customer_option==4:
                        clear()
                        console.print("\n\n\n")
                        console.print(Align.center(f"[bold italic underline magenta]**  BYE BYE !!!  **\n\n[/]"))
                        time.sleep(3)
                        break

            time.sleep(5)
        elif user==3:
            clear()
            console.print("\n\n\n")
            console.print(Align.center(f"[bold italic underline magenta]**  BYE BYE !!!  **\n\n[/]"))
            break
        
