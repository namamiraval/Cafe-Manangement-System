#Project 2023-24

import mysql.connector
cnx=mysql.connector.connect(user='root',password='1307',host='localhost',database='project')
print("******************************CORNER HOUSE******************************")
print("                               SG Highway                               ")
print("                               Ahmedabad                                ")
print("\nHello, Welcome to Corner House!!")
print("\nPlease enter your details") 

cs = True
while cs == True:
    c=cnx.cursor()
    total=[]  
    L=[]
    tb=int(input("Enter your Table No: "))
    name=input("Enter your name: ")
    
    try:
        apple = True
        while apple == True:
            no=input("Enter your phone number: ")
            if len(no)==10:
                apple = False
                break
            if len(no)!='10':
                print("Enter 10 digit number")
                continue
                
    except ValueError:
        print("Invalid entry")

    def us():
        print("""Established back at a time when Bangalore was only trees and lakes, when bougainvillea and raintrees lined the streets, and everybody knew
        everybody, Corner House celebrates the spirit of old Bangalore. To this day, it remains steeped in that uniquely Bangalore feeling.
        Over the last (almost) four decades Corner House has seen birthdays, graduations, first dates, family get-togethers, and even a few engagements.
        Being a part of these memories has only proved that the purpose of the brand goes beyond just dessert.
        Nostalgia is a powerful emotion, and one closely associated with Corner House.
        We take pride in being truly Bangalorean.
        It is the simple moments, the easy interactions and the memories that make up our most essential values.
        Our purpose is to serve uncompromised, quality desserts consistently, and to take care of the people who make the business: our patrons and employees.
        In other words, customers get their money’s worth.
        The system followed at our outlets is self-service, but the company strives to take care of its customers in every way possible.
        Processes have been put in place to maintain consistency for every customer order.
        Employees at Corner House are a priority. Aside from the mandatory ESI, employees are provided additional private insurance to cover minor ailments that
        may not be within the purview of the ESI.
        Employees also benefit from good quality food provided for all three meals, as well as accommodation near the workplace.
        Through the months of the Covid-19 pandemic, employees have been given access to nutritional supplementation in the form of vitamins and medication to boost
        their immunity.""")

         
    def Menu():   
        '''c.execute("create table CornerHouse(No int(3) Not Null, Name varchar(20) Not Null, Quantity varchar(10), Price decimal(6,2) );")
        try:
            tup = ((1,"Cold Coffee","235ml",145),
                  (2,"Mocha","235ml",195),
                  (3,"Espresso","235ml",185),
                  (4,"Cold Brew","235ml",160),
                  (5,"Chocolate Thickshake","235ml",130),
                  (6,"Fries","",65),
                  (7,"Veg Burger","",45),
                  (8,"Cheese Chilli Burger","",79),
                  (9,"Vadapav","",40),
                  (10,"Dabeli","",40),
                  (11,"Pasta","250g",115),
                  (12,"Pizza","6 inch",200),
                  (13,"Vanilla Ice Cream","1 scoop",25),
                  (14,"Chocolate Ice Cream","1 scoop",30),
                  (15,"Brownie","1 Slice",85),
                  (16,"Cheesecake","1 Slice'",75))
            for t in tup:
                c.execute(f"insert into CornerHouse Values {t}")
                cnx.commit()

        except mysql.connector.errors.ProgrammingError:
            print("Error in pogramme")'''

        st="select * from CornerHouse;"
        c.execute(st)
        a = c.fetchall()

        print("\n")
        print("----------------MENU----------------")
        print("\n")
        
        for row in a:
            print("\n")
            print(row)

        mac = True
        while mac == True:
            
            n1=int(input("\nEnter Choice no: "))
            if n1 in range(1,17):
                 order=[]
                 amt=[]
                 if n1==1:
                    order.append("Cold Coffee")
                    quantity=int(input("How many glasses of Coffee would you like: "))
                    a=quantity*145
                    amt.append(a)

                 elif n1==2:
                    order.append("Mocha")
                    quantity=int(input("How many glasses of Mocha would you like: "))
                    a=quantity*195
                    amt.append(a)

                 elif n1==3:
                    order.append("Espresso")
                    quantity=int(input("How many glasses of Espresso would you like: "))
                    a=quantity*185
                    amt.append(a)

                 elif n1==4:
                    order.append("Cold Brew")
                    quantity=int(input("How many glasses of Cold Brew would you like: "))
                    a=quantity*160
                    amt.append(a)
                    
                 elif n1==5:
                    order.append("Chocolate Thickshake")
                    quantity=int(input("How many glasses of thickshake would you like: "))
                    a=quantity*130
                    amt.append(a)
                    
                 elif n1==6:
                    order.append("Fries")
                    quantity=int(input("How many packet of fries would you like: "))
                    a=quantity*65
                    amt.append(a)

                 elif n1==7:
                    order.append("Veg. Burger")
                    quantity=int(input("How many pieces of Burger would you like: "))
                    a=quantity*45
                    amt.append(a)

                 elif n1==8:
                    order.append("Cheese Chilli Burger")
                    quantity=int(input("How many pieces of Burger would you like: "))
                    a=quantity*79
                    amt.append(a)

                 elif n1==9:
                    order.append("Vadapav")
                    quantity=int(input("How many pieces of Vadapav would you like: "))
                    a=quantity*40
                    amt.append(a)

                 elif n1==10:
                    order.append("Dabeli")
                    quantity=int(input("How many pieces of Dabeli would you like: "))
                    a=quantity*40
                    amt.append(a)
                    
                 elif n1==11:
                    order.append("Pasta")
                    quantity=int(input("How many bowls of pasta would you like: "))
                    a=quantity*115
                    amt.append(a)
                    
                 elif n1==12:
                    order.append("Pizza")
                    quantity=int(input("How many Pizzas would you like: "))
                    a=quantity*200
                    amt.append(a)
                    
                 elif n1==13:
                    order.append("Vanilla Ice Cream Scoop")
                    quantity=int(input("How many scoops of ice cream would you like: "))
                    a=quantity*25
                    amt.append(a)
                    
                 elif n1==14:
                    order.append("Chocolate Ice Cream Scoop")
                    quantity=int(input("How many scoop of ice cream would you like: "))
                    a=quantity*30
                    amt.append(a)
                    
                 elif n1==15:
                    order.append("Brownie")
                    quantity=int(input("How many slices of brownie would you like: "))
                    a=quantiy*85
                    amt.append(a)
                    
                 elif n1==16:
                    order.append("Cheesecake")
                    quantity=int(input("How many slices of cheesecake would you like: "))
                    a=quantity*75
                    amt.append(a)
                    
                 else:
                    print("Please choose no between 1 to 16")
                    break

                 q=input("Do you wish to enter more food items (yes/no): ")
                 if q=='yes':
                     continue
                 elif q=='no' or q=='No' or q=='NO' or q=='nO':
                     mac = False
                     break
                 else:
                    print("Invalid Entry")
                
                 
        sum=0
        for i in amt:
            sum=sum+i
        print("\nTotal amount to be paid for Food: ",sum)
        total.append(sum)
                
        while n1==0 or n1>16:
            print("Sorry, Invalid Entry:")

          

    def merchandise():
        merchandise=[]
        mamt=[]
        hello = True
        while hello == True:
            print("\nFollowing are the options of our merchandise: ")
            print("1. Color-Changing Plastic Reusable Hot Cup with Pearl Lid - 16 fl oz -------> 250")
            print("2. Copper Pin Stainless-Steel Tumbler - 20 fl oz -------> 340")
            print("3. Drink-Thru Band Stainless-Steel Tumbler - 16 fl oz -------> 450")
            print("4. Recycled Plastic Tumbler - 16 fl oz -------> 390")
            print("5. Exit")
            mchoice=int(input("\nEnter Choise no: "))
            if mchoice in range(1,6):
                
                if mchoice==1:
                    merchandise.append("Color-Changing Plastic Reusable Hot Cup with Pearl Lid - 16 fl oz")
                    mquantity=int(input("How many would you like: "))
                    a=mquantity*250
                    mamt.append(a)
                elif mchoice==2:
                    merchandise.append("Copper Pin Stainless-Steel Tumbler - 20 fl oz")
                    mquantity=int(input("How many would you like: "))
                    a=mquantity*340
                    mamt.append(a)
                elif mchoice==3:
                    merchandise.append("Drink-Thru Band Stainless-Steel Tumbler - 16 fl oz")
                    mquantity=int(input("How many would you like: "))
                    a=mquantity*450
                    mamt.append(a)
                elif mchoice==4:
                    merchandise.append("Recycled Plastic Tumbler - 16 fl oz")
                    mquantity=int(input("How many would you like: "))
                    a=mquantity*390
                    mamt.append(a)
                elif mchoice==5:
                    hello = False
                    break               

            else:
                print("Please choose value between 1 to 5")

            q=input("Do you wish to enter more items (yes/no): ")
            if q=='yes':
                continue
            if q=='no':
                hello = False
                break

        msum=0
        for i in mamt:
            msum=msum+i
        print("\nTotal amount to be paid for Merchandise products: ",msum)
        total.append(msum)

    def pay():
        pay=input("Enter your mode of payment (CASH\CARD): ")
        if pay=="CASH":
            print("Mode of payment confirmed")
        elif pay=="CARD": 
            input("Enter Card type(Debit/Credit): ")
            input("Enter Bank name: ")
            input("Enter Card holder's name: ")
            print("Mode of payment confirmed")
        else:
            print("Invalid Entry, enter CASH/CARD in blockletters")
                    
    oppo = True
    while oppo == True:
        print("\n\nHow can we help you today?\n")
        print("1. Get to know us")
        print("2. Order Food")
        print("3. Buy our Merchandise Products")
        print("4. Payment Details")
        print("5. Exit")
        xyz=int(input("Enter Choice no: "))

        if xyz==1:
            us()
        elif xyz==2:
            Menu()
        elif xyz==3:
            merchandise()
        elif xyz==4:
            count=0
            for i in total:
                print(i,sep='+')
                count=count+i
            print("Total amount to be paid: ",count)
            pay()
        elif xyz==5:
            oppo = False
            cs=False
            break
            

'''
    c.execute("create table Details(Tableno varchar(5) Primary key, Name varchar(50) Primary key, Order varchar(50), Merchandise varchar(50), Total_cost varchar(20));")
    sql="insert into Details(tb,name,order,merchandise,total)values(%s,%s,%s,%s,%s);"
    val=(tb,name,order,merchandise,total)
    c.execute(sql,val)
    print("Record Inserted")


    display="select * from Details;"
    c.execute(display)
    ab = c.fetchall()

    
    print("\n")
    print("----------------Details----------------")
    print("\n")
        
    for rows in ab:
        print("\n")
        print(rows)
'''
cnx.cursor()
    
    
