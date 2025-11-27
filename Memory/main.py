from js import document
import random


#Landen en hoofdsteden
pairs = { "Vietnam": "Hanoi",
    "Nepal" : "Kathmandu",
    "Kenia": "Nairobi",
    "Tanzania": "Dodoma",
    "Filipijnen": "Manila",
    "India": "New Delhi",
    "Ghana": "Accra",
    "Cambodja": "Phnom Penh",
}


# Houd spelstatus bij
cards = []
flipped = []
matched = []

def init_game():
    global cards, flipped, matched
    cards = list(pairs.keys()) + list(pairs.values())
    random.shuffle(cards)
    flipped = []
    matched = []
    render()

def render():
    game_div = document.getElementById("game")
    game_div.innerHTML = ""
    for i, card in enumerate(cards):
        div = document.createElement("div")
        div.className = "card"
        if card in matched:
            div.classList.add("matched")
            div.innerText = card
        elif i in flipped:
            div.innerText = card
        else:
            div.innerText = "?"
        div.onclick = lambda e, i=i: flip_card(i)
        game_div.appendChild(div)


def flip_card(i):
    global flipped 
    if len(flipped) == 2:
        check_match()
        render()
    elif i not in flipped and cards[i] not in matched:
        flipped.append(i)
        render()

def check_match():
    global flipped
    if len(flipped) < 2:
        return
    c1, c2 = flipped
    v1, v2 = cards[c1], cards[c2]
    if (v1 in pairs and pairs[v1] == v2) or (v2 in pairs and pairs[v2] == v1):
        matched.extend([v1, v2])
    flipped = []

#Reset-functie die vanuit HTML wordt aangeroepen
def reset_game():
    init_game()

init_game()