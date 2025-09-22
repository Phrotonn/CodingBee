import os
import time

def Wait():
  print("Please wait...")
  time.sleep(1)
  os.system("cls")

def Enter():
  print("Please press [Enter] to continue")
  input("")
  os.system("cls")

class Status:
  def __init__(self, name, hp, damage, armor):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.armor = armor

class Player(Status):
  def __init__(self, name, hp, damage, armor, stamina, mana, critical, level):
    super().__init__(name, hp, damage, armor)
    self.stamina = stamina
    self.mana = mana
    self.critical = critical
    self.level = level

class Creep(Status):
  def __init__(self, name, hp, damage, armor, level, loot):
    super().__init__(name, hp, damage, armor)
    self.level = level
    self.loot = loot

class Warrior(Player):
  def __init__(self, name, hp, damage, armor, stamina, level):
    super().__init__(name, hp, damage, armor)
    self.stamina = stamina
    self.level = level

class Mage(Player):
  def __init__(self, name, hp, damage, armor, mana, level):
    super().__init__(name, hp, damage, armor)
    self.mana = mana
    self.level = level

class Ranger(Player):
  def __init__(self, name, hp, damage, armor, critical, level):
    super().__init__(name, hp, damage, armor)
    self.critical = critical
    self.level = level


def Start():
  global a
  global Class
  print("Welcome to VSCRPG")
  a = input("Please selected your class (Warrior/Mage/Ranger) : ").lower()

  if a == "warrior":
    print("Congrats you've chosen Warrior!")
    Wait()
    Info()
    Class = Warrior("Player",200, 10, 5, 50, 1)     

  elif a == "mage":
    print("Congrats you've chosen Mage!")
    Wait()
    Info()
    Class = Mage("Player",120, 15, 2, 150, 1)   

  elif a == "ranger":
    print("Congrats you've chosen Ranger!")
    Wait()
    Info()
    Class = Ranger("Player",150, 20, 4, 10/100, 1)   

  else:
    print("Please select the given class")
    Wait()
    Start()

def Info():
  print('''
1. Status Window
2. Inventory
3. Blessings / Curses
4. Shop
5. Fight!
''')
  b = int(input("What would you like to to do? (1-5) "))

  if b == 1:
    Status_Window()

  elif b == 2:
    # print(Inventory)
    print("Test2")

  elif b == 3:
    # print(Effects)  
    print("Test3")

  elif b == 4:
    # print(Shop)  
    print("Test4")

  elif b == 5:
    # print(Fight)  
    print("Test5")

def Status_Window():
  global Class
  if a == "warrior":
    print(Class)

  elif a == "mage":
    print(Class)

  elif a == "ranger":
    print(Class)

Start()
