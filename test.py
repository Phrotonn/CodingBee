import os
import time
from datetime import datetime

def Wait():
  print("Please wait...")
  time.sleep(1)
  os.system("cls")

class Chatbot():
  def __init__(self,name,):
    self.name = name

  def reply(self,respond):
    if respond.lower() == "hi":
      return "Hello!"
    elif respond.lower() == "how are you doing?":
      return "I'm fine, thank you"
    else :
      return "I don't understand..."
    
def Start():
  global name
  print("Hello, Welcome to ProtonChat! This is a basic Chatbot!")
  name = input("Please Enter Your Name Before Chatting : ")
  print(f"Welcome {name}! I hope you'll have an amazing time here!")
  Wait()
  Selection()
    
def Selection():
  print('''1. View Chat History
2. New Chat''')
  action = int(input("What would you like to do? "))

  if action == 1:
    print("test")

  elif action == 2:  
    Wait()
    Chat()

  else : 
     print("Invalid Selection, Please pick 1-2")
     Wait()
     Selection()

def Chat():
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") #so the file will be different
    filename = f"chathistory_{time}.txt"
    with open(filename, "w") as chat_history: #create file chathistory
        chat_history.write(f"Chat History_{time} :\n")

    print("Input Exit to leave chatroom")
    while True:
        User_text = input(f"{name} : ")
        if User_text.lower() == "exit":
            print(f"{bot.name} : Goodbye {name}! Glad to meet you! ")
            break

        respond = bot.reply(User_text)
        print(f"{bot.name} : {respond}")

        Chattime = datetime.now().strftime("%H:%M:%S") #so that it will have [time] Username format
        with open(filename, "a") as chat_history: 
            chat_history.write(f"[{Chattime}] {name} : {User_text}\n")
            chat_history.write(f"[{Chattime}] {bot.name} : {respond}\n")

bot = Chatbot("ProtonAI")
Wait()
Start()