def initialiser_plateau():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau(plateau):
    for i in range(len(plateau)):
        print(" | ".join(plateau[i]))
        if i < len(plateau) - 1:
            print("-" * 9)

def player():
    playerX = "X"
    playerO = "O"

plateau = initialiser_plateau()
afficher_plateau(plateau)