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

#Lijst met kaarten
cards = list(pairs.keys()) + list(pairs.values())

random.shuffle(cards)

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
    if i in flipped or cards[i] in matched:
        return
    flipped.append(i)
    if len(flipped) == 2:
        check_match()
    render()

def check_match():
    global flipped
    c1, c2 = flipped
    v1, v2 = cards[c1], cards[c2]
    # Check of v1 en v2 een land-hoofdstad paar zijn
    if (v1 in pairs and pairs[v1] == v2) or (v2 in pairs and pairs[v2] == v1):
        matched.extend([v1, v2])
    flipped = []

#Reset-functie die vanuit HTML wordt aangeroepen
def reset_game():
    init_game()

init_game()