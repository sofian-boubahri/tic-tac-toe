# Initialisation du plateau avec des cases vides
morpion = [""] * 9
joueur_actuel = "X"  # Le joueur X commence

def afficher_plateau(): # Affichage du plateau
    print(f"| {morpion[0]} | {morpion[1]} | {morpion[2]} |")
    print("-----------")
    print(f"| {morpion[3]} | {morpion[4]} | {morpion[5]} |")
    print("-----------")
    print(f"| {morpion[6]} | {morpion[7]} | {morpion[8]} |")

def verifier_victoire():
    lignes_gagnantes = [
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8], 
        [0, 4, 8],  
        [2, 4, 6]  
    ]
    
    for ligne in lignes_gagnantes:
        if morpion[ligne[0]] == morpion[ligne[1]] == morpion[ligne[2]] != "":
            return morpion[ligne[0]]  # Renvoie "X" ou "O" s'il y a un gagnant
    return None 

# Boucle principale du jeu
while True:
    afficher_plateau() 
    try:
        # Demander au joueur de choisir une case
        nouveau_tour = int(input(f"Joueur {joueur_actuel}, veuillez choisir une case (1-9): ")) - 1
        
        # Vérifier si la case est valide et si elle est vide
        if 0 <= nouveau_tour <= 8 and morpion[nouveau_tour] == "":
            morpion[nouveau_tour] = joueur_actuel 
            
            # Vérifier si le joueur actuel a gagné
            gagnant = verifier_victoire()
            if gagnant:
                afficher_plateau()  # Afficher le plateau final
                print(f"Félicitations ! Le joueur {gagnant} a gagné !")
                break 
            
            # Vérifier si le jeu est un match nul
            if "" not in morpion:
                afficher_plateau()
                print("Match nul ! Le jeu est terminé.")
                break
            
            # Alterner le joueur actuel
            joueur_actuel = "O" if joueur_actuel == "X" else "X"
        else:
            print("Case invalide ou déjà occupée, essayez encore.")
    except ValueError:
        print("Veuillez entrer un numéro valide entre 1 et 9.")