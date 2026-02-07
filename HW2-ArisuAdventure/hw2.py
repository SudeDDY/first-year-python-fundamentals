"""ARISU'S BORDERLAND ADVENTURES <3"""

hp = 10
gold = 0
place = "forest"

def write_log_line(string):
    with open("treasure_log.txt","a") as f:
        f.write(string)
        f.write("\n")

def apply_event(x,y):
    global gold , hp
    gold += x
    hp += y

def read_intro_line():
    with open("treasure_log.txt", "r") as f:
        line = f.readline()
        print(line)

def decide_step2_pathA(decision):
    global hp , gold, place
    place = "wide river"
    if decision == "A" and gold>=2:
        gold -= 2
        write_log_line(f"Arisu reached a wide river and he paid a ferryman 2 golds to cross safely to the other side!")
        write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
        print("You paid the ferryman 2 gold and crossed safely.")
    elif decision == "A" and gold<2:
        hp -= 3
        write_log_line(f"Arisu wanted to pay to a ferryman but he didn't have enough money so he swam across and lost 3 health points while swimming!")
        write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
        print("You don't have enough money so you tried to swim across and lost your strength. -3 HP.")
    elif decision == "B":
        hp -= 3
        write_log_line(f"Arisu swam across, he lost 3 health points while swimming!")
        write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
        print("You tried to swim across and lost your strength. -3 HP.")

def decide_step2_pathB(decision):
    global gold, hp, place
    place= "forest"
    if decision== "A" and hp <= 5:
        hp = hp + 1
        write_log_line("Arisu felt weak and tired, so he decided to took a rest and found a shelter, gained 1 health point.")
        write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
        print("You found a shelter and recovered. +1HP.")
    elif decision=='B' and hp > 5:
        hp = hp - 2
        write_log_line("Arisu was feeling strong, so he decided to keep going without resting, lost 2 health point.")
        write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
        print("You pressed on without resting. -2HP.")
    elif (decision== "A" and hp > 5) or (decision== "B" and hp <= 5):
        write_log_line("He choosed wrong way and the other option was executed.")
        print("You shouldn't choose this, other option has been executed! ")
        if decision == "A":
            hp = hp - 2
            write_log_line("Arisu was feeling strong, so he decided to keep going without resting, lost 2 health point.")
            write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
            print("You pressed on without resting. -2HP.")
        elif decision == "B":
            hp = hp + 1
            write_log_line("Arisu felt weak and tired, so he decided to took a rest and found a shelter, gained 1 health point.")
            write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
            print("You found a shelter and recovered. +1HP.")

def load_events_for_pack(pack_name):

    if pack_name == "A":
        return 6
    elif pack_name == "B":
        return 4
    else:
        return 0

def run_pack(pack_name):
    global place, hp, gold 
    total_steps = load_events_for_pack(pack_name)

    if pack_name == "A":
        for step in range(1,total_steps+1):

            if step == 1:
                apply_event(5,0)
                print(f"You found 5 gold in the {place}.")
                write_log_line(f"While exploring the {place}, Arisu noticed something glimmering beneath the leaves, 5 gold coins!")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")

            elif step == 2:
                decision = input("You reached a wide river! Pay 2 golds to cross safely (a) / Swim across and lose 3 health points (b) ").upper()
                decide_step2_pathA(decision)

            elif step == 3:
                place = "inside of the dark cave"
                apply_event(0,-3)
                print("A trap in the cave! -3 HP.")
                write_log_line(f"Inside a dark cave, a hidden trap was triggered. Arisu lost 3 health points :(")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")

            elif step == 4:
                place = "near the riverbank"
                apply_event(2,0)
                print("A healing herb by the river. +2 HP.")
                write_log_line(f"Near the riverbank, he found a glowing green herb. He ate it and regained 2 health points!")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")

            elif step == 5:
                apply_event(0,-2)
                print("A draining mirage in the desert. -2 HP.")
                write_log_line(f"In the desert, Arisu chased a mirage and got exhausted. He lost 2 health points :( ")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")

            elif step == 6:
                apply_event(10,0)
                print("A sunken chest in the river! +10 gold!!! :)) ")
                write_log_line(f"While returning once more to the river, he discovered a sunken chest buried beneath the sand. Inside, he found 10 gold coins!! ")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")

        #SUM
        print("-" * 30)
        print(f"SUMMARY: HP = {hp}, GOLD = {gold}, STEPS = {step}")
        print("-" * 30)
    
    elif pack_name == "B":
        for step in range(1, total_steps+1):

            if step == 1:
                apply_event(0, -5)
                print(f"Bee swarm in the {place}!. -5HP.")
                write_log_line(f"While walking trough the {place}, Arisu was attacked by a swarm of bees. He managed to escape but lost 5 health points.")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
            elif step == 2:
                decision = input("You feel weak and tired! Take a rest (a) / Continue without resting (b) ").upper
                decide_step2_pathB(decision)
            elif step == 3:
                place = "inside of a cave"
                apply_event(4, 0)
                print("You mined ore in the cave! +4 gold.")
                write_log_line("Arisu found some valuable ore in the cave and he gained 4 gold. ")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
            elif step == 4:
                place = "at the riverbank"
                apply_event(0, -8)
                print("A whirlpool drags you under! -8 HP.")
                print("The journey ends here.")
                write_log_line(f"At the riverband, Arisu attempted to cross the fast current. However, he was caught in a whirlpool and he lost 8 health points! ")
                write_log_line("Arisu could not recover from the injury, so GAME OVER!!! ")
                write_log_line(f"He has {gold} gold, {hp} health points and his location is: {place}")
       
        print("----------------------------------------------------------------------------------------------------------------------")
        print(f"SUMMARY: HP = {hp}, GOLD = {gold}, STEPS = {step}")
        print("----------------------------------------------------------------------------------------------------------------------")

read_intro_line()
while True: 
    pack_name = input("Choose your adventure! The Golden River (Pack A) / The Dangerous Canyon (Pack B) - please just write A or B for all decisions: ").upper()
    if pack_name == "A" or pack_name == "B":
        print(f'WELCOME ARISU! OUR HERO! Lets choose PACK {pack_name}!')
        write_log_line(f"Arisu choosed to play with PACK {pack_name}")
        break
    else:
        print("Just write A or B! ")
        write_log_line(f"Arisu choosed to play with PACK {pack_name}? ASKING AGAIN! ")

if pack_name == "A":
    run_pack("A")
elif pack_name == "B":
    run_pack("B")
    

