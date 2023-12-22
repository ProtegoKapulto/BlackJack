import random

def draw_card():
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
    if card == 11:
        return int(input("1 point or 11 points? "))
    return card

def dealer_draw():
    return draw_card()

def player_turn():
    return draw_card()

def game_result(player_total, dealer_total):
    if player_total > 21 or dealer_total == 21:
        print("Player loses!")
    elif dealer_total > 21 or player_total == 21 or player_total > dealer_total:
        print("Player wins!")
    elif player_total == dealer_total:
        print("It's a tie!")
    else:
        print("Player loses!")

def play_game():
    print("Welcome to Blackjack")
    start = input("Type 'Start' to begin: ").lower()

    if start != "start":
        print("ERROR. You had one job...")
        return

    player_total = draw_card() + draw_card()
    dealer_total = dealer_draw()

    print(f"You have drawn a {player_total}.")

    while True:
        answer = input("Another card? Yes or No? ").lower()
        if answer != "yes":
            game_result(player_total, dealer_total)
            return

        player_card = draw_card()
        player_total += player_card

        if player_total > 21:
            print(f"You have drawn a {player_card} and you are busted. Player loses!")
            return
        else:
            print(f"You have drawn a {player_card}.")

play_game()
