import os,time,datetime,pytz

a = 0
b = ""
c = ""
d = ""
i = 1 #list "items" counter1
Items = " "
items = " "
failedpayment = 0 

data1 = datetime.datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%H;%M;%S")#time 

def Wait():
    print("Please press [Enter] to continue..")
    input("")
    os.system("cls")

def Checkout():
    global failedpayment
    payment = 0
    total = 0
    with open(data1 + ".txt", "r") as x:
        lines = x.readlines()

    for line in lines:
        if "$" in line:
            price = int(line.strip().split("$")[1])
            total += price
        else:
            continue

    if d == "cash":
        print(f"Your total is : ${total}")
        payment = int(input("Amount : "))
        if payment < total: 
            failedpayment += 1 
            print("Insufficient Gold!")
            if failedpayment == 3:
                print("Begone, begger! Return when your purse is worthy of my wares!")
                exit()
            Wait()
            Open()   

        change = payment - total
        print(f"Here is your change : ${change}")
        print("Gratitude upon thee, noble patron, for thy treasured purchase. May fortune and blessings follow wherever thy journey leads!") 
        Wait()
        exit()

    elif d == "card":
        print("Gratitude upon thee, noble patron, for thy treasured purchase. May fortune and blessings follow wherever thy journey leads!")  
        Wait()
        exit()

    else:
        print("Please choose between [cash/card]")
        Wait()
        Open()

def Open():
    global data1
    global c
    global d
    while True:
        print(8*"=" + " Online Dungeon Shop " + 8*"=")
        print('''1. Shop
2. Exit''')
        
        if os.path.exists(data1 + ".txt"):
            print("3. Report")
            print(37*"=")
            a = int(input("Welcome, brave adventurer, to my humble emporium!(1-3) "))

        else:
            print(37*"=")
            a = int(input("Welcome, brave adventurer, to my humble emporium!(1-2) "))
            
        if a == 1:
            Wait()
            Shop()

        elif a == 2:
            print("Farewell, adventurer.May the goddess bless upon your journey")
            break

        elif a == 3:
            with open(data1 + ".txt","r") as x:
                report = x.read()
                os.system("cls")
                print(report)
                c = input("Are you ready to cash out? (Y/N) ")

            if c == "Y":
                d = input("Will you pay by cash or card? ")
                Checkout()

            elif c == "N":
                Wait()
                Open()
                    
            else:
                print("Please input (Y/N) ")
                Wait()
                Open()

def Shop():
    global i
    global data1
    global Items

    print(8 * "=" + " Online Dungeon Shop " + 8 * "=")

    items = [] 
    with open("items.txt", "r") as file:
        for line in file:
            item, price = line.strip().split(",") #["item","price"]
            items.append([item, int(price)]) #insert items into list 

    for item in items:
        print(f"{i:2}. {item[0]:20} | ${item[1]}")
        i += 1
        if i >= 11:
            i = 1

    print(37 * "=")

    b = input("What relic shall aid you on your quest? ")

    if b == "":
        print("Sorry to disappoint you..")
        Wait()
        Open()

    elif b.isdigit() and 1 <= int(b) <= 10:
        selected_item = items[int(b) - 1]
        print(f"Ah, a fine choice! May this [{selected_item[0]}] serve you well on your journey. Safe travels, adventurer.")
        Wait()    

        if not os.path.exists(data1 + ".txt"):
            with open(data1 + ".txt", "a") as x:
                x.write("Your selected item(s) : \n")

        with open(data1 + ".txt", "a") as x:
            x.write(f"{selected_item[0]}  |  ${selected_item[1]}\n")

    else:
        print("Such relic does not exist in our inventory...")
        Wait()
        Open()

Open()



#Owner
    # Tambah Item
    # Update Item (Nama atau Harga)
    # Hapus Item
    # Lihat Item yang tersedia
# ATM
    # Tarik tunai
    # Cek Saldo
    # Setor Tunai
# User
    # Nama pelanggan
    # Cart 
    # Checkout
#CRUD = Create, Read, Update, Delete
