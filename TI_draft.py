import random

#  File Handling: Open the text files that list the factions associated with expansions and beginner games
beginner_file=open('beginnerfactions.txt', encoding="utf8")
core_file=open('corefactions.txt', encoding="utf8")
pok_file=open('pokfactions.txt', encoding="utf8")

# Create the list that we'll add the assignable factions
factions=[]

# Function to draft factions for each player
def draft_factions(factions,num_players,factions_dealt):
    i = 0
    while i < num_players:
        j = 0
        i+=1
        player_string = "Player " + str(i) + ":"
        player_factions = []
        while j < factions_dealt:
            j+=1
            selected_faction = random.choice(factions)
            factions.remove(selected_faction)
            player_factions.append(selected_faction)
        print(player_string + str(player_factions))

# Builds the factions set by parsing user input
# todo: there's a couple of funcationable things here
while True:
    beginner_game =  input("Is this a beginner game? (Y/N)")
    if beginner_game.lower() not in ('y', 'yes', 'no', 'n'):
        print("Not a valid choice")
        continue
    else:
        break

# Adds the beginner factions to the set, assumed that new players only use the base game
if beginner_game.lower() in ('y','yes'):
    beginner_game = True
    for line in beginner_file:
        for word in line.splitlines():
            factions.append(word)

# Asks whether the players are using Prophecy of Kings
else:
    beginner_game = False
    while True:
        expansion_game = input("Are you using the Prophecy of Kings expansion? (Y/N)")
        if expansion_game.lower() not in ('y', 'yes', 'no', 'n'):
            print("Not a valid choice")
            continue
        else:
            break
    if expansion_game.lower() in ('y','yes'):
        expansion_game = True
        for line in pok_file:
            for word in line.splitlines():
                factions.append(word)
    else:
        expansion_game = False

# Adds the core factions to the set regardless
    for line in core_file:
        for word in line.splitlines():
            factions.append(word)

# Let's get the number of players and check the value for correctness based on whether it's a beginner game or not
while True:
    try:
        num_players = int(input("How many players are there? (3-8)"))
    except ValueError:
        print("Not a valid choice, please enter an integer between 3 and 8")
        continue

    if num_players < 3 or num_players > 8 or (num_players > 6 and beginner_game):
        print("Not a valid choice, please enter an integer between 3 and 8 or 6 players max for a beginner game")
        continue
    else:
        # player count was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break

# Work out the number of factions dealt to each player based on the following
# If it's a beginner game, each player will be dealt a single faction from the reduced list
# If it's not, each player will be dealt the maximum number of factions possbile to get the
if beginner_game:
    factions_dealt = 1
else:
    factions_dealt = int(len(factions)//num_players)

# Call the earlier defined function that does the drafting
draft_factions(factions,num_players,factions_dealt)