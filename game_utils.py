def solve_riddle(riddle):
    print(f"Rätsel: {riddle}")
    antwort = input("Deine Antwort: ").lower()

    if riddle == "Welche Maus hat nur 2 beine?":
        return antwort == "Mickey Mouse"
    elif riddle == "Welche Ente hat nur 2 beine?":
        return antwort == "Alle Enten"
    elif riddle == "Was ist Grün und wird auf Knopfdruck Rot?":
        return antwort == "Ein Frosch im Mixer"
    else:
        return False
    
 