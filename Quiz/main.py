from js import document

def bepaal_resultaat(event=None):
    scores = {
        "Vietnam": 0,
        "Nepal": 0,
        "Kenia": 0,
        "Tanzania": 0,
        "Filipijnen": 0,
        "India": 0,
        "Ghana": 0,
        "Cambodja": 0
    }

    antwoord1 = document.getElementById("vraag1").value
    antwoord2 = document.getElementById("vraag2").value
    antwoord3 = document.getElementById("vraag3").value
    antwoord4 = document.getElementById("vraag4").value
    antwoord5 = document.getElementById("vraag5").value
    antwoord6 = document.getElementById("vraag6").value

    # Vraag 1
    if antwoord1 == "weekend":
        scores["Ghana"] += 2
    elif antwoord1 == "week":
        scores["India"] += 2
        scores["Cambodja"] += 1
    elif antwoord1 == "2weken":
        scores["Vietnam"] += 2
        scores["Nepal"] += 2
    elif antwoord1 == "lang":
        scores["Tanzania"] += 2
        scores["Kenia"] += 2
        scores["Filipijnen"] += 2

    # Vraag 2
    if antwoord2 == "buitenEU":
        scores["Vietnam"] += 2
        scores["Nepal"] += 2
        scores["Kenia"] += 2
        scores["Tanzania"] += 2
        scores["Filipijnen"] += 2
        scores["Cambodja"] += 2
        scores["India"] += 2
        scores["Ghana"] += 2

    # Vraag 3
    if antwoord3 == "actief":
        scores["Nepal"] += 3
        scores["Kenia"] += 2
        scores["Tanzania"] += 2
    elif antwoord3 == "relax":
        scores["Filipijnen"] += 3
        scores["Cambodja"] += 2
    elif antwoord3 == "cultuur":
        scores["India"] += 3
        scores["Vietnam"] += 2
        scores["Cambodja"] += 2
    elif antwoord3 == "feest":
        scores["Ghana"] += 2
        scores["Filipijnen"] += 2

    # Vraag 4
    if antwoord4 == "sneeuw":
        scores["Nepal"] += 3
    elif antwoord4 == "zon":
        scores["Vietnam"] += 2
        scores["Filipijnen"] += 2
        scores["Cambodja"] += 2
    elif antwoord4 == "gematigd":
        scores["India"] += 2
        scores["Ghana"] += 2
    elif antwoord4 == "geen":
        scores["Tanzania"] += 1
        scores["Kenia"] += 1

    # Vraag 5
    if antwoord5 == "alleen":
        scores["Nepal"] += 2
        scores["India"] += 1
    elif antwoord5 == "koppel":
        scores["Filipijnen"] += 2
        scores["Cambodja"] += 2
    elif antwoord5 == "kinderen":
        scores["Tanzania"] += 2
        scores["Kenia"] += 2
    elif antwoord5 == "pubers":
        scores["Vietnam"] += 2
        scores["Ghana"] += 1
    elif antwoord5 == "jongeren":
        scores["Ghana"] += 2
        scores["Filipijnen"] += 1
    elif antwoord5 == "volwassenen":
        scores["India"] += 2
        scores["Cambodja"] += 1
    elif antwoord5 == "groep":
        scores["Kenia"] += 2
        scores["Tanzania"] += 2

    # Vraag 6
    if antwoord6 == "resort":
        scores["Filipijnen"] += 2
        scores["Vietnam"] += 1
    elif antwoord6 == "hostel":
        scores["Cambodja"] += 2
        scores["India"] += 1
    elif antwoord6 == "tent":
        scores["Nepal"] += 2
        scores["Kenia"] += 2
        scores["Tanzania"] += 2
    elif antwoord6 == "airbnb":
        scores["Ghana"] += 2
        scores["India"] += 1

    resultaat = max(scores, key=scores.get)
    document.getElementById("resultaat").innerText = f"Jouw resultaat is: {resultaat}"

document.getElementById("submitBtn").addEventListener("click", bepaal_resultaat)

