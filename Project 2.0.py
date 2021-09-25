
class Player:  # creates individual players
    def __init__(self, name, playernum):
        """initialize instance of class"""
        self.name = name
        self.playernum = playernum
        self.active = False
        file1 = open("{}.csv".format(name), "w")
        file1.close()

    def getname(self):
        """return name of player, string"""
        return self.name

    def get_playernum(self):
        """return index of player, integer"""
        return self.playernum

    def printplayer(self):
        """prints player name and number"""
        print(self.playernum, self.name)

    def set_active(self):
        """sets players as active, boolean"""
        self.active = True

    def is_active(self):
        """tells if player is active"""
        return self.active


class Players:  # stores individual players in a list
    def __init__(self):
        """initialize instance of class"""
        self.players = []

    def add(self, name):
        """adds individual players to player list"""
        self.players.append(Player(name, len(self.players) + 1))

    def get_players(self):
        """returns list of players"""
        return self.players

    def printplayers(self):
        """prints list of players"""
        print('Players:')
        for i in self.players:
            i.printplayer()

    def activate_player(self, playernum):
        """activates player by playernum, returns activated player"""
        player = None
        for i in self.players:
            if playernum == i.get_playernum():
                i.set_active()
                player = i
                break
        return player

    def find_player(self, playernum):
        """find and return player by playernum"""
        player = None
        for i in self.players:
            if playernum == i.get_playernum():
                player = i
                break

        return player


def display_Main_Menu(players):
    """Creator: Rogelio. Will display the pokemon menu and parameters current pokemon and will have a default value
    of none returns list of the usernames """
    current_player = None
    players.printplayers()
    while current_player is None:
        playernum = int(input('Select a player number from the list: '))
        current_player = players.find_player(playernum)
        if current_player == None:
            print('That player was not found.  Try again.')
    print("--------------------------- MAIN MENU--------------------------- ")
    print("1. Display the options menu")
    print("2. Quit")
    pick_any = ''
    while pick_any != 2:
        try:
            pick_any = int(input("What option would you like to choose {}?:".format(current_player.getname())))
        except ValueError:
            print("Please enter an integer")
        if pick_any == 1:
            display_Option_Menu(players)
            break
    if pick_any == 2:
        print("Thanks for playing!")

    return players


def current_users():
    """Creates a list of the new users as the game starts, there are no parameters and the
    function returns a list of the usernames for use later. """
    print('Welcome to Pokemon: Gotta Catch \'em All!')
    print("First things first you need to enter the amount of people that will be playing.")
    print("If you want to add in a player, type in a 'y' and then the name of the user in the following prompt.")
    print("To stop adding players type in an 'n'.")
    players = Players()
    player_input = input('Do you want to add a player? (y/n) ')
    while player_input.lower() == 'y':
        newplayername = input('Enter PLayer Name: ')
        players.add(newplayername)  # players added to list
        player_input = input('Do you want to add a player? (y/n) ')
    while player_input.lower() not in {'y','n'}:
        print("Please either type in a 'y' or a 'n'.")
        player_input = input('Do you want to add a player? (y/n) ')
    if player_input.lower() == 'n':
        return players



def display_Current_Pokemon(poke_user):
    """
    Displays the list of all pokemon and the selected pokemon. Will use a list of pokemon as the only parameter."""
    print("--------------------------- Pokemon Selection Menu ---------------------------")
    poke_list = []
    file_path = "{}.csv".format(poke_user.getname())
    if os.stat(file_path).st_size != 0:   # Tests if file is empty
        with open('{}.csv'.format(poke_user.getname()), 'r') as pokeFile:
            pokeReader = csv.reader(pokeFile, delimiter=",")
            for row in pokeReader:
                poke_list.append(row)
        for i in range(len(poke_list)):
            print("{}. {}".format(i + 1, poke_list[i][1]))
            print("Pokemon level - {}".format(poke_list[i][-1]))
            print("Current candies - {}".format(poke_list[i][-2]))
            print("Current Cp - {}".format(poke_list[i][2]))
            print()
        return True
    else:
        print("User {} does not own any pokemon".format(poke_user.getname()))
        return False


def display_Option_Menu(players):
    """
    Will display current options and prompt users to pick the option they want to do. Takes in list of players as parameter"""
    current_player = None
    players.printplayers()
    while current_player is None:
        try:
            playernum = int(input('Select a player number from the list: '))
            current_player = players.find_player(playernum)
            if current_player == None:
                print('That player was not found. Try again.')
        except ValueError:
            print('Please enter and integer.')
    option_tables()
    option = ''
    while option != 7:
            option = int(input("What would you like to do (Enter a number):"))
            while option not in {1, 2, 3, 4, 5, 6, 7}:
                option = int(input("Please enter a valid number, 1, 2, 3, 4, 5, 6, or 7:"))
            pokemon = None
            # If statements calling the different functions in the game
            if option == 1:
                get_Starter(current_player)
                option_tables()
            elif option == 2:
                catch_Pokemon(current_player)
                option_tables()
            elif option == 3:
                pokemon_Battle(players)
                option_tables()
            elif option == 4:
                pokemon_LevelUp(current_player, l)
                option_tables()
            elif option == 5:
                current_player = switch_users(players)
                option_tables()
            elif option == 6:
                pokemon = select_Pokemon(current_player)
                option_tables()
            l = pokemon

    print("Thanks For Playing!")


def option_tables():
    """
    Displays the basic options the user can pick from, no parameters or return values."""
    print(" --------------------------- Options Menu --------------------------")
    options = ['Get Starter', 'Catch Pokemon', 'Battle', 'Level up', 'Switch User', 'Select Pokemon',
               'Stop Playing']
    for i in range(7):
        print('|' + "{:>28}. {:<15}".format(i + 1, options[i]) + "|".rjust(23))
    print(" -------------------------------------------------------------------")


def switch_users(players):
    """
    Takes in the parameter of the list of all the users to then ask the user to input the name of the user they
    want to select, returns the string value of the selected user. """
    current_player = None
    players.printplayers()
    while current_player is None:
        playernum = int(input('Select a player number from the list: '))
        current_player = players.find_player(playernum)
        if current_player == None:
            print('That player was not found.  Try again.')
    return current_player


def get_Starter(player):
    """
    Gets starter pokemon from the given csv file returns list of pokemon information, the parameter is a string of
    the user and if the users file is empty the function returns a list of the data of the obtained pokemon. """
    i = 0
    file_path = "{}.csv".format(player.getname())
    if os.stat(file_path).st_size == 0:   # Tests for empty file
        with open("PokeList(1).csv", 'r') as pokeFile:
            pokeReader = csv.reader(pokeFile, delimiter=',')
            chooser = random.randint(2, 150)
            for lines in pokeReader:
                i += 1
                if i == chooser:
                    starter = lines
        level = 1
        candies = random.choice([1, 3, 5, 10])   # Gives pokemon an assigned candy value
        starter.append(candies)
        starter.append(level)
        print("You earned a {}".format(starter[1]))
        with open("{}.csv".format(player.getname()), "a", newline='') as user_file:
            pokeWriter = csv.writer(user_file, delimiter=",")
            pokeWriter.writerow(starter)
        return starter
    else:
        print("The user cannot recive a starter as they already own a pokemon.")


def pokemon_LevelUp(player, pokemon=None):
    """
    Modifies the selected pokemon level based on current level and amount of candies, parameter for user and
    pokemon selected defaulted as none to deal with case no pokemon was selected, returns updated list of pokemon data. """
    if pokemon == None:
        print('First select which pokemon you want to level up.')
        pokemon = select_Pokemon(player)

    if pokemon is not None:
        candies = int(pokemon[4])
        p_list = []
        if (candies >= 1) and (int(pokemon[-1]) <= 30):
            pokemon[-1] = int(pokemon[-1]) + 1
            candies -= 1
            pokemon[4] = candies
            pokemon[2] = int(pokemon[2]) + (int(pokemon[2]) * 0.0094) / (0.095 * sqrt(int(pokemon[-1]) - 1))
            pokemon[2] = int(pokemon[2])
            if pokemon[2] > int(pokemon[3]):
                pokemon[2] = pokemon[3]
            with open("{}.csv".format(player.getname()), "r") as copyfile:
                preader = csv.reader(copyfile, delimiter=',')
                for row in preader:
                    if pokemon[1] not in row:
                        p_list.append(row)
            with open("{}.csv".format(player.getname()), "w", newline='') as dfile:
                dreader = csv.writer(dfile, delimiter=',')
                dreader.writerow(pokemon)
                for i in p_list:
                    dreader.writerow(i)
            print("New Pokemon Stats for {}".format(pokemon[1]))
            print("New Level - {}".format(pokemon[-1]))
            print("New Cp - {}".format(pokemon[2]))
            print("New Candy Amount - {}".format(pokemon[4]))
            return pokemon
        elif (candies >= 2) and (31 <= int(pokemon[-1]) <= 40):
            pokemon[-1] = int(pokemon[-1]) + 1
            candies -= 2
            pokemon[4] = candies
            pokemon[2] = int(pokemon[2]) + (int(pokemon[2]) * 0.0045) / (0.095 * sqrt(int(pokemon[-1]) - 1))
            pokemon[2] = int(pokemon[2])
            with open("{}.csv".format(player.getname()), "r") as copyfile:
                preader = csv.reader(copyfile, delimiter=',')
                for row in preader:
                    if pokemon[1] not in row:
                        p_list.append(row)
            with open("{}.csv".format(player.getname()), "w", newline='') as dfile:
                dreader = csv.writer(dfile, delimiter=',')
                dreader.writerow(pokemon)
                for i in p_list:
                    dreader.writerow(i)
            print("New Pokemon Stats for {}".format(pokemon[1]))
            print("New Level - {}".format(pokemon[-1]))
            print("New Cp - {}".format(pokemon[2]))
            print("New Candy Amount - {}".format(pokemon[4]))
            return pokemon

        elif pokemon[-1] == 40:
            print("{} is max level already.".format(pokemon[1]))

        else:
            print("There are not enough candies to level up {}.".format(pokemon[1]))


def select_Pokemon(player):
    """
    Picks an active pokemon to use in battle to level up etc…, parameter of pokemon list, will call the
    display_Option_Menu() and ask the user to pick a pokemon. Returns the currently picked pokemon """
    x1 = display_Current_Pokemon(player)  # Calls previously made function for user display
    if not x1:
        print("Catch a pokemon first")
    elif x1:
        pokedata = []
        total_candies = []
        with open("{}.csv".format(player.getname()), "r") as lfile:
            lreader = csv.reader(lfile, delimiter=',')
            for row in lreader:
                pokedata.append(row)
        poke_picker = int(input("Which pokemon do you want to pick(Enter a number):"))
        if poke_picker == 1:
            return pokedata[0]
        elif poke_picker == 2:
            return pokedata[1]
        elif poke_picker == 3:
            return pokedata[2]
        elif poke_picker == 4:
            return pokedata[3]
        elif poke_picker == 5:
            return pokedata[4]
        elif poke_picker == 6:
            return pokedata[5]
        elif poke_picker == 7:
            return pokedata[6]
        elif poke_picker == 8:
            return pokedata[7]


def pokemon_Battle(players):
    """
    Will begin a battle between the two players when prompted, parameter is the list of the two users,
    no return value. """
    player1 = None
    player2 = None

    players.printplayers()

    # choose active players
    while player1 == None:
        p1 = int(input('Choose player 1 by entering player number: '))
        player1 = players.activate_player(p1)
        if player1 == None:
            print('Pick a valid player from the list.')
    while player2 == None:
        p2 = int(input('Choose player 2 by entering player number: '))
        player2 = players.activate_player(p2)
        if player2 == None:
            print('Pick a valid player from the list.')

    pokeList = []
    p1_list = []
    p2_list = []

    # Creates copies of existing files to use for battle files
    with open("{}.csv".format(player1.getname()), "r") as BattleFile:
        battleReader = csv.reader(BattleFile, delimiter=",")
        for rows in battleReader:
            rows.append(100)
            pokeList.append(rows)
    with open("{}Battle.csv".format(player1.getname()), "w", newline='') as BattleData:
        battleWriter = csv.writer(BattleData, delimiter=",")
        for row in pokeList:
            battleWriter.writerow(row)
    p1_list = pokeList[:]
    pokeList = []
    with open("{}.csv".format(player2.getname()), "r") as BattleFile:
        battleReader = csv.reader(BattleFile, delimiter=",")
        for rows in battleReader:
            rows.append(100)
            pokeList.append(rows)
    p2_list = pokeList[:]
    with open("{}Battle.csv".format(player2.getname()), "w", newline='') as BattleData:
        battleWriter = csv.writer(BattleData, delimiter=",")
        for row in pokeList:
            battleWriter.writerow(row)
    x = select_Pokemon(player1)
    y = select_Pokemon(player2)
    x.append(100)
    y.append(100)
    fainted_p1 = 0
    fainted_p2 = 0
    health = float(x[-1])
    health2 = float(y[-1])
    num1 = len(p1_list)
    num2 = len(p2_list)

    while (fainted_p1 != len(p1_list)) and (fainted_p2 != len(p2_list)):
        k = False
        v = False
        health = float(x[-1])
        health2 = float(y[-1])
        while (health > 0) and (health2 > 0):
            p1 = battle_options(player1.getname())
            pokes = []
            if p1 == 1:
                k = pokemon_Attack(player1.getname(), player2.getname(), x, y)

                if k:
                    break
            elif p1 == 2:
                x = pokemon_Heal(player1.getname(), x)
            elif p1 == 3:
                x = select_Battle_Pokemon(player1)

            p2 = battle_options(player2.getname())
            pokes = []
            if p2 == 1:
                v = pokemon_Attack(player2.getname(), player1.getname(), y, x)
                if v:
                    break
            elif p2 == 2:
                y = pokemon_Heal(player2.getname(), y)
            elif p2 == 3:
                y = select_Battle_Pokemon(player2)

        if v:
            fainted_p1 += 1
            if fainted_p1 != num1:
                print("Player '{}' must select a new pokemon".format(player1.getname()))
                x = select_Battle_Pokemon(player1)
        elif k:
            fainted_p2 += 1
            if fainted_p2 != num2:
                print("Player '{}' must select a new pokemon".format(player2.getname()))
                y = select_Battle_Pokemon(player2)
        if fainted_p1 == num1:
            print('{} wins!'.format(player2.getname()))
            print("Each of your pokemon have been awarded 5 candies!")
            data = []
            with open('{}.csv'.format(player2.getname()), 'r') as winFile:
                preader = csv.reader(winFile, delimiter= ',')
                for i in preader:
                    data.append(i)
            for i in data:
                new_candies = int(i[4]) + 5
                i[4] = str(new_candies)
            with open('{}.csv'.format(player2.getname()), 'w') as winFile:
                pwriter = csv.writer(winFile, delimiter=',')
                for i in data:
                    pwriter.writerow(i)
            print("Congratulations!")
        elif fainted_p2 == num2:
            print('{} wins!'.format(player1.getname()))
            print("Each of your pokemon have been awarded 5 candies!")
            data = []
            with open('{}.csv'.format(player1.getname()), 'r') as winFile:
                preader = csv.reader(winFile, delimiter=',')
                for i in preader:
                    data.append(i)
            for i in data:
                new_candies = int(i[4]) + 5
                i[4] = str(new_candies)
            with open('{}.csv'.format(player1.getname()), 'w') as winFile:
                pwriter = csv.writer(winFile, delimiter=',')
                for i in data:
                    pwriter.writerow(i)
            print("Congratulations!")

def display_Battle_Pokemon(player):
    """
    Displays the list of all pokemon and the selected pokemon of the parameter of the user string. Will use a list
    of pokemon as the only parameter. """
    print("--------------------------- Battle Pokemon Selection Menu for {}---------------------------".format(
        player.getname()))
    poke_list = []
    file_path = "{}Battle.csv".format(player.getname())
    if os.stat(file_path).st_size != 0:   # Checks for empty file
        with open('{}Battle.csv'.format(player.getname()), 'r') as pokeFile:
            pokeReader = csv.reader(pokeFile, delimiter=",")
            for row in pokeReader:
                poke_list.append(row)
        for i in range(len(poke_list)):
            print("{}. {}".format(i + 1, poke_list[i][1]))
            print("Pokemon level - {}".format(poke_list[i][5]))
            print("Current HP - {}".format(poke_list[i][-1]))
            print()
    else:
        print("User {} does not own any pokemon".format(player.getname()))


def select_Battle_Pokemon(player):
    """
    Picks an active pokemon to use in battle to level up etc…, parameter of pokemon list, will call the
    display_Option_Menu() and ask the user to pick a pokemon. Returns the currently picked pokemon """
    display_Battle_Pokemon(player)
    pokedata = []
    total_candies = []
    with open("{}Battle.csv".format(player.getname()), "r") as lfile:
        lreader = csv.reader(lfile, delimiter=',')
        for row in lreader:
            pokedata.append(row)
        if len(pokedata) == 0:
            print("Catch a pokemon first.")
        else:
            pokemon_found = False
        while pokemon_found == False:
            poke_picker = int(input("Which pokemon do you want to pick(Enter a number):"))
            if (poke_picker > 0) and (poke_picker <= len(pokedata)):
                pokemon_found = True
            else:
                print('You did not enter a valid pokemon. Please try again.')

    return pokedata[poke_picker - 1]


def battle_options(playername):
    """
    Displays a list of battle options for the user to pick from with an input statement, takes in parameter of the
    user as a string and returns their choice. """
    print("---------- Battle Options for {} -----------".format(playername))
    print("| 1. Attack\n")
    print("| 2. Heal\n")
    print("| 3. Switch pokemon\n")
    choice = int(input("What do you want to do?:"))
    return choice


def pokemon_Attack(playername, opponent, user_pokemon, opp_pokemon):
    """
    Takes in parameters of the user and opponent names as strings and the lists of the opponents and users pokemon
    to Allows the selected pokemon to attack in battle, Returns True if opponent pokemon has an HP value of 0,
    otherwise the funciton returns False. """

    health = float(opp_pokemon[-1])
    damage = 10 * float(user_pokemon[5]) + (0.1 * float(user_pokemon[2]))   # Random battle damage based on level and CP
    health -= damage
    opp_pokemon[-1] = str(health)
    print('{} attacked {} and dealt {} damage'.format(user_pokemon[1], opp_pokemon[1], damage))
    if health <= 0:
        health = 0
    print("{}'s new health is {}".format(opp_pokemon[1], health))
    fainted2 = False
    if float(opp_pokemon[-1]) <= 0:   # Conditional statement to see if pokemon fainted
        pokes = []
        fainted2 = True
        print("{} fainted!".format(opp_pokemon[1]))
        with open('{}Battle.csv'.format(opponent), "r") as cfile:
            hreader = csv.reader(cfile, delimiter=",")
            for row in hreader:
                if opp_pokemon[1] not in row:
                    pokes.append(row)
        with open('{}Battle.csv'.format(opponent), "w", newline='') as xfile:
            xwriter = csv.writer(xfile, delimiter=',')
            for row in pokes:
                xwriter.writerow(row)
        return True
    pokes = []
    with open('{}Battle.csv'.format(opponent), "r") as bfile:
        hreader = csv.reader(bfile, delimiter=",")
        for row in hreader:
            if opp_pokemon[1] not in row:
                pokes.append(row)
    with open('{}Battle.csv'.format(opponent), "w", newline='') as nfile:
        hwriter = csv.writer(nfile, delimiter=",")
        if float(opp_pokemon[-1]) > 0:
            hwriter.writerow(opp_pokemon)
        for row in pokes:
            hwriter.writerow(row)


def pokemon_Heal(playername, pokemon):
    """
    Takes in the parameters of the pokemon and the owner of the pokemon in order to randomly assign a heal value
    to the given pokemons HP. The function returns the updated list of pokemon information. """
    current_health = float(pokemon[-1])
    heal_value = random.choice([20, 40, 60])
    new_health = current_health + heal_value
    if new_health > 100:
        new_health = 100
    print("{} was healed to {}".format(pokemon[1], new_health))
    pokemon[-1] = str(new_health)
    return pokemon


def comp_winner(cpus_spaces):
    """
    Algorithms to determine the winner of the tic-tac-toe mini game. Returns true if any one of the combinations
      is found in the owned_spaces parameter which is a list of the spaces claimed by the cpu. """
    if (7 in cpus_spaces) and (8 in cpus_spaces) and (9 in cpus_spaces):
        return True
    elif (4 in cpus_spaces) and (5 in cpus_spaces) and (6 in cpus_spaces):
        return True
    elif (1 in cpus_spaces) and (2 in cpus_spaces) and (3 in cpus_spaces):
        return True
    elif (1 in cpus_spaces) and (4 in cpus_spaces) and (7 in cpus_spaces):
        return True
    elif (2 in cpus_spaces) and (5 in cpus_spaces) and (8 in cpus_spaces):
        return True
    elif (3 in cpus_spaces) and (6 in cpus_spaces) and (9 in cpus_spaces):
        return True
    elif (1 in cpus_spaces) and (5 in cpus_spaces) and (9 in cpus_spaces):
        return True
    elif (3 in cpus_spaces) and (5 in cpus_spaces) and (7 in cpus_spaces):
        return True
    else:
        return False


def user_winner(owned_spaces):
    """
    Algorithms to determine the winner of the tic-tac-toe mini game. Returns true if any one of the combinations
    is found in the owned_spaces parameter which is a list of the spaces claimed by the user. """
    if (7 in owned_spaces) and (8 in owned_spaces) and (9 in owned_spaces):
        return True
    elif (4 in owned_spaces) and (5 in owned_spaces) and (6 in owned_spaces):
        return True
    elif (1 in owned_spaces) and (2 in owned_spaces) and (3 in owned_spaces):
        return True
    elif (1 in owned_spaces) and (4 in owned_spaces) and (7 in owned_spaces):
        return True
    elif (2 in owned_spaces) and (5 in owned_spaces) and (8 in owned_spaces):
        return True
    elif (3 in owned_spaces) and (6 in owned_spaces) and (9 in owned_spaces):
        return True
    elif (1 in owned_spaces) and (5 in owned_spaces) and (9 in owned_spaces):
        return True
    elif (3 in owned_spaces) and (5 in owned_spaces) and (7 in owned_spaces):
        return True
    else:
        return False


def tic_tac_toe():
    """
    Prints a display of the current tic tac toe board for the first mini-game. No parameters and it returns True
    only if the winner is the user otherwise it returns False """
    c1 = 1
    c2 = 2
    c3 = 3
    c4 = 4
    c5 = 5
    c6 = 6
    c7 = 7
    c8 = 8
    c9 = 9
    print("The game is simple, Tic-Tac-Toe you vs the computer:")
    print("Here is the tic tac toe board:")
    print("1 | 2 | 3\n"
          "----------\n"
          "4 | 5 | 6\n"
          "-----------\n"
          "7 | 8 | 9")
    print("You will represent 'x' and the computer will represent 'y'\n")

    user_move = int(input("Where would you like to mark first(pick one of the numbers)"))
    used_spaces = [user_move]
    user_spaces = [user_move]
    if user_spaces[-1] == c1:
        c1 = 'x'
    elif user_spaces[-1] == c2:
        c2 = 'x'
    elif user_spaces[-1] == c3:
        c3 = 'x'
    elif user_spaces[-1] == c4:
        c4 = 'x'
    elif user_spaces[-1] == c5:
        c5 = 'x'
    elif user_spaces[-1] == c6:
        c6 = 'x'
    elif user_spaces[-1] == c7:
        c7 = 'x'
    elif user_spaces[-1] == c8:
        c8 = 'x'
    elif user_spaces[-1] == c9:
        c9 = 'x'
    computer_list = []
    computer_move = 0
    while (len(used_spaces) <= 8) and (comp_winner(computer_list) == False) and (user_winner(user_spaces) == False):
        computer_move = random.randint(1, 9)
        if computer_move not in used_spaces:
            used_spaces.append(computer_move)
            computer_list.append(computer_move)
            if computer_list[-1] == c1:
                c1 = 'o'
            elif computer_list[-1] == c2:
                c2 = 'o'
            elif computer_list[-1] == c3:
                c3 = 'o'
            elif computer_list[-1] == c4:
                c4 = 'o'
            elif computer_list[-1] == c5:
                c5 = 'o'
            elif computer_list[-1] == c6:
                c6 = 'o'
            elif computer_list[-1] == c7:
                c7 = 'o'
            elif computer_list[-1] == c8:
                c8 = 'o'
            elif computer_list[-1] == c9:
                c9 = 'o'
        elif computer_move in used_spaces:
            while computer_move in used_spaces:
                computer_move = random.randint(1, 9)
            used_spaces.append(computer_move)
            computer_list.append(computer_move)
            if computer_list[-1] == c1:
                c1 = 'o'
            elif computer_list[-1] == c2:
                c2 = 'o'
            elif computer_list[-1] == c3:
                c3 = 'o'
            elif computer_list[-1] == c4:
                c4 = 'o'
            elif computer_list[-1] == c5:
                c5 = 'o'
            elif computer_list[-1] == c6:
                c6 = 'o'
            elif computer_list[-1] == c7:
                c7 = 'o'
            elif computer_list[-1] == c8:
                c8 = 'o'
            elif computer_list[-1] == c9:
                c9 = 'o'
        if comp_winner(computer_list):
            break

        print("This is the current board.")
        print("{} | {} | {}"
              "\n{} | {} | {}"
              "\n{} | {} | {}".format(c1, c2, c3, c4, c5, c6, c7, c8, c9))
        user_move = int(input("Where would you like to mark next(pick one of the numbers)"))
        if user_move not in used_spaces:
            used_spaces.append(user_move)
            user_spaces.append(user_move)
            if user_spaces[-1] == c1:
                c1 = 'x'
            elif user_spaces[-1] == c2:
                c2 = 'x'
            elif user_spaces[-1] == c3:
                c3 = 'x'
            elif user_spaces[-1] == c4:
                c4 = 'x'
            elif user_spaces[-1] == c5:
                c5 = 'x'
            elif user_spaces[-1] == c6:
                c6 = 'x'
            elif user_spaces[-1] == c7:
                c7 = 'x'
            elif user_spaces[-1] == c8:
                c8 = 'x'
            elif user_spaces[-1] == c9:
                c9 = 'x'
        else:
            while user_move in used_spaces or (user_move < 0) or (user_move > 9):
                user_move = int(input("Please select an available space"))
            user_spaces.append(user_move)
            used_spaces.append(user_move)
            if user_spaces[-1] == c1:
                c1 = 'x'
            elif user_spaces[-1] == c2:
                c2 = 'x'
            elif user_spaces[-1] == c3:
                c3 = 'x'
            elif user_spaces[-1] == c4:
                c4 = 'x'
            elif user_spaces[-1] == c5:
                c5 = 'x'
            elif user_spaces[-1] == c6:
                c6 = 'x'
            elif user_spaces[-1] == c7:
                c7 = 'x'
            elif user_spaces[-1] == c8:
                c8 = 'x'
            elif user_spaces[-1] == c9:
                c9 = 'x'

    print("{} | {} | {}"
          "\n{} | {} | {}"
          "\n{} | {} | {}".format(c1, c2, c3, c4, c5, c6, c7, c8, c9))
    if user_winner(user_spaces):
        return True
    elif comp_winner(computer_list):
        return False
    else:
        return False


def betting_game():
    """
    Betting mini-game designed to be played when users want to catch new pokemon, returns either a True or False,
    no parameters """
    print("Welcome to the blackjack betting game!")
    print("Your job is to guess within 2 numbers of the computers random draw of two cards.")
    print("For example... if the cpu draws a 10 and a 5 and the user guesses 16 they win otherwise they lose.")
    print("Jokers are excluded and Aces are worth one.")
    cpu_total = 0
    for i in range(2):
        cpu_total += random.randint(1, 10)

    guess = int(input("\nWhat is your guess?:"))

    if cpu_total - 2 <= guess <= cpu_total + 2:
        return True
    else:
        return False


def catch_Pokemon(player):
    """
    Prompts the user with mini game in order to catch pokemon will be called from the display_Option_Menu()
    function and will use the random module to determine which game that the user will play """
    list_length = []
    with open("{}.csv".format(player.getname()), "r") as ffile:
        lre = csv.reader(ffile, delimiter=",")
        for row in lre:
            list_length.append(row)
    while len(list_length) < 8:
        print("In order to catch a pokemon, you must win a game of tic tac toe vs the cpu!")
        print("\nFirst of all we you need to decide if you want a hard game or an easy game.")
        print("The harder game gives you a higher chance at a higher level pokemon than the easy game does.")
        game = int(input("\nPress 1 for an easy game and 2 for a hard game:\n"))
        pokeData = []
        if game == 1:
            i = 0
            if tic_tac_toe():
                with open("PokeList(1).csv", 'r') as pokeFile:
                    pokeReader = csv.reader(pokeFile, delimiter=',')
                    chooser = random.randint(2, 150)
                    for lines in pokeReader:
                        i += 1
                        if i == chooser:
                            pokeData = lines
                            level = 1
                            candies = random.choice([1, 3, 5, 10])
                            pokeData.append(candies)
                            pokeData.append(level)
                print("You Win!\nYou caught a {}".format(pokeData[1]))
                with open('{}.csv'.format(player.getname()), "a", newline='') as pokedexs:
                    pokedexer = csv.writer(pokedexs, delimiter=",")
                    pokedexer.writerow(pokeData)

            else:
                print("You Failed!")
        elif game == 2:
            x1 = betting_game()
            multiplier = random.randint(1, 2)
            if multiplier == 1:
                multiplier = True
            elif multiplier == 2:
                multiplier = False
            if (x1 == True) and (multiplier == False):
                i = 0
                with open("PokeList(1).csv", 'r') as pokeFile:
                    pokeReader = csv.reader(pokeFile, delimiter=',')
                    chooser = random.randint(2, 150)
                    for lines in pokeReader:
                        i += 1
                        if i == chooser:
                            pokeData = lines
                            level = 1
                            candies = random.choice([1, 3, 5, 10])
                            pokeData.append(candies)
                            pokeData.append(level)
                print("You win!\nYou caught a {}".format(pokeData[1]))
                with open('{}.csv'.format(player.getname()), "a") as pokedexs:
                    pokedexer = csv.writer(pokedexs, delimiter=",")
                    pokedexer.writerow(pokeData)

            elif (x1 == True) and (multiplier == True):
                possible_list = []
                i = 0
                with open("PokeList(1).csv", 'r') as pokeFile:
                    pokeReader = csv.reader(pokeFile, delimiter=',')
                    for lines in pokeReader:
                        if (i > 0) and (int(lines[2]) >= 300):
                            possible_list.append(lines)
                        i += 1
                chooser = random.randint(0, len(possible_list))
                pokeData = possible_list[chooser]
                candies = random.choice([1, 3, 5, 10])
                level = 1
                pokeData.append(candies)
                pokeData.append(level)
                print("You win!\nYou caught a {}".format(pokeData[1]))
                with open('{}.csv'.format(player.getname()), "a") as pokedexs:
                    pokedexer = csv.writer(pokedexs, delimiter=",")
                    pokedexer.writerow(pokeData)
            else:
                print("You Failed!")
        return pokeData
    if len(list_length) >= 8:
        print("You have the maximum amount of pokemon")



x = current_users()
display_Main_Menu(x)
