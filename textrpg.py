# name: Ali Thursland
# date: 2019-11-11
# title: Text-based RPG

import dicts
import sys, time


Items = []
complete = False

def decide(choice1, choice2, output1, output2):
    print('\n\n - ' + choice1 + '\n\nor\n')
    print(' - ' + choice2 + '\n')
    while True:
        decision = input('Choose a path (1 or 2) \n')
        if decision == '1' or decision == '2':
            break
        elif decision.lower() == 'items':
            print()
            for x in Items:
                print(' - ' + x)
            print()
        else:
            print('Please use a number for your answer')
    if decision == '1':
        print(output1)
        return 1
    else:
        print(output2)
        return 2

#Main
def Main():
    welcome = "Welcome to Sloth Killerz Beta. Each character has a unique story. Beta version currently has only one game, but more games will be added as I feel like it. Typing 'items' will display a list of your current items in the story. Enjoy!"
    delay_print(welcome)
    time.sleep(2)
    print("\n\n*************************\nGame 1 -\n\nMain Character Bio  -\nName: " + dict1['Name'] + "\nAge: " + dict1['Age'] + "\nGender: "
    + dict1['Gender'] + "\n\nDescription -\nPersonality: " + dict1['Personality'] + "\nExtra: " + dict1['Extra']
    + "\n\nAlly Bio -\nName: " + dict1['Ally'] + "\nAlly age: " + dict1['Ally age'] + "\nAlly gender: " + dict1['Ally gender'] + "\n\nDescription -\nAlly personality: "
    + dict1['Ally personality'] + "\nAlly extra: " + dict1['Ally extra'] + "\n\nBackground -\n" + dict1['Background'] + "\n*************************")
    time.sleep(2)
    gameMode()

def Game1():
    Items.append("Bean")
    Items.append("Plastic water bottle filled with vodka")
    Items.append("$300 in fives")
    Items.append("Andrew's gun")
    time.sleep(2)
    delay_print("\n\nOkay, something really reeks. Are you going to check it out pussy?")
    num = decide('You are obliged to discover what the smell is', 'No comma thank you', '','')
    #Search out smell
    if num == 1:
        time.sleep(2)
        delay_print("You raise your head above the train seats and take a look at your surroundings, really taking it all in. You inhale deeply. It seems that there may be two culprits: the bathroom, immediately to your left, or the odd-looking wise woman with three eyes who has been staring at you for the past thirty minutes. Which will you approach?")
        num = decide('Bathroom. Maybe theres loot!', 'The only true wisdom is knowing that you know nothing. I must approach her.', '\nYou step out of your seat and pry open the bathroom doors, only to reveal...', '\nYou step away from your seat and slowly make your way over to the woman. Her stare is eternal.')
        #Bathroom
        if num == 1:
            time.sleep(2)
            delay_print("\nHoly cow! You found amorphophallus titanum, the corpse flower! No wonder it stinks so bad! You also find a bunch of dermestids, aka carcass-eating beetles, littered around the place. You pocket these bad boys immediately.")
            Items.append("Corpse flower")
            Items.append("Three dermestids")
            time.sleep(3)
            delay_print("\n\nAs sick as these fauna and flora may be, you smell like shit now. Everyone on the train is staring like you're an absolute madman. What do you do?")
            num = decide('Pry open the emergency exit and hop off this moving train', 'Do nothing, be uh oh stinky', '\nYou use you immense superhuman strength to rip open the train car doors. You make a leap of faith, only to find...', '')
            #Hop off train
            if num == 1:
                time.sleep(2)
                delay_print("\n...uh oh, you died. Everyone makes fun of your stupidity post-mortem.")
                tryAgain()
                complete = True
                return complete
                #
                #
                #END ROUTE

            #Do nothing
            else:
                time.sleep(2)
                delay_print("Kinda gross but whatever. The train car quickly empties out, though, and you spend the rest of the ride to Atlantic Terminal in solitude. Score!")
                time.sleep(5)
                delay_print("\n\n'Stand clear of the closing doors please!'")
                time.sleep(2)
                delay_print("\n\nOh fuck. You must have dozed off, and the train's about to pull out of the terminal. You quickly gather your insects and make your way off the car.")
                time.sleep(2)
                delay_print("\n\n'YOOOOOOOOOOOOOO!', a mystery brunette screeches in the distance.")
                time.sleep(2)
                delay_print("\n\nOh look, it's Jamie, here to meet you! What luck! You heard her distinctive 'yo' above the roar of the trains and cries of the babes!")
                time.sleep(2)
                delay_print("\n\n'Ali, you dumb fucking hoe, it's 7:45 and the doors opened to the concert already. We need to be there like YESTERDAY, dude.'")
                time.sleep(2)
                delay_print("\n\n'Ok cunt', you reply. Looks like time is the enemy tonight.")
                time.sleep(2)
                delay_print("\n\nThe Barclays Center is technically right above your heads, but still you decide to brainstorm faster ways to get there. Which route do you plan to take?")
                num = decide('Suite Life inspired air vent crawl','Take to the sewers','','')
                #Air vent crawl
                if num == 1:
                    time.sleep(2)
                    delay_print("\n\nYour cold, bloodied fingers pry open the nearest air vent and you two make your way inside. Jamie follows right behind.")
                    time.sleep(2)
                    delay_print("\n\n'Allison,' she begs, 'my dear Allison, do you have any concept of where we are going?'")
                    time.sleep(2)
                    delay_print("\n\n'...up?' you reply.")
                    time.sleep(2)
                    delay_print("\n\n'It's just... I don't know what you ate today dude, but... you keep ripping it and I literally think I might fucking pass out I am so sorry.'")
                    time.sleep(2)
                    delay_print("\n\nYou have no idea what this crazy bitch is talking about. You are anything BUT flatulent and such a ludicrous accusation is completely unfounded and probably an attempt by your enemies to unsettle your power. She must be treated as a threat from here on out.")
                    delay_print("\n\n'Eat my shit you fake Canadian moose-eating motherfucker!' You kick your legs back until she stops moving.")
                    time.sleep(2)
                    delay_print("\n\nOh wait - the corpse flower! That must be it! She wasn't crazy after all. Your long journey with it must have made you immune to the smell. You turn around to tell her you're sorry but realize you've killed her. \n\nYou can't live with the guilt so you turn yourself in, and end up getting 15-life at Riker's Island where you become the head of an illicit drug cartel. Someone sticks you four years in and you die, a badass, at 24 years old.")
                    time.sleep(2)
                    delay_print("\n\nA bright life cut far too short!")
                    tryAgain()
                    complete = True
                    return complete
                    #
                    #
                    #END ROUTE

                #Take to the sewers
                else:
                    time.sleep(2)
                    delay_print("\n\nThe two of you get out on Atlantic Ave and find a manhole to penetrate. After several unsuccessful tries at lifting it, you finally accomplish penetrating the man's hole with the help of a good samaritan on the street.")
                    time.sleep(2)
                    delay_print("\n\n'Thank you, ma'am!' you call after her. She turns around and waves. You realize now that it was the wise woman from the train. Life has a funny way of coming full circle like that, huh?")
                    time.sleep(2)
                    delay_print("\n\n'Here we fucking go' Jamie cries, and you both jump down into the underbelly of Kings County, New York.")
                    time.sleep(5)
                    delay_print("\n\n'...hello? Anybody down here?' you ask timidly. 'Fuck, Jamie, did we bring a flashlight?")
                    time.sleep(2)
                    delay_print("\n\n'Fuuuuuuuck. I should've asked Will to borrow his headlamp. What do we have on us that could serve as an unexpected source of light?'")
                    time.sleep(2)
                    delay_print("\n\n'Party mode on my juul?'")
                    time.sleep(2)
                    delay_print("\n\n'Lmao'")
                    time.sleep(2)
                    delay_print("\n\nYou acquire the bean from the bottom of your bag and wave it into the darkness. 'Lumos!' you cry, and the bean lights up, a prism of light streaking across the night. You always wanted to do that.")
                    time.sleep(2)
                    delay_print("\n\nAfter walking for a while, you approach a fork in the tunnel. To the left, a sign reads: 'To Barclays Center'. To the right, there is no sign, but there is a faint light in the distance and the smell of pizza wafting through the air. Which path do you choose?")
                    time.sleep(2)
                    num = decide('Theres no time left to fuck around. Lets take the left.','A sign? Pfft. An amateurish attempt to mislead you. Clearly the right fork is the way.','\n"I walk this lonely road... the only one that I have ever known..."','\n"I walk this lonely road... the only one that I have ever known...')
                    #Left fork
                    if num == 1:
                      #Win the game
                      time.sleep(2)
                      delay_print("\n\nBean in hand, you and Jamie tepidly make your way through the semi-flooded left passageway. After what feels like hours, but is really only about seven minutes, you reach a stairway-so tall it reaches up to the heavens. She takes the lead and you follow close behind, counting each step because you're crazy. You reach the top and are awash by a flood of light.")
                      time.sleep(2)
                      delay_print("\n\nLights. Cameras. Guitars, beers and naked babes everywhere. You've somehow made it BACKSTAGE to the Strokes concert! Wahoo! You and Jamie go on to have the best nights of your young lives. This is truly an adventure that you'll never forget.")
                      time.sleep(2)
                      tryAgain()
                      complete = True
                      return complete
                      #
                      #
                      #END ROUTE

                    #Right fork
                    else:
                      #TMNT
                      time.sleep(2)
                      delay_print("\n\nYou and Jamie both take a swig of your vodka before delving deep into the heart of the right fork in the tunnel. The smell of pizza grows ever stronger. A few hops, skips and jumps later, you find yourselves smack in the middle of a dojo-like underground lair, surrounded by four anthropomorphic turtles and their wise-looking rat teacher. Are these...?")
                      time.sleep(2)
                      delay_print("\n\n'THE TEENAGE MUTANT NINJA TURTLES!' Jamie cries. 'YOOOOOOO! Dudes, I am like, A HUGE fucking fan. Leonardo my dude what is UP?'")
                      time.sleep(2)
                      delay_print("\n\n'Jamie! SHUT THE FUCK UP dude no WE are big fans of YOU! Could you sign my shell man? Your outfits are like, crazy,' Leonardo said, gawking at the two beautiful women who appeared suddenly, like angels, in their top secret superhero lair.")
                      time.sleep(2)
                      delay_print("\n\n'Anything for you, Leonardo,' Jamie replied, taking a sharpie and drawing a dick on his back. You and Jamie giggled at each other. You cannot wait for him to see how much he jut got owned.")
                      time.sleep(2)
                      delay_print("")
                      Items.append("Slice of cold pizza")
                      time.sleep(2)
                      delay_print()
                      tryAgain()
                      complete = True
                      return complete



        #Old Woman
        else:
            time.sleep(2)
            delay_print("\n\nWait... is it a real third eye at all? It looks like makeup. You should've brought your eyedrops. Your contacts get so dry in the winter. Anyway, you approach the bitch. Turns out she's a cosplayer. But she gives you a neat Naruto dojinshi! Arigato, Kakashi-sensei!")
            Items.append("Naruto dojinshi")
            time.sleep(2)
            delay_print("\n\nIt looks like it might be hentai. You decide to read it anyway for the irony and then knock out for the rest of the train ride.")
            time.sleep(5)
            delay_print("\n\n'Stand clear of the closing doors please!'")
            time.sleep(5)
            delay_print("\n\n'Stand clear of the closing doors please!'")
            time.sleep(2)
            delay_print("\n\n'FUCK,' you cry.")
            delay_print("\nYou fell asleep. You're at Atlantic terminal and rush off the train with your things just in time to beat those damned closing doors.")
            time.sleep(2)
            delay_print("\n\n'YOOOOOOOOOOOOOO!', a mystery brunette screeches in the distance.")
            time.sleep(2)
            delay_print("\n\nOh look, it's Jamie, here to meet you! What luck! You heard her distinctive 'yo' above the roar of the trains and cries of the babes!")
            time.sleep(2)
            delay_print("\n\n'Ali, you dumb fucking hoe, it's 7:45 and the doors opened to the concert already. We need to be there like YESTERDAY, dude.'")
            time.sleep(2)
            delay_print("\n\n'Ok cunt', you reply. Looks like time is the enemy tonight.")
            time.sleep(2)
            delay_print("\n\nNEED TO FINISH THIS PATH. TRY ANOTHER FOR NOW!")
            tryAgain()
            complete = True
            return complete

    #Ignore it and hope it goes away
    else:
        time.sleep(2)
        delay_print("\nYou ignore it and hope it goes away, but alas... the fumes are too much for your weak, drunk body to handle. Sadly, you pass away just hours before seeing the band of your dreams. Jamie had a lot of fun without you.")
        time.sleep(2)
        delay_print("\n\nA bright life cut far too short!")
        tryAgain()
        complete = True
        return complete
        #
        #
        #END ROUTE

#try again helper function
def tryAgain():
  tryAgain = input('\n\nTry again? (Y to start over): \n\n')
  if tryAgain in ['y', 'Y', 'yes', 'Yes']:
    Main()
  else:
    sys.exit()

#for typing one letter at a time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

#gamemode helper function
def gameMode():
    while True:
        gameMode = input('\n\nType the number of the game you would like to play: ')
        if int(gameMode) == 1:
            Game1()
            break
        else:
            print('Game mode chosen is out of range')

Main()
