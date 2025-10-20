import os
import time
import random

Class = ""
Player_level = 1
selected_skills = []
os.system("cls")

def Wait():
    print("Please wait...")
    time.sleep(1)
    os.system("cls")

def Enter():
    print("Please press [Enter] to continue")
    input("")
    os.system("cls")

class Status:
    def __init__(self, name, hp, damage, armor, level):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.level = level

class Creep(Status):
    def __init__(self, name, hp, damage, armor, level):
        super().__init__(name, hp, damage, armor, level)

class Warrior(Status):
    def __init__(self, name, hp, damage, armor, level, stamina):
        super().__init__(name, hp, damage, armor, level)
        self.stamina = stamina
        self.max_stamina = stamina
        self.base_hp = hp
        self.base_damage = damage
        self.base_armor = armor

class Mage(Status):
    def __init__(self, name, hp, damage, armor, level, mana):
        super().__init__(name, hp, damage, armor, level)
        self.mana = mana
        self.max_mana = mana
        self.base_hp = hp
        self.base_damage = damage
        self.base_armor = armor

class Ranger(Status):
    def __init__(self, name, hp, damage, armor, level, critical):
        super().__init__(name, hp, damage, armor, level)
        self.critical = critical
        self.base_hp = hp
        self.base_damage = damage
        self.base_armor = armor
        self.first_dodge = True

name = input("Please input your username before playing : ")

def Start():
    global a
    global Class
    print("Welcome to VSCRPG")
    a = input("Please select your class (Warrior/Mage/Ranger) : ").lower()

    if a == "warrior":
        print("Congrats you've chosen Warrior!")
        Class = Warrior(name,200, 10, 5, 1, 50)     
        Wait()
        Info()

    elif a == "mage":
        print("Congrats you've chosen Mage!")
        Class = Mage(name,120, 15, 2, 1, 150)   
        Wait()
        Info()

    elif a == "ranger":
        print("Congrats you've chosen Ranger!")
        Class = Ranger(name,150, 20, 4, 1, "10%")  
        Wait()
        Info()
 
    else:
        print("Please select the given class")
        Wait()
        Start()

def Info():
    print("1. Status Window")
    if len(selected_skills) >= 3:
        print("2. Skills Set (LOCKED)")
    else:
        print("2. Skills Set")
    print("3. Fight!")
    b = int(input("What would you like to do? (1-3) "))

    if b == 1:
        Wait()
        Status_Window()

    elif b == 2:
        if len(selected_skills) >= 3:
            print("You have successfully learned 3 skills.")
            Wait()
            Info()
        else:
            Wait()
            Skills()

    elif b == 3:
        Wait()
        Fight()

def Status_Window():
    global Class
    print(f"Player Name: {Class.name} \nHP: {Class.hp} \nDamage: {Class.damage} \nArmor: {Class.armor} \nLevel: {Class.level}")

    if a == "warrior":
        print(f"Stamina: {Class.stamina} \nClass: Warrior")
    elif a == "mage":
        print(f"Mana: {Class.mana} \nClass: Mage")
    elif a == "ranger":
        print(f"Critical: {Class.critical} \nClass: Ranger")

    if selected_skills:
        print("Skills set: ")
        for c in selected_skills:
            print(f"- {c}")
    else:
        print("Skills set: None")

    Enter()
    Info()

def Skills():
    global selected_skills
    if len(selected_skills) >= 3 :
        print("You can not learn more skills")

    if a == "warrior":
        skills_list = [
            "Lion's Terror (Stuns the enemy and reduces 50% armor)", 
            "Mountain Cleave (Deals 150% damage to the enemy)", 
            "Armored (Passive) (Increases armor by 20%)", 
            "Berserker (Passive) (Enables double hit)",
            "Iron Body (Passive) (Max HP increase to 300)"
        ]

    elif a == "mage":
        skills_list = [
            "Fire Bolt (Deals 75% damage to the enemy)",
            "Dark Void (Deals 25% Max HP of the enemy (Can't be Chained))",
            "Chain Casting (Passive) (1/4 Chance to double cast, 1/8 Chance to triple cast)",
            "Archmage (Passive) (Increase spell damage by 50%)",
            "Talent Bearer (Passive) (Max Mana increase to 300)"
        ]

    elif a == "ranger":
        skills_list = [
            "Headshot (Deals 300% damage to the enemy)",
            "Piercing Arrow (Deals 100% damage, no armor)",
            "Sniper (Passive) (Increases crit damage 50%)",
            "Hunter's Eyes (Passive) (Increases crit chance to 3/10)",
            "Lightweighted (Passive) (Dodges the first attack)"
        ]
      
    print("Available Skills:") 
    for i, skill in enumerate(skills_list, 1):
        print(f"{i}. {skill}")

    while True:
        skill = input("What skills would you like to pick? (Only pick 3 skills and use , [Ex: 1,2,3]) ")
        selected_index = [int(x.strip()) for x in skill.split(",")]
        selected_skills = [skills_list[i-1] for i in selected_index]
        if len(selected_skills) < 3 :
            print("You HAVE TO pick 3 skills!")
        elif len(selected_skills) > 3 :
            print("You CAN ONLY pick 3 skills")
        elif len(selected_skills) == 3 : 
            print("You have selected:")
            for c in selected_skills:
                print(f"- {c}")
            apply_passive_skills()
            Enter()
            Info()
            break

def apply_passive_skills():
    global Class
    for skill in selected_skills:
        if "Armored (Passive)" in skill:
            Class.armor = int(Class.base_armor * 1.2)
        elif "Berserker (Passive)" in skill:
            Class.damage = Class.base_damage * 2
        elif "Iron Body (Passive)" in skill:
            Class.hp = 300
        elif "Archmage (Passive)" in skill:
            Class.damage = int(Class.base_damage * 1.5)
        elif "Talent Bearer (Passive)" in skill:
            Class.mana = 300
            Class.max_mana = 300
        elif "Hunter's Eyes (Passive)" in skill:
            Class.critical = "30%"
        elif "Lightweighted (Passive)" in skill:
            Class.first_dodge = True

def Fight():
    global Player_level, Class

    Creeps = [
        Creep("Skeleton", 40, 5, 1, 1),       
        Creep("Goblin", 70, 8, 2, 2),      
        Creep("Orc", 120, 12, 4, 3),     
        Creep("Bandit", 180, 18, 8, 4),     
        Creep("Golem", 280, 25, 12, 5)   
    ]

    Bosses = [
        Creep("Skeleton King", 100, 9, 2, 1),     
        Creep("Goblin Chief", 160, 12, 4, 2),    
        Creep("Orc Warlord", 260, 18, 6, 3),      
        Creep("Bandit Leader", 380, 25, 10, 4),  
        Creep("Ancient Golem", 600, 35, 15, 5)  
    ]

    current_level = Class.level
    enemy = Creeps[current_level - 1]
    boss = Bosses[current_level - 1]

    fights_until_boss = 3
    fights_done = 0
    player_hp = Class.hp  
    
    if a == "ranger" and "Lightweighted (Passive)" in selected_skills:
        Class.first_dodge = True
    if a == "warrior":
        Class.stamina = Class.max_stamina
    if a == "mage":
        Class.mana = Class.max_mana

    while True:
        used_ranger_skills = set()  # reset each new fight

        if fights_done < fights_until_boss:
            print(f"A {enemy.name} appears!")
            current_enemy = enemy
            enemy_hp = enemy.hp
        else:
            print(f"The {boss.name} has appeared! Prepare for the boss fight!")
            current_enemy = boss
            enemy_hp = boss.hp

        enemy_stunned = False

        while player_hp > 0 and enemy_hp > 0:
            print(f"\n{Class.name} (HP: {player_hp})  VS  {current_enemy.name} (HP: {enemy_hp})")
            if a == "warrior":
                print(f"Stamina: {Class.stamina}")
            elif a == "mage":
                print(f"Mana: {Class.mana}")
            print("[1] Attack")
            print("[2] Skills")
            move = input("Choose your action: ")

            if move == "1":
                damage_to_enemy = Class.damage
                if a == "ranger":
                    crit_chance = 0.1
                    if "Hunter's Eyes (Passive)" in selected_skills:
                        crit_chance = 0.3
                    if random.random() < crit_chance:
                        crit_multiplier = 2.0
                        if "Sniper (Passive)" in selected_skills:
                            crit_multiplier = 3.0
                        damage_to_enemy = int(Class.damage * crit_multiplier)
                        print("CRITICAL HIT!")

                elif a == "mage" and "Chain Casting (Passive)" in selected_skills:
                    cast_times = 1
                    if random.random() < 0.25:
                        cast_times = 2
                        if random.random() < 0.5:
                            cast_times = 3
                    if cast_times > 1:
                        print(f"Chain Casting! Attack hits {cast_times} times!")
                        damage_to_enemy *= cast_times

                damage_to_enemy = max(1, damage_to_enemy - current_enemy.armor)
                enemy_hp -= damage_to_enemy
                print(f"You dealt {damage_to_enemy} damage!")

                if enemy_hp <= 0:
                    if fights_done < fights_until_boss:
                        print(f"You defeated {current_enemy.name}!")
                        fights_done += 1
                        used_ranger_skills.clear()
                        Enter()
                        break
                    else:
                        print(f"\nYou defeated the {current_enemy.name}!")
                        used_ranger_skills.clear()
                        Class.level += 1
                        if current_enemy.name == "Ancient Golem":
                            os.system("cls")
                            print("\nYou have defeated the Ancient Golem and cleared the entire dungeon")
                            print("Thank you for playing VSCRPG!")
                            exit()
                        print(f"You leveled up! Now you are Level {Class.level}")
                        Enter()
                        Info()
                        return

                if not enemy_stunned:
                    damage_to_player = max(1, current_enemy.damage - Class.armor)
                    if a == "ranger" and Class.first_dodge:
                        print("Lightweighted passive activated! You dodged the attack")
                        Class.first_dodge = False
                    else:
                        player_hp -= damage_to_player
                        print(f"{current_enemy.name} attacked you for {damage_to_player} damage")
                else:
                    print(f"{current_enemy.name} is stunned and cannot attack")
                    enemy_stunned = False

                if player_hp <= 0:
                    print(f"\nYou were defeated by {current_enemy.name}...")
                    print("Game over")
                    Enter()
                    Info()
                    return

                time.sleep(1)
                os.system("cls")

            elif move == "2":
                active_skills = [s for s in selected_skills if "(Passive)" not in s]

                if not active_skills:
                    print("You don't have any active skills to use in battle")
                    Enter()
                    continue

                print("\nChoose a skill to use:")
                for i, skill in enumerate(active_skills, 1):
                    print(f"[{i}] {skill}")

                choice = input("Enter the skill number (or press Enter to cancel): ").strip()

                if choice == "":
                    print("You decided not to use a skill")
                    time.sleep(1)
                    os.system("cls")
                    continue

                try:
                    chosen_skill = active_skills[int(choice) - 1]
                    print(f"\nYou used {chosen_skill}")

                    #Warrior
                    if "Lion's Terror" in chosen_skill:
                        if a == "warrior" and Class.stamina >= 10:
                            enemy_stunned = True
                            Class.stamina -= 10
                            reduced_armor = current_enemy.armor * 0.5
                            current_enemy.armor -= reduced_armor
                            print(f"{current_enemy.name}'s armor has been reduced and they are stunned for one turn")
                        else:
                            print("Not enough stamina")

                    elif "Mountain Cleave" in chosen_skill:
                        if a == "warrior" and Class.stamina >= 15:
                            damage_to_enemy = max(1, int(Class.damage * 1.5) - current_enemy.armor)
                            enemy_hp -= damage_to_enemy
                            Class.stamina -= 15
                            print(f"You cleaved {current_enemy.name} for {damage_to_enemy} damage!")
                        else:
                            print("Not enough stamina")

                    #Mage
                    elif "Fire Bolt" in chosen_skill:
                        if a == "mage" and Class.mana >= 30:
                            damage_to_enemy = max(1, int(Class.damage * 0.75) - current_enemy.armor)
                            enemy_hp -= damage_to_enemy
                            Class.mana -= 30
                            print(f"Fire Bolt hits {current_enemy.name} for {damage_to_enemy} damage!")
                        else:
                            print("Not enough mana")

                    elif "Dark Void" in chosen_skill:
                        if a == "mage" and Class.mana >= 50:
                            damage_to_enemy = int(current_enemy.hp * 0.25)
                            enemy_hp -= damage_to_enemy
                            Class.mana -= 50
                            print(f"Dark Void consumes {damage_to_enemy} HP from {current_enemy.name}!")
                        else:
                            print("Not enough mana")

                    #Ranger 
                    elif "Headshot" in chosen_skill:
                        if a == "ranger":
                            if "Headshot" in used_ranger_skills:
                                print("You already used Headshot in this battle!")
                            else:
                                damage_to_enemy = max(1, int(Class.damage * 3) - current_enemy.armor)
                                enemy_hp -= damage_to_enemy
                                used_ranger_skills.add("Headshot")
                                print(f"HEADSHOT! You deal {damage_to_enemy} damage")
                        else:
                            print("You can't use that skill")

                    elif "Piercing Arrow" in chosen_skill:
                        if a == "ranger":
                            if "Piercing Arrow" in used_ranger_skills:
                                print("You already used Piercing Arrow in this battle")
                            else:
                                damage_to_enemy = Class.damage  # Ignores armor
                                enemy_hp -= damage_to_enemy
                                used_ranger_skills.add("Piercing Arrow")
                                print(f"Piercing Arrow strikes through armor for {damage_to_enemy} damage")
                        else:
                            print("You can't use that skill")

                    Enter()

                except (ValueError, IndexError):
                    print("Please enter a valid skill")
                    Enter()

            else:
                print("Please select 1-2")

        if fights_done == fights_until_boss:
            print("\nThe boss senses your presence...")
            time.sleep(1)

Start()
