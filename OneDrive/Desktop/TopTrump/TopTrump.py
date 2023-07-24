import random
from datetime import time
from pprint import pprint
import random
import webbrowser
import requests


amountCards=2 #change value to test, usually 30
amountPlayers=2
deck_WildPokemon= []
deck_Player = []
pokemonNum = []


def random_pokemon():
    pokemon_number = random.randint(1, 153)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return{
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order'],
    }


def random_stat():
    random_number = random.randint(1, 4)
    if random_number == 1:
        stat = 'id'
    elif random_number == 2:
        stat = 'height'
    elif random_number == 3:
        stat = 'weight'
    else:
        stat = 'order'
    return stat

def splashScreen():
 print("**********************         WELCOME TO               *******************************")
print("                                                                          ")
print("""
==============                    ============
|              |                |               |                                                                                 
 ============            _.----.  ============       _.----.                                     
     \    \           _,-'       `.    \    \     _,-'       `.                               ___       ___     _.----.  
      \    \      __  \      __    \    \    \    \      __    \      _____          _____   |    \   /    |_,-'       `.
       \    \   ,' _`. \.    \ \   |     \    \    \.    \ \   |      \    \        /     /  |     \ /     |\      __    \  
        \    \ /  /   \ \    \/   /       \    \    \    \/   /-' ':   \    \      /     /   |             | \.    \ \   |
         \    |   \_/  | \     ,-'         \    \    \     ,-''''   \   \     \___/     /    |   |     |   |  \     \/   / 
          \    \      /   \    \            \    \    \    \    \    \   \             /     |   |\   /|   |   \     ,-'   
           \____`.__,'     \    \            \____\    \    \    \    \   '-._______.-'      |__ | \ / |   |    \    \ 
                            \    \                      \    \    \_.-'                                 '-.|     \    \         
                             \_.-'                       \_.-'                                                    \    \ 
                                                                                                                   \_.-'
                                    
               
""")
input("Press 'Start' when ever you see this: >")
Player_name=input(" hey Player enter your name")
print("Welcome",Player_name.format()," to the topTrump Game")



def menu():
    print("--------------")
    print("-----MENU-----")
print("--------------")

'''
while True:
     print("1. Play")
     print("2. How to play")
     print("3. Pokemon Lore in the games")
     print("4. About this Python Project")
     print("5. Exit")

menuSelection = input("\nPlease select an option using the number:")
if menuSelection == "1":
             numOfCardsForGame()
elif menuSelection == "2":
             howToPlay()
elif menuSelection == "3":
             pokemonLore()
elif menuSelection == "4":
             aboutPythonProject()
elif menuSelection == "5":
            print("...Bye then")
            input(">")
            quit()
else:
    print("Invalid Selection")
'''
def howToPlay():
        print("\n-------------")
        print("-How to Play-")
        print("-------------")
        print("""
    Aim of the Game:
    Win the game by catching all of the different types pokemon.
    Do this by fighting them. If you win the fight you will catch in a pokeball and be able to use them in future fights.
    If your pokemon loses a fight, you lose that pokemon and need to catch that type again.
    If you lose all of your pokemon, you lose the game.""")
        input(">")
        print("""
    Set Up:
    1.You select an even number of pokemon you wish to have in the game.
    2.Half of the pokemon are yours and the other half are in the wild.""")
        input(">")
        print("""
    Stages of the game are:
    1. You encounter wild pokemon
    2. You are given the option to research the pokemon
    3. You can choose to run away or fight. 
    3. You select one of the card's stats
    3. Another random card is selected for your opponent (the computer)
    4. The stats of the two cards are compared
    5. The player with the stat higher than their opponent wins""")
        input(">")


def pokemonLore():
        print("\n-------------")
        print("Pokemon  Lore")
        print("-------------")
        print("Pokemon means Pocket Monster...")
        input(">")


def aboutPythonProject():
        print("\n-------------")
        print("-The Project-")
        print("-------------")
        print("It's a Python program...")
        input(">")


def numOfCardsForGame():
        while True:
            try:
                amountCards = int(input("How many Pokemon do you want in the game?(Even numbers only)"))
                if amountCards % 2 == 0:
                    print(amountCards)
                    break

                else:
                    print("Invalid selection")
                    break
            except:
                print("Invalid selection")


        print("YOU ARE READY!\nCatch as many Pokemon as you can!")

        input(">")

def deal_cards(amountCards, amountPlayers):
            cardsPerPlayer = int(amountCards / amountPlayers)
            print(cardsPerPlayer)
            for x in range(cardsPerPlayer):
                x += 1
                cardDealt = random.choice(deck_WildPokemon)
                deck_Player.append(cardDealt)
                deck_WildPokemon.remove(cardDealt)
            displaypokemonremain()

def displaypokemonremain():
         print("---------------")
         print("YOU HAVE:", len(deck_Player), "POKEMON")
         print("YOU NEED:", len(deck_WildPokemon), "MORE POKEMON")
         print(input(">"))

def menu():
     print("--------------")
     print("-----MENU-----")
     print("--------------")

     print("1. Play")
     print("2. How to play")
     print("3. Pokemon Lore in the games")
     print("4. About this Python Project")
     print("5. Exit")
menu()

option = int(input('Enter your choice: '))
if option == 1:
    print('Handle option \'Option 1\'')
    numOfCardsForGame()

elif option == 2:
    print('Handle option \'Option 2\'')
    howToPlay()
elif option == 3:
    print('Handle option \'Option 3\'')
    pokemonLore()
elif option == 4:
    print('Thanks message before exiting')
    aboutPythonProject()

elif option ==5:
    print ("bye ")
    input(">")
    quit()
else:
    print('Invalid option. Please enter a number between 1 and 4.')


def my_round():
  player_name=input("Hey Player what is your Name ")
  print('hey',player_name,'Welcome to TopTrumps GAME :>')
my_score = 0
opponent_score = 0
random_pokemon_1 = random_pokemon()
random_pokemon_2 = random_pokemon()
random_pokemon_3 = random_pokemon()

print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'], random_pokemon_2['name'], random_pokemon_3['name']))
pokemon_choice = input('Which pokemon do you want to use? ')

if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3

print('Your stats are: id: {}, height: {}, weight: {}, order: {} '.format(my_pokemon['id'],my_pokemon['height'],my_pokemon['weight'],my_pokemon['order']))
stat_choice = input('Which stat do you want to use? (id, height, weight, order) ')

opponent_pokemon = random_pokemon()
print('The opponent chose {}'.format(opponent_pokemon['name']))

my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]
'''
if my_stat > opponent_stat:
    print((my_pokemon.name).upper(), 'WINS!')
    time.sleep(2)
    player_turn = True
    player_deck.append(cpu_current_card)
    cpu_deck.remove(cpu_current_card)
elif my_stat() < opponent_stat:
    print((cpu_current_card.name).upper(), 'WINS!')
    time.sleep(2)
    player_turn = False
    cpu_deck.append(current_card)
    player_deck.remove(current_card)
else:
    print('BOTH HEROS LIVE TO FIGHT ANOTHER DAY!')
    time.sleep(2)
'''



if my_stat > opponent_stat:
      #  print('You Win!')
        print ("")
        print ("")
        print ("##############")
        print ("###HAND WON###")
        print ("##############")
        print ("")
        print ("")
        my_score = my_score + 1
elif my_stat < opponent_stat:
     print("")
     print("")
     print("###############")
     print("###HAND LOST###")
     print('###############')
     print("")
     print("")
     opponent_score = opponent_score + 1

else:
     print('Draw!')
     print("The result of this round is: You {}, Opponent {} ".format(my_score, opponent_score))
     #return my_score, opponent_score


def opponent_round():

    my_score = 0
    opponent_score = 0

    random_pokemon_1 = random_pokemon()
    random_pokemon_2 = random_pokemon()
    random_pokemon_3 = random_pokemon()

    print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'], random_pokemon_2['name'], random_pokemon_3['name']))
    pokemon_choice = input('Which pokemon do you want to use? ')

    if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
    elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
    elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    opponent_stat_choice = random_stat()
    print('The opponent chose {} as their stat choice'.format(opponent_stat_choice))

    opponent_stat = opponent_pokemon[opponent_stat_choice]

    my_stat = my_pokemon[opponent_stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
        my_score = my_score + 1
    elif my_stat < opponent_stat:
        print('You Lose!')
        opponent_score = opponent_score + 1
    else:
        print('Draw!')

    print("The result of this round is: You {}, Opponent {} ".format(my_score, opponent_score))

    return my_score, opponent_score


def run():
    with open("scores.txt", "w+") as scores_file:

        scores_list = []

        for rounds in range(5):
            my_round_scores = my_round()
            opponent_round_scores = opponent_round()
            scores_list.append(my_round_scores)
            scores_list.append(opponent_round_scores)

        for score in scores_list:
            scores_file.write('(My Score, Opponent Score):' + '%s\n' % str(score))
        Valid = False
        while Valid == False:
            play_again = input("Would you like to play again?")
            if play_again == 'Yes' or play_again == 'yes' or play_again == 'y' or play_again == 'Y':
                game_started = False
                Valid = True
            elif play_again == 'No' or play_again == 'no' or play_again == 'n' or play_again == 'N':
                print("Thanks for playing!!")
                Valid = True
                continue
            else:

                print("Invalid input, please try again!")



splashScreen()
#menu()
run()
