# Document ophalen van javascript naar python en setTimeout voor confetti
from js import document, setTimeout, showConfetti


def bepaal_resultaat(event=None):

    # Scoretabel voor bestemmingen
    scores = {
        # Azië
        "Vietnam": 0,
        "Nepal": 0,
        "India": 0,
        "Filipijnen": 0,
        "Cambodja": 0,
        "Thailand": 0,
        "Indonesië": 0,
        "Laos": 0,
        "Kirgistan": 0,
        "Oezbekistan": 0,
        "Iran": 0,
        "Georgië": 0,
        "Armenië": 0,

        # Afrika
        "Kenia": 0,
        "Tanzania": 0,
        "Ghana": 0,
        "Egypte": 0,
        "Seychellen": 0,
        "Marokko": 0,
        "Oeganda": 0,
        "Zuid-Afrika": 0,

        # Europa
        "Kreta": 0,
        "Cyprus": 0,
        "Spanje": 0,
        "Oostenrijk": 0,
        "Frankrijk": 0,
        "Nederland": 0,

        # Amerika
        "Mexico": 0,
        "Jamaica": 0,
        "Brazilië": 0,
        "Guyana": 0,
        "Peru": 0,
        "Bolivia": 0,
        "Canada": 0,

        # Midden-Oosten
        "Jordanië": 0,
    }

    # Lijsten voor afstandsfilter
    EU_LANDEN = [
        "Nederland",
        "Kreta",
        "Cyprus",
        "Spanje",
        "Oostenrijk",
        "Frankrijk"
    ]

    NIET_EU_LANDEN = [
        land for land in scores if land not in EU_LANDEN
    ]

    # Antwoorden van de HTML halen
    antwoord1 = document.getElementById("vraag1").value
    antwoord2 = document.getElementById("vraag2").value
    antwoord3 = document.getElementById("vraag3").value
    antwoord4 = document.getElementById("vraag4").value
    antwoord5 = document.getElementById("vraag5").value
    antwoord6 = document.getElementById("vraag6").value

    # -------------------------------
    # --- Vraag 1: Duur vakantie ---
    # -------------------------------
    if antwoord1 == "weekend":
        # korte trips → vooral Europa
        for land in ["Kreta", "Cyprus", "Spanje", "Oostenrijk", "Frankrijk"]:
            scores[land] += 2

    elif antwoord1 == "week":
        for land in ["Kreta", "Cyprus", "Spanje", "Oostenrijk", "Frankrijk"]:
            scores[land] += 2

    elif antwoord1 == "2weken":
        for land in [
            "Vietnam", "Nepal", "Kenia", "Tanzania", "Filipijnen", "India",
            "Cambodja", "Thailand", "Indonesië", "Laos", "Marokko",
            "Egypte", "Seychellen", "Mexico", "Jamaica", "Brazilië",
            "Guyana", "Peru", "Bolivia", "Oeganda", "Zuid-Afrika",
            "Georgië", "Armenië", "Iran", "Oezbekistan", "Kirgistan"
        ]:
            scores[land] += 2

    elif antwoord1 == "lang":
        # lange reizen → verre bestemmingen
        for land in [
            "Vietnam", "Nepal", "Kenia", "Tanzania", "Filipijnen", "India",
            "Cambodja", "Thailand", "Indonesië", "Laos", "Seychellen",
            "Mexico", "Jamaica", "Brazilië", "Guyana", "Peru", "Bolivia",
            "Oeganda", "Zuid-Afrika", "Canada", "Iran", "Oezbekistan",
            "Kirgistan", "Georgië", "Armenië", "Jordanië"
        ]:
            scores[land] += 2

    # -------------------------------
    # --- Vraag 2: Afstand ---
    # -------------------------------
    if antwoord2 == "binnenNL":
        scores["Nederland"] += 20

    elif antwoord2 == "binnenEU":
        for land in EU_LANDEN:
            scores[land] += 5

    elif antwoord2 == "buitenEU":
        for land in NIET_EU_LANDEN:
            scores[land] += 5

    # -------------------------------
    # --- Vraag 3: Wat zoekt u? ---
    # -------------------------------
    if antwoord3 == "actief":
        for land in ["Nepal", "Kenia", "Tanzania", "Peru", "Bolivia", "Kirgistan", "Oeganda"]:
            scores[land] += 2

    elif antwoord3 == "relax":
        for land in ["Filipijnen", "Seychellen", "Jamaica", "Mexico", "Kreta", "Cyprus"]:
            scores[land] += 3

    elif antwoord3 == "cultuur":
        for land in ["India", "Vietnam", "Cambodja", "Iran", "Oezbekistan", "Jordanië", "Marokko", "Georgië", "Armenië"]:
            scores[land] += 3

    elif antwoord3 == "feest":
        for land in ["Ghana", "Filipijnen", "Spanje", "Jamaica", "Mexico", "Brazilië"]:
            scores[land] += 2

    # -------------------------------
    # --- Vraag 4: Weer ---
    # -------------------------------
    if antwoord4 == "sneeuw":
        for land in ["Nepal", "Oostenrijk", "Canada", "Kirgistan"]:
            scores[land] += 3

    elif antwoord4 == "zon":
        for land in [
            "Vietnam", "Filipijnen", "Cambodja", "Thailand", "Indonesië",
            "Kreta", "Cyprus", "Spanje", "Egypte", "Seychellen", "Mexico",
            "Jamaica", "Brazilië", "Guyana", "Marokko", "Oeganda",
            "Zuid-Afrika", "Jordanië", "Laos"
        ]:
            scores[land] += 2

    elif antwoord4 == "gematigd":
        for land in ["India", "Frankrijk", "Georgië", "Armenië", "Peru", "Bolivia", "Canada"]:
            scores[land] += 2

    elif antwoord4 == "geen":
        for land in scores:
            scores[land] += 1

    # -------------------------------
    # --- Vraag 5: Met wie? ---
    # -------------------------------
    if antwoord5 == "alleen":
        for land in [
            "Nepal", "India", "Egypte", "Seychellen", "Brazilië", "Guyana",
            "Laos", "Vietnam", "Oeganda", "Peru", "Bolivia"
        ]:
            scores[land] += 2

    elif antwoord5 == "koppel":
        for land in ["Filipijnen", "Cambodja", "Kreta", "Cyprus", "Seychellen", "Jamaica", "Marokko"]:
            scores[land] += 2

    elif antwoord5 == "kinderen":
        for land in ["Tanzania", "Kenia", "Mexico", "Kreta", "Cyprus"]:
            scores[land] += 2

    elif antwoord5 == "pubers":
        for land in ["Vietnam", "Ghana", "Spanje"]:
            scores[land] += 2

    elif antwoord5 == "jongeren":
        for land in ["Ghana", "Filipijnen", "Spanje", "Thailand", "Brazilië"]:
            scores[land] += 2

    elif antwoord5 == "volwassenen":
        for land in [
            "India", "Cambodja", "Jamaica", "Mexico", "Brazilië", "Guyana",
            "Zuid-Afrika", "Georgië", "Armenië", "Iran", "Oezbekistan",
            "Kirgistan", "Marokko"
        ]:
            scores[land] += 2

    elif antwoord5 == "groep":
        for land in ["Kenia", "Tanzania"]:
            scores[land] += 2

    # -------------------------------
    # --- Vraag 6: Verblijf ---
    # -------------------------------
    if antwoord6 == "resort":
        for land in ["Filipijnen", "Vietnam", "Kreta", "Cyprus", "Egypte", "Seychellen", "Mexico", "Jamaica"]:
            scores[land] += 2

    elif antwoord6 == "hostel":
        for land in ["Cambodja", "India", "Brazilië", "Peru", "Bolivia", "Laos", "Vietnam"]:
            scores[land] += 2

    elif antwoord6 == "tent":
        for land in ["Nepal", "Kenia", "Tanzania", "Kirgistan", "Oeganda", "Seychellen"]:
            scores[land] += 2

    elif antwoord6 == "airbnb":
        for land in ["Ghana", "India", "Frankrijk", "Kreta", "Cyprus"]:
            scores[land] += 2

    # -------------------------------
    # --- Beste bestemming kiezen ---
    # -------------------------------
    if antwoord2 == "binnenEU":
        gefilterde_scores = {land: score for land, score in scores.items() if land in EU_LANDEN}

    elif antwoord2 == "buitenEU":
        gefilterde_scores = {land: score for land, score in scores.items() if land in NIET_EU_LANDEN}

    else:
        gefilterde_scores = scores

    resultaat = max(gefilterde_scores, key=gefilterde_scores.get)

    # Resultaat tonen in HTML
    document.getElementById("resultaat").innerText = f"Jouw resultaat is: {resultaat}"

    # Opnieuw-knop laten zien
    document.getElementById("opnieuwBtn").style.display = "block"

    # Confetti tonen
    showConfetti()

