print("Welcome to Treasure Island!\n")
print("You have discovered a map with directions to an uncharted island, on the back of the map is a drawing which seems to be a landscape sketch of cavern, in the sketch is a X. Could this be hidden treasure or a fools errand?\nLThere's only one way to find out.\n")
print("You have some choices to make, this could be either your rise to riches or your demise.\n")
print("How will you fair!?\n")
choice1 = input("You arrive at the beach, there is fire smoke comming from over the trees to the right. To the left is a old watch tower. press R to head towards the smoke or L to climb the tower.\n").lower()

if choice1 == "L":
    choice2 = input("After you climb the tower, you survey the landscape, searching for any hints and to where this cavern could be.\nTo the left is what looks to be an old shipwreck graveyard with 10 or more ships from the days of legendary pirates.\nTo the right is a jungle, at its center is something large poking just above the canopy, as the sun beams down it reflects brightly.\nPress L to go to the ship graveyard and R to venture into the jungle.\n").lower()
    if choice2 == "R":
        choice3 = input("You finaly reach the structure which was poking above the canpoy, is an old stone statue of a man holding a spear, the tip is made entirely of bronze.\nBeneath the statue is a passage leading into a large cavern underground.\nThere are two paths, above the one on the right is a carved stone snake and on the left is a rat.\nPress R to enter the passage with the sanke above it or L to enter the passage with the Rat.\n").lower()
        if choice3 == "L":
            print("Congradulations, you made it to the hidden treasure of the island!\nYou uncovered the mounds of gold and jewels and now are richer than you ever though possible.\n")
            print('''         
                             __________
                            /\____;;___\.
                            | /        /
                            `. ())oo() .
                            |\(%()*^()^\.
                            | |-%-------|
                            \ | %  ))   |
                             \|%________| 
                ''')
        else:
            print("You see the opening to the cavern and quicken your step, in your hurry you failed to see the trap which opens up the floor and sends you to your death!\n")

    else:
        print("After climbing onto the shipwreck a large wave hits, which sends you flying off into the water only to find this area is a feeding ground for sharks!\nToday is not a pleasant one for you...")
else:
    print("You finaly reach the source of the smoke to find a primitve tribe all dancing around the fire, when they spot you they waste no time capturing, binding and throwing you into a cage.\nYou've been enslaved for the rest of your days.")
