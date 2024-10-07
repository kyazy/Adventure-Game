def greeting():
    print("Willkommen zur verlorenen Schatzsuche!")
    print("Löse Rätsel um dem Schatz zu finden")
    print("Mithilfe der Eingabe von 'norden', 'süden', 'westen' oder 'osten' kannst du dich fortbewegen!")

def end_game():
    print("Danke fürs Spielen! Adios!")

def main():
    greeting()
    current_room= "Raum 1"
    print("\n----- Aktueller Raum: ", current_room, "-----")
    print("1. Nach Norden gehen")
    print("2. Nach Osten gehen")
    print("3. Nach Süden gehen")
    print("4. Nach Westen gehen")

    action = input("In Welche richtung möchtest du gehen ? (norden,osten,süden,westen,verlassen): ?")
    if action =="norden":
        if current_room == "Raum 1":
            current_room = "Raum 2"
            enter_room(current_room)
        elif current_room == "Raum 2":
            current_room == "Raum 3"
            enter_room(current_room)
    elif action == "osten":
        print("Dort sind nur seltsame Zeichen an der Wand. Du kannst sie nicht lesen.")
    elif action == "süden":
        print("Du kannst den Dungeon nicht einfach verlassen ohne es probiert zu haben.")
    elif action == "westen":
        print("Diese Wand scheint mit moos überdeckt zu sein. Dort kann ich nicht weiter.")
    elif action == "verlassen":
        print("Dein Mut ist nicht genug.. Du verlässt weinend den Dungeon!")
        end_game()
        

    else: 
        print("Das funktioniert nicht. Bitte wähle zwischen norden, osten, süden ,westen oder verlassen")

   

    







    def enter_room(room):
        if room == "Raum 1":
            print("Eine geheimnissvolle Stimme ertönt! Lausche Ihr um das erste Rätsel zu lösen!")
            riddle = "Welche Maus hat nur 2 Beine?"
            if solve_riddle(riddle):
                print("Du hast das erste Rätsel gelöst! Eine Tür öffnet sich und du gehst weiter")
            else:
                print("Das Rätsel wurde nicht gelöst. Kehre zum Anfang zurück!")
        elif room == "Raum 2":
            print("Du bist beim 2. Rätsel angekommen. Die Mysteriöse Stimme ertönt erneut: ")
            riddle = "Welche Ente hat nur 2 Beine?"
            if solve_riddle(riddle):
                print("Das 2. Rätsel wurde gelöst. Eine klapprige Falltür öffnet sich. Steige hinab!")
            else:
                print("Du hast das Rätsel nicht gelöst. Bitte starte von vorne! ")
        elif room == "Raum 3":
            print("Ein Großes verschlossenes Tor. Eine Inschrift zeigt an : ")
            riddle = "Was ist Grün und wird auf Knopfdruck Rot ?"
            if solve_riddle(riddle):
                print("Du hast es in die Großes Ruhmeshalle voller Gold geschafft! Herzlichen Glückwunsch")
            else:
                print("Die Antwort war falsch. Kehre zurück! ")
                end_game()
