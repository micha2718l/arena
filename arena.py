from random import *
# player class
class Player:
    life = 5
    attackpower = 4
    gold = 0
    name = "name"
    traincost = 5
    fights = 0
    totalfights = 0
    stagger = 0
# enemy class
class Enemy:
    life = 5
    attackpower = 5
    goldvalue = 10
    name = "name"
    stagger = 0
    difficulty = 0
# Game functions
def idle(player): # idle state before fight, player can either fight(choice = 1) train(choice = 2) or pay to win (choice = 3)
    idle = 1
    while (idle == 1):
        if (player.gold >= 100):
            ready = 1
        else:
            ready = 0

        while (ready == 0):
            choice = int(input("You currently have " + str(player.life) + " health and " + str(player.gold) + " gold.\nYou can fight or spend gold on training (cost = " + str(player.traincost) + "g).\nWhat would you like to do? (1 = fight) (2 = train)\n\nInput:"))
            if (choice == 1):
                return choice
            elif(choice == 2):
                if (player.gold >= player.traincost):
                    train(player)
                    player.gold = player.gold - player.traincost
                    player.traincost = player.traincost + 1
                else:
                    print("Not enough gold to train\n\n")
            else:
                print("Not a valid choice\n\n")

        while (ready == 1):
            choice = int(input("You currently have " + str(player.life) + " health and " + str(player.gold) + " gold.\nYou can fight,spend gold on training (cost = " + str(player.traincost) + "g) or pay to leave (100g).\nWhat would you like to do? (1 = fight) (2 = train) (3 = win)\n\nInput:"))
            if (choice == 1):
                return choice
            elif(choice == 2):
                if (player.gold >= player.traincost):
                    train(player)
                    player.gold = player.gold - player.traincost
                    player.traincost = player.traincost + 2
                    break
                else:
                    print("Not enough gold to train\n\n")
            elif (choice == 3):
                return choice
            else:
                print("Not a valid choice\n\n")
def train(player): #player training, increases power or health. some rand involved
    train = 1
    while (train == 1):
        choice = int(input("\n\nWelcome to the training grounds, you can either train with a grand champion(80% chance increase attackpower by 2), master archer(50% chance increase life and attackpower by 1),\nmaster swordsman(10% chance increase attackpower by 5, or by yourself (100% chance increase life by 1).\
                           \nWhat would you like to do? (Grand Champion = 1) (Master Archer = 2) (Master Swordsman = 3) (By Yourself = 4)\n\nInput: "))
        prop = randint(1, 10) # random number generation for probability of success
        if (choice == 1):
            if (prop >= 9):
                print("You somehow failed to grasp the champion's instructions and learned nothing from him.\n\n")
                return player
            else:
                player.attackpower = player.attackpower + 2
                print("You comprehended everything the champion taught you, attack power is now: " + str(player.attackpower)+"\n\n")
                return player
        elif (choice == 2):
            if (prop >= 6):
                print("You somehow failed to grasp the archer's instructions and learned nothing from him.\n\n")
                return player
            else:
                player.attackpower = player.attackpower + 1
                player.life = player.life + 1
                print("You comprehended everything the archer taught you, attack power is now: " + str(player.attackpower) + " and life is: " + str(player.life) + "\n\n")
                return player
        elif (choice == 3):
            if (prop >= 2):
                print("You failed to grasp the swordsman' complex instructions and learned nothing from him.\n\n")
                return player
            else:
                player.attackpower = player.attackpower + 5
                print("You comprehended everything the swordsman taught you, attack power is now: " + str(player.attackpower) + "\n\n")
                return player
        elif (choice == 4):
            player.life = player.life + 1
            print("A good workout by yourself increased your life, it is now: " + str(player.life) + "\n\n")
            return player
        else:
            print("Not a valid choice\n\n")
# fighting mechanic
def fighting(fighter, player):
    fighting = 1
    coinflip = randint(1,2)
    while (fighting == 1):
        while (coinflip == 1):  # Player chooses stance first
            print("\n\nYou are fighting " + fighter.name + "  life: " + str(fighter.life) + " Who is " + str(fighter.stagger) + "% staggered"\
                  + "\nYou have " + str(player.life) + " life and are " + str(player.stagger) + "% staggered\nYou have the initiative!"\
                  + "\n\n Choose your stance: (1 = aggressive) (2 = balanced) (3 = defensive)")
            stance = int(input("\ninput:"))
            if (stance == 1):
                print("You take a aggressive stance ready to unleash a flurry of blows at " + fighter.name + ".")
                fighterprob = randint(1,3)
                if (fighterprob == 1):
                    print(fighter.name + " also takes an aggressive stance trying to match your furry.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.8)*player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print("In " + fighter.name + "'s fury he doesn't manage to block your great blows.")
                        print("You inflict " + str((0.8)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.2)*fighter.attackpower
                        player.stagger = player.stagger + (15)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " fury gives him a quickness that lets him sidestep your blows and attack your legs.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.2)*fighter.attackpower) + " damage and 15% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.05)*fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0.6)*player.attackpower
                        fighter.stagger = fighter.stagger + (5)
                        print("You aggressively attack " + fighter.name + " but he lands a swift punch to your face.")
                        print("You inflict " + str((0.6)*player.attackpower) + " damage and 5% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif(fighterprob == 2):
                    print(fighter.name + " takes a balanced stance in the hopes to capitalize on your furry.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (2)
                        fighter.life = fighter.life - (0.6)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You clash weapons but by changing your footing you manage to stab " + fighter.name + " right in the chest.")
                        print("You inflict " + str((0.6)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 2% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.4)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (5)
                        print("Every single one of your blows are countered and then you feel blood runing down your arm.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 5% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.4)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.1)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.3)*player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print(fighter.name + " can't quite keep up with your assault but he manages to get one hit in")
                        print("You inflict " + str((0.3)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print(fighter.name + " takes a defensive stance, trying to deflect your vicious blows.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.5)*player.attackpower
                        fighter.stagger = fighter.stagger + (30)
                        print("You break through " + fighter.name + " guard with your quick blows and slash at his shoulder.")
                        print("You inflict " + str((0.5)*player.attackpower) + " damage and 30% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.08)*fighter.attackpower
                        player.stagger = player.stagger + (30)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " says: 'is that all you have " + player.name + " ?'" + fighter.name + "'s guard protects him from all your attacks and he shield bashes you in the face.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.08)*fighter.attackpower) + " damage and 30% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.03)*fighter.attackpower
                        player.stagger = player.stagger + (10)
                        fighter.life = fighter.life - (0.4)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " guard allows him to regain his composure after your attack")
                        print("You inflict " + str((0.4)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.03)*fighter.attackpower) + " damage and 10% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
            elif (stance == 2):
                print("You take a balanced stance.")
                fighterprob = randint(1, 3)
                if (fighterprob == 1):
                    print(fighter.name + " takes an aggressive stance.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.4) * player.attackpower
                        fighter.stagger = fighter.stagger + (20)
                        print("You capitalize on " + fighter.name + " fury and give a quick calculated strike.")
                        print("You inflict " + str((0.4)*player.attackpower) + " damage and 20% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.5) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You miss you calculated strike and are bombarded with a flurry of blows.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.5)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.1) * fighter.attackpower
                        player.stagger = player.stagger + (3)
                        fighter.life = fighter.life - (0.3) * player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print("You land a quick calculated strike on " + fighter.name + " arm, but he also manages to land a punch in your stomach.")
                        print("You inflict " + str((0.3)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 3% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif (fighterprob == 2):
                    print(fighter.name + " takes a balanced stance to match yours.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.3) * player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print("confident in your training you land hit on " + fighter.name + "'s face.")
                        print("You inflict " + str((0.3)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.2) * fighter.attackpower
                        player.stagger = player.stagger + (15)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " deflected your attack and returned his pommel to your chest.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.2)*fighter.attackpower) + " damage and 15% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.1) * fighter.attackpower
                        player.stagger = player.stagger + (1)
                        fighter.life = fighter.life - (0.35) * player.attackpower
                        fighter.stagger = fighter.stagger + (2)
                        print("You both carefully consider your strikes and each land a blow.")
                        print("You inflict " + str((0.35)*player.attackpower) + " damage and 2% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 1% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print(fighter.name + " takes a defensive stance.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.2) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("Your careful strike manges to bypass " + fighter.name + " guard.")
                        print("You inflict " + str((0.2)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.05) * fighter.attackpower
                        player.stagger = player.stagger + (20)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You miss and " + fighter.name + " stumps on your feet and gives a quick uppercut.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 20% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.02) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0.08) * player.attackpower
                        fighter.stagger = fighter.stagger + (2)
                        print("You swing left and right carfully but are still slightly hurt, but not before you land a hit.")
                        print("You inflict " + str((0.08)*player.attackpower) + " damage and 2% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.02)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
            elif (stance == 3):
                print("You take a defensive stance, raising your guard as you attack " + fighter.name + ".")
                fighterprob = randint(1, 3)
                if (fighterprob == 1):
                    print(fighter.name + " takes an aggressive stance trying to bypass your defenses.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.1) * player.attackpower
                        fighter.stagger = fighter.stagger + (50)
                        print("In" + fighter.name + "'s fury he doesn't manage to block your great shield bash.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 50% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.2) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You miss but still manage to block a majority of the attack.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.2)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.01) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.05) * player.attackpower
                        fighter.stagger = fighter.stagger + (35)
                        print("You don't do much damage but you get " + fighter.name + " off balance.")
                        print("You inflict " + str((0.05)*player.attackpower) + " damage and 35% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.01)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif (fighterprob == 2):
                    print(fighter.name + " takes a balanced stance in the hopes to find a weakness in your defense.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.05) * player.attackpower
                        fighter.stagger = fighter.stagger + (60)
                        print(fighter.name + " thinks his stance is clever but you manage to swipe his feet")
                        print("You inflict " + str((0.05)*player.attackpower) + " damage and 60% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.5) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " takes advantage of your slow form and strikes you in the back.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.5)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.2) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.1) * player.attackpower
                        fighter.stagger = fighter.stagger + (20)
                        print("You do a swift pommel strike but you feel a slash on your ankle.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 20% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.2)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print(fighter.name + " takes a defensive stance trying to match yours, you begin to circle each other.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (80)
                        print("Running at each other, you clash shields but your momentum was greater and you have knock " + fighter.name + " on his back!")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 80% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (30)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " charges you but his momentum is greater and he knocks you off your feet.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 30% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (10)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (15)
                        print("No damage is done to either of you as you circle each other, but fear stagger you both.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 15% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 10% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
            else:
                    print("Not a valid choice")
            coinflip = randint(1,2)
        while (coinflip == 2):  # fighter chooses stance first
            print("\n\nYou are fighting " + fighter.name + "  life: " + str(fighter.life) + " Who is " + str(fighter.stagger) + "% staggered" \
                  + "\nYou have " + str(player.life) + " life and are " + str(player.stagger) + "% staggered\n" + fighter.name + " has the initiative!")
            fighterprob = randint(1,3)
            if (fighterprob == 1):
                print(fighter.name + " takes a aggressive stance.")
                print("\nChoose your stance: (1 = aggressive) (2 = balanced) (3 = defensive)")
                stance = int(input("input:"))
                if (stance == 1):
                    print("You throw your shield down and match " + fighter.name + "'s rage.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0.4)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You sidestep " + fighter.name + "'s flurry of attacks and respond with a backstab. ")
                        print("You inflict " + str((0.4)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.7)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("In your rage you put up no defense to the massive attacks from " + fighter.name + ".")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.7)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.5)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.4)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You both take a good amount of damage.")
                        print("You inflict " + str((0.4)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.5)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif(stance == 2):
                    print("You try to out-think " + fighter.name + " and take a calculated balanced stance in the face of his rage.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.5)*player.attackpower
                        fighter.stagger = fighter.stagger + (5)
                        print("As " + fighter.name + " charges you deliver a straight thrust of your weapon and impale him in the chest!")
                        print("You inflict " + str((0.5)*player.attackpower) + " damage and 5% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.5)*fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You try to deliver a straight thrust but it is deflected and you recive a vast amount of hits to your shoulder.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.5)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.1)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.5)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("the fury in " + fighter.name + "'s eyes may look frightening but you still land your calculated strike.")
                        print("You inflict " + str((0.5)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif(stance == 3):
                    print("You take a defensive stance, trying to deflect " + fighter.name + "'s vicious blows.")
                    hit = randint(1,10)
                    if (hit == 1):
                        player.life = player.life - (0)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.1)*player.attackpower
                        fighter.stagger = fighter.stagger + (80)
                        print(fighter.name + " charges but you deftly dodge and swipe his feet.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 80% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.1)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0)*player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " bypasses your defenses.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.05)*fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.02)*player.attackpower
                        fighter.stagger = fighter.stagger + (20)
                        print("you clash weapons and each manage to get a hit in.")
                        print("You inflict " + str((0.02)*player.attackpower) + " damage and 20% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print("Not a valid choice")
            elif (fighterprob == 2):
                print(fighter.name + " takes a balanced stance.")
                print("\nChoose your stance: (1 = aggressive) (2 = balanced) (3 = defensive)")
                stance = int(input("input:"))
                if (stance == 1):
                    print("You side on brute strength rather then logic and take a aggressive stance.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.7) * player.attackpower
                        fighter.stagger = fighter.stagger + (5)
                        print(fighter.name + " goes for a quick calculated strike but your aggressive agility allow you to jump over the strike and deliver a swift kick.")
                        print("You inflict " + str((0.7)*player.attackpower) + " damage and 5% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.3) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You try to pommel the enemy as he approaches but " + fighter.name + " must had expected this rash action and retaliates before you land your blows.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.3)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.3) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0.6) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You hack away at " + fighter.name + " while he also lands some hits.")
                        print("You inflict " + str((0.6)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.3)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif (stance == 2):
                    print("You take a balanced stance as well.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.5) * player.attackpower
                        fighter.stagger = fighter.stagger + (5)
                        print("You out logic " + fighter.name + " and deliver a great strike in his opening.")
                        print("You inflict " + str((0.5)*player.attackpower) + " damage and 5% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.5) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " looks as if he is about to swing one way, but reverses and hits you in the back.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.5)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.3) * fighter.attackpower
                        player.stagger = player.stagger + (2)
                        fighter.life = fighter.life - (0.2) * player.attackpower
                        fighter.stagger = fighter.stagger + (2)
                        print("You each give a straight thrust to the chest.")
                        print("You inflict " + str((0.2)*player.attackpower) + " damage and 2% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.3)*fighter.attackpower) + " damage and 2% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif(stance == 3):
                    print("You take a slow defensive stance ready to block and retaliate.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.1) * player.attackpower
                        fighter.stagger = fighter.stagger + (50)
                        print(fighter.name + "'s calculated strike is deflected and you give a great shield bash.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 50% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.4) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " finds a weakness in your defense and takes the opportunity.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.4)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.1) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.05) * player.attackpower
                        fighter.stagger = fighter.stagger + (30)
                        print("You block most hits and give a quick uppercut.")
                        print("You inflict " + str((0.05)*player.attackpower) + " damage and 30% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.1)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print("Not a valid choice")
            elif (fighterprob == 3):
                print(fighter.name + " takes a defensive stance.")
                print("\nChoose your stance: (1 = aggressive) (2 = balanced) (3 = defensive)")
                stance = int(input("input:"))
                if (stance == 1):
                    print("Your aggressive stance should be able to overcome " + fighter.name + "'s defence.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (5)
                        fighter.life = fighter.life - (0.4) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("As " + fighter.name + " approaches your start overwhelming him with your attacks.")
                        print("You inflict " + str((0.4)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 5% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.05) * fighter.attackpower
                        player.stagger = player.stagger + (20)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " appraches slowly and you go to start attacking but then one moment later you are eating his shield.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 20% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.05) * fighter.attackpower
                        player.stagger = player.stagger + (10)
                        fighter.life = fighter.life - (0.1) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print(fighter.name + " approaches, shield raised but this allows you to run around and hit a weakness in his defense.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 10% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif (stance == 2):
                    print("You take a balanced stance so that you may logically find an opening in " + fighter.name + "'s guard.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0.1) * player.attackpower
                        fighter.stagger = fighter.stagger + (2)
                        print("You manage to find an opening in " + fighter.name + "'s defence as he approaches.")
                        print("You inflict " + str((0.1)*player.attackpower) + " damage and 2% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0.08) * fighter.attackpower
                        player.stagger = player.stagger + (30)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You were shield rushed!")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.08)*fighter.attackpower) + " damage and 30% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.01) * fighter.attackpower
                        player.stagger = player.stagger + (10)
                        fighter.life = fighter.life - (0.08) * player.attackpower
                        fighter.stagger = fighter.stagger + (1)
                        print("You clash weapons and each land a hit with fist.")
                        print("You inflict " + str((0.08)*player.attackpower) + " damage and 1% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.01)*fighter.attackpower) + " damage and 10% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                elif(stance == 3):
                    print("You ready your guard as well, taking a defensive stance.")
                    hit = randint(1, 10)
                    if (hit == 1):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (0)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print("You are shield rushed but you also raise your shield and bounce " + fighter.name + " off.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 0% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    elif (hit == 2 or hit == 3):
                        player.life = player.life - (0) * fighter.attackpower
                        player.stagger = player.stagger + (20)
                        fighter.life = fighter.life - (0) * player.attackpower
                        fighter.stagger = fighter.stagger + (0)
                        print("You are shield rushed but you raise your shield as well but are bounced back.")
                        print("You inflict " + str((0)*player.attackpower) + " damage and 0% stagger."
                        "\n" + fighter.name + " inflicts " + str((0)*fighter.attackpower) + " damage and 20% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                    else:
                        player.life = player.life - (0.05) * fighter.attackpower
                        player.stagger = player.stagger + (10)
                        fighter.life = fighter.life - (0.02) * player.attackpower
                        fighter.stagger = fighter.stagger + (10)
                        print("You each shield bash each other.")
                        print("You inflict " + str((0.02)*player.attackpower) + " damage and 10% stagger."
                        "\n" + fighter.name + " inflicts " + str((0.05)*fighter.attackpower) + " damage and 10% stagger")
                        if (fighter.stagger >= 100):
                            fighter.life = fighter.life - player.attackpower
                            print("The enemy is staggered and you inflict a critical hit for " + str(
                                player.attackpower) + "!")
                            fighter.stagger = 0
                        if (player.stagger >= 100):
                            player.life = player.life - fighter.attackpower
                            print("you are staggered and the enemy inflicts a critical hit for " + str(
                                fighter.attackpower) + "!")
                            player.stagger = 0
                        if (player.life <= 0):
                            result = -1
                            return result
                        elif (fighter.life <= 0):
                            player.gold = player.gold + fighter.goldvalue
                            print("You slayed " + fighter.name + " and gained: " + str(fighter.goldvalue) + "g.")
                            return player
                else:
                    print("Not a valid choice")
            coinflip = randint(1, 2)
def fight(player):
    enemynames = ['Bernardo','Pierre','Ulysses','Rudy','Gilbert','Ashley','Chung','Byron','Ronald','Ben','Kerry','Noe','Haywood','Dusty','Anton','Darren','Juan','Bruno','Sam','Trenton','Vance','Jamal','Harold','Wilson','Cesar','Ian','Garth','Buddy','Devon','Russ','Joseph','Hoyt','Scotty','Tomas','Wilburn','Cecil','Amado','Brain','Elmer','Manual','Scottie','Rob','Everett','Dorian','Chet','Warren','Arnulfo','Val','Alvaro','Frederic','Huey','Herb','Elvin','Danial','Rolando','Simon','Garrett','Elmo','Horace','Orlando','Patrick','Carter','Delbert','Reggie','Nathaniel','Edwin','Dane','Joey','Numbers','Chi','Gil','Tomas','Lincoln','Jeffrey','Otha','Clair','Lenny','Darwin','Alexander','Ahmed','Spencer','Guy','Hank','Elias','Marcelo','Charlie','Clayton','Stan','Jerry','Harrison','Arnulfo','Wayne','Merle','Jonah','Abram','Gerardo','Johnie','Neville','Rudolph','Manuel','Bennie','Tony','Wilber','Fabian','Demetrius','Clement','Perry','Rufus','Cruz','Arturo','Ethan','Archie','Elvin','Luis','Riley','Edwin','Javier','Harrison','Shaun','Antony','Willard','Vito','Spencer','Russ','Adolfo','Tim','Kraig','Duncan','Al','Lino','Emery','Douglass','Cleveland','Haywood','Micheal','Curt','Freddy','Bernard','Merle','Logan','Steven','Truman','Erik','Tobias','Porter','Alva','Rogelio','Eddy','Warren','Hipolito','Refugio','Chang','Claudio','Sheldon','Harris','Maynard','Stephen','Barry','Weldon','Arnulfo','Bobby','Johnathan','Reginald','Carroll','Earnest','Loren','Lincoln','Darryl','Vincenzo','Alfred','Darren','Kent','Rusty','Virgilio','Elton','Claud','Mervin','Alejandro','Jerrell','Jae','William','Elden','Bruce','Malcolm','Leif','Bart','Waldo','Van','Jonah','Leon','Will','Zachary','Denver','Cedrick','Shawn','Darrel','Joey','Benton','Freddy','Cleo']
    fighter1 = Enemy()  # High health low attack power enemy
    fighter1.life = randint(2+Enemy.difficulty,Enemy.life)
    fighter1.attackpower = randint(1+Enemy.difficulty,Enemy.attackpower - 3)
    fighter1.name = enemynames[randint(1,199)]
    fighter1.goldvalue = Enemy.goldvalue + fighter1.life/2 + fighter1.attackpower
    fighter2 = Enemy()  #Balanced enemy
    fighter2.life = randint(1+Enemy.difficulty,Enemy.life)
    fighter2.attackpower = randint(1+Enemy.difficulty,Enemy.attackpower)
    fighter2.name = enemynames[randint(1,199)]
    fighter2.goldvalue = Enemy.goldvalue + fighter2.life/2 + fighter2.attackpower
    fighter3 = Enemy()  # Low health high attack power enemy
    fighter3.life = randint(1+Enemy.difficulty, Enemy.life-3)
    fighter3.attackpower = randint(2+Enemy.difficulty,Enemy.attackpower)
    fighter3.name = enemynames[randint(1,199)]
    fighter3.goldvalue = Enemy.goldvalue + fighter3.life/2 + fighter3.attackpower

    fight = 1
    while (fight == 1):
        print("you are in the fighting pits, three challengers are available to fight.\n\n" \
              + fighter1.name + " with life: " + str(fighter1.life) + " and attack power: " + str(
            fighter1.attackpower) + "  Gold value for winning: " + str(fighter1.goldvalue) + "g (input 1)\n" \
              + fighter2.name + " with life: " + str(fighter2.life) + " and attack power: " + str(
            fighter2.attackpower) + "  Gold value for winning: " + str(fighter2.goldvalue) + "g (input 2)\n" \
              + fighter3.name + " with life: " + str(fighter3.life) + " and attack power: " + str(
            fighter3.attackpower) + "  Gold value for winning: " + str(fighter3.goldvalue) + "g (input 3)\n")
        choice = int(input("Who will you fight?\n\nInput:"))
        if (choice == 1):
            result = fighting(fighter1,player)
            return result
        elif(choice == 2):
            result = fighting(fighter2,player)
            return result
        elif(choice == 3):
            result = fighting(fighter3,player)
            return result
        else:
            print("not a valid choice")
def main():
    player = Player()
    win = 0
    player.gold = 0
    player.name = input("what is your name?\n")
    print("Welcome to the Arena " + player.name + "!\nYou must fight in the arena until you can pay for your freedom with 100 gold.\n")

    while (win == 0):
        choice = idle(player)
        if (choice == 1):
            result = fight(player)
            player.fights = player.fights + 1
            player.totalfights = player.totalfights + 1
            player.stagger = 0
            if (player.fights >= 5):
                Enemy.life = Enemy.life + 1
                Enemy.attackpower = Enemy.attackpower + 2
                Enemy.difficulty = Enemy.difficulty + 1
                player.fights = 0
            if (result == -1):
                win = -1
        elif (choice == 3):
            win = 1

    if (win == 1):
        print("Congratulations! You WIN!\nYou finished with: " + str(player.gold) + " gold and " + str(player.life) + " life.")
    else:
        print("You died! You lose!")
play = 1
while (play == 1):  # Ability to restart the game
    main()
    play = int(input("1 to play again, anything else to quit."))