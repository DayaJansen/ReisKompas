from js import document
import random #zodat de kaarten willekeurig worden geschud


#Lijst Landen en hoofdsteden
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
cards = []  #alle kaarten van landen en hoofdsteden
flipped = []    #alle omgedraaide kaarten
matched = []    #Lijst met kaart die al een match zijn

def init_game():
    global cards, flipped, matched  #kondigt aan dat de bovengenoemde lijsten worden aangepast
    cards = list(pairs.keys()) + list(pairs.values())   #voegt de landen en hoofdsteden samen in één lijst
    random.shuffle(cards)   #Schud de kaarten met landen en hoofdsteden door elkaar
    flipped = []    #Reset spelstatus
    matched = []
    render()    #Maakt het speelveld

def render():
    game_div = document.getElementById("game")  
    game_div.innerHTML = ""     #Het programma maakt het vak waar de kaarten komen eerst leeg
    for i, card in enumerate(cards):    #Voor elke kaart wordt er een apart vakje gemaakt
        div = document.createElement("div")
        div.className = "card"
        if card in matched:     #De kaart is goed gematcht dus wordt het toegevoegd aan de class matched, zodat het via de CSS-pagina groen wordt
            div.classList.add("matched")
            div.innerText = card
        elif i in flipped:      #De kaart is omgedraaid en wordt via de CSS-pagina dikgedrukt weergegeven
            div.classList.add("revealed")
            div.innerText = card
        else:       #De kaart is niet omgedraaid en laat de achterkant van de kaart zien: "memory kaart"
            div.innerText = "Memory kaart"
        div.onclick = lambda e, i=i: flip_card(i)       #Het programma draait de kaart om als er op wordt gedrukt
        game_div.appendChild(div)   #Het programma laat de inhoud van het kaartje (een land of hoofdstad) zien


def flip_card(i):
    global flipped
    if i in flipped or cards[i] in matched:
        return #het programma negeert het als er wordt gedrukt op kaarten die al gematcht of omgedraaid zijn
    elif len(flipped) < 2:   # Je mag omdraaien tot er 2 kaarten omgedraaid zijn
        flipped.append(i)   #de omgedraaide kaart wordt toegevoegd aan de lijst 'flipped'
        render()    #Het wordt laten zien op het scherm dat de kaart is omgedraaid

def check_game(event=None):
    global flipped
    msg_div = document.getElementById("message")        #Het programma maakt plek voor het bericht of de match klopt of niet
    if len(matched) == len(cards):
        msg_div.innerText = "Je hebt alles gevonden! Het spel start opnieuw"
        reset_game()
        return
    elif len(flipped) == 2:     #Als er twee kaarten zijn omgedraaid checkt het programma of de match klopt
         c1, c2 = flipped
         v1, v2 = cards[c1], cards[c2]
         if (v1 in pairs and pairs[v1] == v2) or (v2 in pairs and pairs[v2] == v1):
            matched.extend([v1, v2])      #Voegt de kaarten toe aan de lijst 'matched'
            msg_div.innerText = "Goed gedaan! Dat is een match"
         else:
            msg_div.innerText = "Geen match, probeer opnieuw."   
         flipped = []      #Het programma draait de kaarten weer om als het geen match is
         render()   #Het spel wordt bijgewerkt zodat te zien is dat de kaarten weer zijn omgedraaid
    else:
        msg_div.innerText = "Kies twee kaarten"

#Reset-functie die game opnieuw start
def reset_game(event=None):
    init_game()

init_game()