
import tkinter as tk
from tkinter import messagebox
import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score



def start_game():
    global player_cards, dealer_cards, game_over

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    game_over = False

    update_display()

def update_display():
    player_score = calculate_score(player_cards)

    player_cards_label.config(
        text=f"Player Cards: {' '.join(map(str, player_cards))}"
    )

    player_score_label.config(
        text=f"Player Score: {player_score}"
    )

    dealer_cards_label.config(
        text=f"Dealer Cards: {dealer_cards[0]} ?"
    )

    result_label.config(text="")

    if player_score > 21:
        dealer_cards_label.config(
            text=f"Dealer Cards: {' '.join(map(str, dealer_cards))}"
        )

        result_label.config(
            text="You went over 21. You Lose!"
        )

        disable_buttons()

def hit():
    if game_over:
        return

    player_cards.append(deal_card())
    update_display()

def stand():
    global game_over

    dealer_score = calculate_score(dealer_cards)

    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    player_score = calculate_score(player_cards)

    dealer_cards_label.config(
        text=f"Dealer Cards: {' '.join(map(str, dealer_cards))}"
    )

    dealer_score_label.config(
        text=f"Dealer Score: {dealer_score}"
    )

    if dealer_score > 21:
        result = "Dealer busted. You Win!"
    elif player_score > dealer_score:
        result = "You Win!"
    elif player_score < dealer_score:
        result = "Dealer Wins!"
    else:
        result = "Draw!"

    result_label.config(text=result)

    game_over = True
    disable_buttons()

def disable_buttons():
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")

def new_game():
    hit_button.config(state="normal")
    stand_button.config(state="normal")
    dealer_score_label.config(text="")
    start_game()


root = tk.Tk()
root.title("Blackjack")
root.geometry("700x500")

title = tk.Label(
    root,
    text="BLACKJACK",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

dealer_title = tk.Label(
    root,
    text="Dealer",
    font=("Arial", 18)
)
dealer_title.pack()

dealer_cards_label = tk.Label(
    root,
    text="",
    font=("Arial", 16)
)
dealer_cards_label.pack()

dealer_score_label = tk.Label(
    root,
    text="",
    font=("Arial", 16)
)
dealer_score_label.pack()

tk.Label(root, text="").pack()

player_title = tk.Label(
    root,
    text="Player",
    font=("Arial", 18)
)
player_title.pack()

player_cards_label = tk.Label(
    root,
    text="",
    font=("Arial", 16)
)
player_cards_label.pack()

player_score_label = tk.Label(
    root,
    text="",
    font=("Arial", 16)
)
player_score_label.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

hit_button = tk.Button(
    button_frame,
    text="Hit",
    font=("Arial", 14),
    width=10,
    command=hit
)
hit_button.grid(row=0, column=0, padx=10)

stand_button = tk.Button(
    button_frame,
    text="Stand",
    font=("Arial", 14),
    width=10,
    command=stand
)
stand_button.grid(row=0, column=1, padx=10)

new_game_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14),
    command=new_game
)
new_game_button.pack(pady=20)

start_game()

root.mainloop()
