# Définir la grille du jeu
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

# Variable pour le joueur actuel
joueur_actuel = ""

# Fonction pour demander à l'utilisateur de choisir X ou O
def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O) : ")
    
    while True:
        joueur_actuel = joueur_actuel.upper()  # Convertir la réponse en majuscule
        if joueur_actuel == 'X':
            print("Vous avez choisi X. Le joueur 2 aura O")
            break
        elif joueur_actuel == 'O':
            print("Vous avez choisi O. Le joueur 2 aura X")
            break
        else:
            joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O) : ")

# Appeler la fonction pour tester le choix du joueur
choix_joueur()

# Fonction pour afficher la grille
def affichage_grille():
    print("\n") # ?
    print("-------------")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|")
    print("-------------")
    print("|", grille[3], "|", grille[4], "|", grille[5], "|")
    print("-------------")
    print("|", grille[6], "|", grille[7], "|", grille[8], "|")
    print("-------------")

# Appeler la fonction pour afficher la grille
affichage_grille()