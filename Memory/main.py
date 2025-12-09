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
            div.classList.add("revealed")
            div.innerText = card
        else:
            div.innerText = "Memory kaart"
        div.onclick = lambda e, i=i: flip_card(i)
        game_div.appendChild(div)


def flip_card(i):
    global flipped
    if i in flipped or cards[i] in matched:
        return
    elif len(flipped) < 2:   # Je mag maximaal twee kaarten omdraaien
        flipped.append(i)
        render()

def check_game(event=None):
    global flipped
    msg_div = document.getElementById("message")
    if len(matched) == len(cards):
        msg_div.innerText = "Je hebt alles gevonden! Het spel start opnieuw"
        reset_game()
        return
    elif len(flipped) == 2:
         c1, c2 = flipped
         v1, v2 = cards[c1], cards[c2]
         if (v1 in pairs and pairs[v1] == v2) or (v2 in pairs and pairs[v2] == v1):
              matched.extend([v1, v2])
              msg_div.innerText = "Goed gedaan! Dat is een match"
         else:
            msg_div.innerText = "Geen match, probeer opnieuw."   
         flipped = []
         render()
    else:
        msg_div.innerText = "Kies twee kaarten"

#Reset-functie die game opnieuw start
def reset_game(event=None):
    init_game()

init_game()