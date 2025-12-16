from js import document

def bepaal_resultaat(event=None):
    document.getElementById("resultaat").innerText = "Knop werkt!"

document.getElementById("submitBtn").addEventListener("click", bepaal_resultaat)
