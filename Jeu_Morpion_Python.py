import os

SYMBOLES = ["❌", "⭕"]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def creer_plateau():
    return [" " for _ in range(9)]

def afficher_plateau(plateau):
    print("-----+-----+-----")
    for i in range(9):
        case = plateau[i] if plateau[i] != " " else str(i + 1)
        print(f"  {case}  ", end="")
        if i % 3 != 2:
            print("|", end="")
        else:
            print("\n-----+-----+-----")

def verifier_victoire(plateau, joueur):
    combinaisons = [
        (0,1,2), (3,4,5), (6,7,8),  # lignes
        (0,3,6), (1,4,7), (2,5,8),  # colonnes
        (0,4,8), (2,4,6)            # diagonales
    ]
    
    for a, b, c in combinaisons:
        if plateau[a] == plateau[b] == plateau[c] == joueur:
            return True
    return False

def plateau_plein(plateau):
    return " " not in plateau

def demander_choix(plateau, joueur):
    while True:
        try:
            choix = int(input(f"Joueur {joueur}, choisissez une case (1-9) : "))
            if 1 <= choix <= 9 and plateau[choix - 1] == " ":
                return choix - 1
            else:
                print("Case invalide ou déjà occupée.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def jouer():
    plateau = creer_plateau()
    joueur_index = 0
    
    while True:
        clear_screen()
        afficher_plateau(plateau)
        
        joueur = SYMBOLES[joueur_index]
        position = demander_choix(plateau, joueur)
        plateau[position] = joueur
        
        if verifier_victoire(plateau, joueur):
            clear_screen()
            afficher_plateau(plateau)
            print(f"🎉 Le joueur {joueur} a gagné !")
            break
        
        if plateau_plein(plateau):
            clear_screen()
            afficher_plateau(plateau)
            print("🤝 Match nul !")
            break
        
        joueur_index = 1 - joueur_index  # alterner joueur

if __name__ == "__main__":
    jouer()
