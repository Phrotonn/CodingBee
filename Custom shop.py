import os,time,datetime,pytz

a = 0
b = ""
i = 1 #list "items" counter1
total = 0

data1 = datetime.datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%H;%M;%S")#time 

def Wait():
    print("Please press [Enter] to continue..")
    input("")
    os.system("cls")

def Open():
    global data1
    global total
    global payment
    while True:
        print(8*"=" + " Online Dungeon Shop " + 8*"=")
        print('''1. Shop
2. Exit''')
        1
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

        if a == 2:
            print("Farewell, adventurer.May the goddess bless upon your journey")
            break

        if a == 3:
            with open(data1 + ".txt","r") as x:
                report = x.read()
                os.system("cls")
                print(report)
                c = input("Are you ready to cash out? (Y/N) ")

            if c == "Y":
                d = input("Will you pay by cash or card? ")  

                if d == "cash":
                    total = 0
                    with open(data1 + ".txt", "r") as x:
                        lines = x.readlines()

                    for line in lines:
                        if "$" in line:
                            price = int(line.strip().split("$")[1])
                            total += price

                        else :
                            pass
                            # break
                    
                    print(f"Your total is : ${total}")
                    payment = int(input("Amount : "))
                    change = payment - total
                    print(f"Here is your change : ${change}")
                    print("Gratitude upon thee, noble patron, for thy treasured purchase. May fortune and enchantment follow wherever thy journey leads!")  
                    Wait()
                    break

                if d == "card":
                    print("Gratitude upon thee, noble patron, for thy treasured purchase. May fortune and enchantment follow wherever thy journey leads!")  
                    Wait()
                    break  

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
    print(8 * "=" + " Online Dungeon Shop " + 8 * "=")
    items =[
        ["Smoke of Deceit",50],
        ["Sentry Ward",50],
        ["Observer Ward",75],
        ["Dust of Appearance",80],
        ["Healing Salve",100],
        ["Quelling Blade",100],
        ["Gem of True Sight",900],
        ["Shadow Amulet",1000],
        ["Blink Dagger",2250],
        ["Moon Shard",4000]
    ]
    
    for item in items:
        print(f"{i}. {item[0]} ${item[1]}")
        i += 1
        if i >= 11:
            i = 1

    print(37 * "=")
    
    b = input("What relic shall aid you on your quest? ")

    if b == "":
        print("Sorry to disappoint you..")
        Wait()
        Open()

    elif b.isdigit() and 1 <= int(b) <= 10: #isdigit = to find out if input = int, if input = int then checks if input is 1 - 10
        selected_item = items[int(b) - 1] #to select item from list of "items"
        print(f"Ah, a fine choice! May this {selected_item} serve you well on your journey. Safe travels, adventurer.")
        Wait()    
        
        if not os.path.exists(data1 + ".txt"): #similar to if os.path.exists but this is the opposite, only write when data1.txt doesnt exist. If it exists then it doesnt do anything
            with open(data1 + ".txt","a") as x:
                x.write("Your selected item(s) : \n")
                
        with open(data1 + ".txt","a") as x:      
            x.write(f"{selected_item[0]} ${selected_item[1]}" "\n")

    else:
        print("Such relic does not exist in our inventory...")
        Wait()
        Open()
        
Open()

