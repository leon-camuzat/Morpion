#Partie 1 : Variables (grille ; joueur_actuel ; fin_jeu ; gagnant)

grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

joueur_actuel = ""

fin_jeu = False

gagnant = ""

#Partie 2 : Fonctions (jouer + choix_joueur + affichage_grille)
def jouer():
    choix_joueur()
    affichage_grille()
    while fin_jeu == False :
        tour(joueur_actuel)
        verifier_fin_jeu()
        joueur_suivant()
    resultat()


# Fonction pour demander à l'utilisateur de choisir X ou O
def choix_joueur():
    global joueur_actuel #?
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
    print("\n") # ?

# Appeler la fonction pour afficher la grille
affichage_grille()

def tour(joueur) :
    print("C'est le tour du joueur : ",joueur) 
    pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : ")
    
    valide = False
    while valide == False:
    
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 :")
        pos = int(pos) - 1 #?
        
        if grille[pos] =="-":
            valide = True
        else :
            print("Vous ne pouvez pas accéder à cette position")
            
    grille[pos] = joueur
    affichage_grille()
    
def verifier_fin_jeu():
    verfifier_victoire()
    verifier_match_nul()
    
def verfifier_victoire(): # conditions de victoirres
    global fin_jeu
    global gagnant
    #lignes
    if grille[0] == grille[1] == grille[2] and grille[2] !="-":
        fin_jeu=True
        gagnant = grille[1]
    if grille[3] == grille[4] == grille[5] and grille[3] !="-":
        fin_jeu=True
        gagnant = grille[3]
    if grille[6] == grille[7] == grille[8] and grille[7] !="-":
        fin_jeu=True
        gagnant = grille[6]
    #colonnes
    if grille[0] == grille[3] == grille[6] and grille[0] !="-":
        fin_jeu=True
        gagnant = grille[1]
    if grille[1] == grille[4] == grille[7] and grille[4] !="-":
        fin_jeu=True
        gagnant = grille[4]
    if grille[2] == grille[5] == grille[8] and grille[8] !="-":
        fin_jeu=True
        gagnant = grille[5]
    #diagonalles
    if grille[0] == grille[4] == grille[8] and grille[8] !="-":
        fin_jeu=True
        gagnant = grille[8]
    if grille[2] == grille[4] == grille[6] and grille[3] !="-":
        fin_jeu=True
        gagnant = grille[3]
        
def verifier_match_nul():
    global fin_jeu
    if "-" not in grille:
        fin_jeu = True
    
def joueur_suivant():
    global joueur_actuel
    if joueur_actuel == "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"
        
def resultat ():
    if gagnant == "X" or gagnant == "O":
        print("Le joueur : ",gagnant,"a gagné")
    else:
        print("Match nul")
jouer()