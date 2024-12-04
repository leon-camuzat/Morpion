# Fonction principale qui gère le déroulement du jeu
def jouer():
    choix_joueur()  # Demande à l'utilisateur de choisir son symbole (X ou O)
    affichage_grille()  # Affiche l'état actuel de la grille
    while fin_jeu == False :  # Tant que la partie n'est pas finie
        tour(joueur_actuel)  # Un joueur joue son tour
        verifier_fin_jeu()  # Vérifie si le jeu est terminé (victoire ou match nul)
        joueur_suivant()  # Change de joueur
    resultat()  # Affiche le résultat de la partie une fois finie

# Fonction qui gère le tour d'un joueur
def tour(joueur):
    print("C'est le tour du joueur : ", joueur)  # Affiche quel joueur doit jouer
    pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : ")
    
    valide = False  # Variable qui vérifie si la position choisie est valide
    while valide == False:
    
        # Si la position choisie n'est pas un nombre entre 1 et 9, on redemande
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 :")
        pos = int(pos) - 1  # Convertit la position en indice de la liste (indices de 0 à 8)
        
        # Si la case est vide, on peut jouer. Sinon, on redemande.
        if grille[pos] == "-":
            valide = True
        else:
            print("Vous ne pouvez pas accéder à cette position")
            