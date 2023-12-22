import random

def game_start(): # startet das spiel
    print("Welcome to Black Jack")
    start = input("Type 'Start' to begin: ")
    if start == "start" or start == "Start":
        player_result()
    else:
        print("ERROR. You had one Job...")

Jack = 10 # definiert die ganzen karten
Queen = 10
King = 10
Ace = 11

buster = 0 # damit buster global funktioniert


def player_turn(): # zieht für den Spieler die Karten
    return random.choice([2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace])


def dealer_turn(): # zieht für den Dealer die Karten
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace])

first_draw = player_turn() # Macht das erste ziehen und setzt die extra Regel für den Ass um
second_draw = player_turn()
if second_draw == Ace:
    ace_answer = int(input("1 point or 11 points?"))
    if ace_answer == 1:
        buster += 1
        second_draw = 1
    else:
        buster +=11
        second_draw = 11

dealer_first_draw = dealer_turn() # Das selbe nur für den Dealer (Er hat keine Wahl ob er 11 oder 1 kriegt, wie in GTA ^^)
dealer_buster = dealer_first_draw
while dealer_buster < 17:
    dealer_buster += dealer_turn()
    if dealer_turn() == Ace:
        if dealer_buster > 10:
            Ace = 1
        elif dealer_buster < 11:
            Ace = 11



def player_result(): # ergebnis der ersten Ziehung beim Spieler
    print(f"You have drawn a {first_draw} and a {second_draw}. You have in total {first_draw + second_draw}.")
    dealer_result()
    answer = input(f"The first Card of the Dealer is a {dealer_first_draw}. Take another Card? yes or no ")
    if answer == "yes":
        player_sec_turn()
    else:
        game_result1()

def game_result1(): # Wenn man keine Karten zieht
    if dealer_buster > 21:
        print(f"Dealer has a busted. Player wins!!!")
        exit()
    if first_draw + second_draw > dealer_buster:
        print(f"You have drawn a total of {first_draw + second_draw} and the dealer only has drawn a {dealer_buster}. You Win!!!")
        exit()
    elif first_draw + second_draw == dealer_buster:
        print(f"You and the Dealer both have {dealer_buster}. its a Tie!!!")
        exit()
    elif first_draw + second_draw < dealer_buster:
        print(f"You have drawn only a total of {first_draw + second_draw} and the dealer has drawn a {dealer_buster}. You lose!!!")
        exit()

def game_result2(): # Wenn man eine Karte mehr gezogen hat
    if dealer_buster > 21:
        print(f"Dealer has a busted. Player wins!!!")
        exit()
    if buster > dealer_buster:
        print(f"You have drawn a total of {buster} and the dealer only has drawn a {dealer_buster}. You Win!!!")
        exit()
    elif buster == dealer_buster:
        print(f"You and the Dealer both have {dealer_buster}. its a Tie!!!")
        exit()
    elif buster < dealer_buster:
        print(f"You have drawn only a total of {buster} and the dealer has drawn a {dealer_buster}. You lose!!!")
        exit()




def dealer_result(): # Falls der Dealer und oder der Spieler direkt Black jack hat
    if dealer_buster == 21 == first_draw + second_draw:
        print("Both the Player and Dealer have a Black Jack. Its a Tie!!!")
        exit()
    elif dealer_buster == 21:
        print("Dealer has a Black Jack. Player loses!!!")
        exit()
def player_sec_turn(): # Wenn der Spieler eine Karte gezogen hat
    global buster
    third_draw = player_turn()
    if third_draw == Ace:
        ace_answer = int(input("1 point or 11 points?"))
        if ace_answer == 1:
            buster += 1
            third_draw = 1
        else:
            buster += 11
            third_draw = 11
    buster = first_draw + second_draw + third_draw
    print(f"You have drawn a {third_draw}.")
    while buster <= 21:
        answer = input("Another Card? Yes or No?")
        if answer.lower() == "yes":
            one_more_turn = player_turn()
            if one_more_turn == Ace:
                ace_answer = int(input("1 point or 11 points?"))
                if ace_answer == 1:
                    buster += 1
                    one_more_turn = 1
                else:
                    buster += 11
                    one_more_turn = 11
            buster += one_more_turn
            if buster > 21:
                print(f"You have drawn a {one_more_turn} and you are Busted. Player loses!!!")
                exit()
            else:
                print(f"You have drawn a {one_more_turn}.")
        else:
            game_result2()
    if buster > 21:
        print(f"You are Busted. Player loses!!!")
        exit()

game_start() #startet das Programm