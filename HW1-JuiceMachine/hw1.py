total = 0

# Greet the user warmly
name = input("Welcome girl! Please let me know who are you <3 : ").upper()
print(name + "! Welcome back my friend, skrrt!") 

# Let them choose from among the previous, and future favorites / Handle unavailable items gracefully / The mango situation 
while True:
        fruit = input("Which fruit would you prefer?  ").lower()

        if fruit == "apple":
            break
        elif fruit == "orange":
            break
        elif fruit == "carrot":
            break
        elif fruit == "pomegranate":
            break
        elif fruit == "grape":
            break
        elif fruit == "watermelon":
            break
        elif fruit == "date":
            break
        elif fruit == "limeade":
            break
        elif fruit == "mango":
            print("The mango was a bust, so it will no longer be served. We apologize profusely for having dared to serve such a horrid drink :(")
        else:
            print("We dont have that thing :/") 

    # The cup sizes      
while True:
        size = input("Choose a size! ").lower()

        if size == "small":
            break
        elif size == "medium":
            break
        elif size == "large":
            break
        elif size == "huge":
            break
        elif size == "enormous":
            break
        elif size == "gigantic":
            break
        else:
            print("We dont have that size :/ " \
            "Options are: Small, Medium, Large, Huge, Enormous, Gigantic") 

    # Prices     

if fruit == "apple":
            if size == "small":
                total = total + 10
            elif size == "medium":
                total = total + 11
            elif size == "large":
                total = total + 12
            elif size == "huge":
                total = total + 13
            elif size == "enormous":
                total = total + 14
            elif size == "gigantic":
                total = total + 15
        
if fruit == "orange":
            if size == "small":
                total = total + 15
            elif size == "medium":
                total = total + 16
            elif size == "large":
                total = total + 17
            elif size == "huge":
                total = total + 18
            elif size == "enormous":
                total = total + 19
            elif size == "gigantic":
                total = total + 20

if fruit == "carrot":
            if size == "small":
                total = total + 13
            elif size == "medium":
                total = total + 14
            elif size == "large":
                total = total + 15
            elif size == "huge":
                total = total + 16
            elif size == "enormous":
                total = total + 17
            elif size == "gigantic":
                total = total + 18

if fruit == "pomegranate":
            if size == "small":
                total = total + 25
            elif size == "medium":
                total = total + 26
            elif size == "large":
                total = total + 27
            elif size == "huge":
                total = total + 28
            elif size == "enormous":
                total = total + 29
            elif size == "gigantic":
                total = total + 30

if fruit == "grape":
            if size == "small":
                total = total + 20
            elif size == "medium":
                total = total + 21
            elif size == "large":
                total = total + 22
            elif size == "huge":
                total = total + 23
            elif size == "enormous":
                total = total + 24
            elif size == "gigantic":
                total = total + 25

if fruit == "watermelon":
            if size == "small":
                total = total + 5
            elif size == "medium":
                total = total + 6
            elif size == "large":
                total = total + 7
            elif size == "huge":
                total = total + 8
            elif size == "enormous":
                total = total + 9
            elif size == "gigantic":
                total = total + 10

if fruit == "date":
            if size == "small":
                total = total + 30
            elif size == "medium":
                total = total + 31
            elif size == "large":
                total = total + 32
            elif size == "huge":
                total = total + 33
            elif size == "enormous":
                total = total + 34
            elif size == "gigantic":
                total = total + 35

if fruit == "limeade":
            print("Btw it's not a juice you alr know that right? :)")
            if size == "small":
                total = total + 17
            elif size == "medium":
                total = total + 18
            elif size == "large":
                total = total + 19
            elif size == "huge":
                total = total + 20
            elif size == "enormous":
                total = total + 21
            elif size == "gigantic":
                total = total + 22

print(total)

# Charging for ice
ice = input("Wanna extra ice? It's only 1$! ")
if ice == "yes" and fruit != "limeade":
        total += 2
        if (fruit == "apple" and size == "large") or (fruit == "orange" and size == "large"):
            print("There is 2$ surcharge for your rare combination!")
            total += 2 #total 4$, double of 2 (2+2)
        elif (fruit == "apple" and size == "medium") or (fruit == "orange" and size == "medium"):
            print("There is 0.5$ surcharge for your rare choice!")
            total -= 0.5 #total 1.5, triple of 0.5 (2-0.5)
print(total)

# Sugar is bad
sugar = input("Wanna extra sugar?  ")
if sugar == "yes": 
        if fruit == "pomegranate":
            total += 5
        elif fruit == "grape":
            total += 5
        elif fruit == "date":
            total += 5
            
        elif fruit == "apple":
            total += 0.3
        elif fruit == "orange":
            total += 0.3
        elif fruit == "carrot":
            total += 0.3
        elif fruit == "watermelon":
            total += 0.3
        elif fruit == "limeade":
            total += 0.3
print(total)

# Allow for large orders
large = input("Wanna larger order? ").lower()
if large == "yes":
    large = input("Are you sure!? ").lower()
    if large == "yes":
        large = input("Are you SUPER sure!? ").lower()
        if large == "yes":
            print("Then order one more drink amigo!")

            # Same codes for second order + blueberry (just for Alex)
            while True:
                    fruit2 = input("Which fruit would you prefer?  ").lower()

                    if fruit2 == "apple":
                        break
                    elif fruit2 == "orange":
                        break
                    elif fruit2 == "carrot":
                        break
                    elif fruit2 == "pomegranate":
                        break
                    elif fruit2 == "grape":
                        break
                    elif fruit2 == "watermelon":
                        break
                    elif fruit2 == "date":
                        break
                    elif fruit2 == "limeade":
                        break
                    elif fruit2 == "blueberry":
                        break
                    elif fruit2 == "mango":
                        print("The mango was a bust, so it will no longer be served. We apologize profusely for having dared to serve such a horrid drink :(")
                    else:
                        print("We dont have that thing :/") 
                
            while True:
                    size2 = input("Choose a size! ").lower()

                    if size2 == "small":
                        break
                    elif size2 == "medium":
                        break
                    elif size2 == "large":
                        break
                    elif size2 == "huge":
                        break
                    elif size2 == "enormous":
                        break
                    elif size2 == "gigantic":
                        break
                    else:
                        print("We dont have that size :/ " \
                        "Options are: Small, Medium, Large, Huge, Enormous, Gigantic") 
                
            if fruit2 == "apple":
                        if size2 == "small":
                            total = total + 10
                        elif size2 == "medium":
                            total = total + 11
                        elif size2 == "large":
                            total = total + 12
                        elif size2 == "huge":
                            total = total + 13
                        elif size2 == "enormous":
                            total = total + 14
                        elif size2 == "gigantic":
                            total = total + 15
                    
            if fruit2 == "orange":
                        if size2 == "small":
                            total = total + 15
                        elif size2 == "medium":
                            total = total + 16
                        elif size2 == "large":
                            total = total + 17
                        elif size2 == "huge":
                            total = total + 18
                        elif size2 == "enormous":
                            total = total + 19
                        elif size2 == "gigantic":
                            total = total + 20

            if fruit2 == "carrot":
                        if size2 == "small":
                            total = total + 13
                        elif size2 == "medium":
                            total = total + 14
                        elif size2 == "large":
                            total = total + 15
                        elif size2 == "huge":
                            total = total + 16
                        elif size2 == "enormous":
                            total = total + 17
                        elif size2 == "gigantic":
                            total = total + 18

            if fruit2 == "pomegranate":
                        if size2 == "small":
                            total = total + 25
                        elif size2 == "medium":
                            total = total + 26
                        elif size2 == "large":
                            total = total + 27
                        elif size2 == "huge":
                            total = total + 28
                        elif size2 == "enormous":
                            total = total + 29
                        elif size2 == "gigantic":
                            total = total + 30

            if fruit2 == "grape":
                        if size2 == "small":
                            total = total + 20
                        elif size2 == "medium":
                            total = total + 21
                        elif size2 == "large":
                            total = total + 22
                        elif size2 == "huge":
                            total = total + 23
                        elif size2 == "enormous":
                            total = total + 24
                        elif size2 == "gigantic":
                            total = total + 25

            if fruit2 == "watermelon":
                        if size2 == "small":
                            total = total + 5
                        elif size2 == "medium":
                            total = total + 6
                        elif size2 == "large":
                            total = total + 7
                        elif size2 == "huge":
                            total = total + 8
                        elif size2 == "enormous":
                            total = total + 9
                        elif size2 == "gigantic":
                            total = total + 10

            if fruit2 == "date":
                        if size2 == "small":
                            total = total + 30
                        elif size2 == "medium":
                            total = total + 31
                        elif size2 == "large":
                            total = total + 32
                        elif size2 == "huge":
                            total = total + 33
                        elif size2 == "enormous":
                            total = total + 34
                        elif size2 == "gigantic":
                            total = total + 35

            if fruit2 == "limeade":
                        print("Btw it's not a juice you alr know that right? :)")
                        if size2 == "small":
                            total = total + 17
                        elif size2 == "medium":
                            total = total + 18
                        elif size2 == "large":
                            total = total + 19
                        elif size2 == "huge":
                            total = total + 20
                        elif size2 == "enormous":
                            total = total + 21
                        elif size2 == "gigantic":
                            total = total + 22

            print(total)

    ice2 = input("Wanna extra ice? It's only 1$! ")
    if ice2 == "yes" and fruit2 != "limeade":
        total += 2
        if (fruit == "apple" and size == "large") or (fruit == "orange" and size == "large"):
            print("There is 2$ surcharge for your rare combination!")
            total += 2 #total 4$, double of 2 (2+2)
        elif (fruit == "apple" and size == "medium") or (fruit == "orange" and size == "medium"):
            print("There is 0.5$ surcharge for your rare choice!")
            total -= 0.5 #total 1.5, triple of 0.5 (2-0.5)
    print(total)

    sugar2 = input("Wanna extra sugar?  ")
    if sugar2 == "yes": 
                
                    if fruit2 == "pomegranate":
                        total += 5
                    elif fruit2 == "grape":
                        total += 5
                    elif fruit2 == "date":
                        total += 5
                        
                    elif fruit2 == "apple":
                        total += 0.3
                    elif fruit2 == "orange":
                        total += 0.3
                    elif fruit2 == "carrot":
                        total += 0.3
                    elif fruit2 == "watermelon":
                        total += 0.3
                    elif fruit2 == "limeade":
                        total += 0.3
    
    # All free for Alex :/
    if fruit2 == "blueberry" and size2 == "gigantic" and ice2 == "no" and sugar2 == "yes" and name == "ALEX":
        total = 0
    elif (fruit2 == "blueberry") and (size2 != "gigantic" or ice2 != "no" or sugar2 != "yes" or name != "ALEX"):
        print("We don't have that drink :( ")

    print("Your second order: ")
    print("fruit:" , fruit2 , " size:" ,  size2 , " ice:", ice2 , " sugar:" , sugar2)

print("Your drink is ready! There is: ")
print("fruit:" , fruit , " size:" ,  size , " ice:", ice , " sugar:" , sugar)
print("The total cost is: " , total , "$")