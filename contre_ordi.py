from os import system # on import la fonction "system" du module "os" pour pouvoir vider le terminal
from platform import system as system_name # et la fonction "system" du module "platform" 
                                           # pour savoir sur quel SE on est, et vider le terminal avec la bonne commande
                                           
vider_terminal = "cls" if system_name() == "Windows" else "clear" # on choisis la bonne commande selon le SE pour vider le terminal

# la fonction qui affiche la grille pour l'utilisateur
def afficher_grille(grille):
    print(f"""
{grille[0]} | {grille[1]} | {grille[2]}
----------
{grille[3]} | {grille[4]} | {grille[5]}
----------
{grille[6]} | {grille[7]} | {grille[8]}    
""")
    
def demande_case_joueur(grille, symbole: str) -> int:
    """
    Fonction qui demande au joueur dans quel case il veux jouer, et retourn le numéro de la case
    tout en gérant les erreurs, par exemple si la case est déja prise, ou si le joueur entre une case qui n'existe pas...
    """
    while True:
        try:
            choix = int(input(f"joueur {symbole}, ou veux-tu joueur :")) - 1 # on soustrait 1 car le compte dans les listes commence a 0, tandis que le joueur compte en commençant par  1
            if choix < 0 or choix > 8:
                print("case invalid, veuillez entrer un nombre entre 1 et 9 pour la case")
                continue
            if grille[choix] == "X" or grille[choix] == "O":
                print(grille)
                print("choix invalid, cette case est deja prise")
                continue
            break
        except ValueError:
            print("case invalid, veuillez entrer un nombre entre 1 et 9 pour la case")
    return choix 

def demande_rejouer() -> bool:
    """
    Fonction qui demande a l'utilisateur si il veux rejouer tout en gérant les erreurs des choix invalides etc...
    retourn un True si le joueur veux rejouer, sinon False
    """
    while True:
        rejouer = input("rejouer ? o/n: ")
        if rejouer.lower() == "o":
            return True
        elif rejouer.lower() == "n":
            return False
        else:
            print("choix invalid, veuillez entrer 'o' pour oui, ou 'n' pour non")
            
def demande_symbole_joueur() -> str:
    while True:
        symbole = input("veux tu joueur avec X ou o (taper X ou O):")
        if symbole.lower() != "x" and symbole.lower() != 'o':
            print("choix invalid, veuillez entrer X ou O pour choisir votre symbole")
            continue
        else:
            break
    
    return symbole.upper()
        

def coup_ordi(grille, symbole):
    coup_possibles = [index for index, c in enumerate(grille) if c != "X" and c != "O"]
    meilleur_coup = coup_possibles[0]
    if symbole == "X":
        maxeval = -100
        for coup in coup_possibles:
            grille[coup] = symbole
            evaluation = minimax(grille, 9, False)
            if (evaluation > maxeval):
                meilleur_coup = coup
                maxeval = evaluation
            grille[coup] = coup + 1
    else:
        mineval = 100
        for coup in coup_possibles:
            grille[coup] = symbole
            evaluation = minimax(grille, 9, True)
            if (evaluation < mineval):
                meilleur_coup = coup
                mineval = evaluation
            grille[coup] = coup + 1
        
    return meilleur_coup
    
            
def is_win(grille):
    """
    Fonction qui vérifie si il y'a un gagnant dans la position
    elle vérifie si le meme symbole est le meme 3 fois, sur une ligne, une colonne, ou une diagonale
    """
    return ((grille[0] == grille[1] == grille[2]) or
            (grille[3] == grille[4] == grille[5]) or
            (grille[6] == grille[7] == grille[8]) or
            (grille[0] == grille[3] == grille[6]) or
            (grille[1] == grille[4] == grille[7]) or
            (grille[2] == grille[5] == grille[8]) or
            (grille[0] == grille[4] == grille[8]) or
            (grille[2] == grille[4] == grille[6]))

def evaluer_position(grille):
    """Fonction qui vérifie si il y'a un gagnant dans la position
    retourn 1 si le joueur X a gagné
    retourn 0 si il n'y a pas de gagnant
    retourn -1 si le joueur O a gagné
    cette fonction peut etre optimiser de ouf mais j'ai la flemme en tout cas elle fait le taff que j'ai décrit
    """
    # cet if check si X a une combinaison gagnate
    if ((grille[0] == grille[1] == grille[2] == "X") or
        (grille[3] == grille[4] == grille[5] == "X") or
        (grille[6] == grille[7] == grille[8] == "X") or
        (grille[0] == grille[3] == grille[6] == "X") or
        (grille[1] == grille[4] == grille[7] == "X") or
        (grille[2] == grille[5] == grille[8] == "X") or
        (grille[0] == grille[4] == grille[8] == "X") or
        (grille[2] == grille[4] == grille[6] == "X")):
        return 1
    # cet if check si O a une combinaison gagnate
    elif ((grille[0] == grille[1] == grille[2] == "O") or
          (grille[3] == grille[4] == grille[5] == "O") or
          (grille[6] == grille[7] == grille[8] == "O") or
          (grille[0] == grille[3] == grille[6] == "O") or
          (grille[1] == grille[4] == grille[7] == "O") or
          (grille[2] == grille[5] == grille[8] == "O") or
          (grille[0] == grille[4] == grille[8] == "O") or
          (grille[2] == grille[4] == grille[6] == "O")):
        return -1
    
    # sinon c'est match nul
    else:
        return 0
    
def minimax(grille, depth, xplayer, alpha=-200, beta=200):
    coup_possibles = [index for index, c in enumerate(grille) if c != "X" and c != "O"] # on récupere tout les coups possibles a joueur dans la position pour ensuite tous les tester
    if is_win(grille) or depth == 0 or len(coup_possibles) == 0:
        return evaluer_position(grille)
    
    # on test tout les coups possibles recursivement, pour voir si ils sont bon ou non pour notre position
    if xplayer: # si c'est le joueur x on essaye de maximiser
        maxeval = -100
        for coup in coup_possibles:
            grille[coup] = "X" # on joue le coup qu'on veux tester 
            evaluation = minimax(grille, depth - 1, False, alpha, beta)
            maxeval = max(evaluation, maxeval)
            grille[coup] = coup + 1 # on annule le coup pour pas alterer l'état de la position
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxeval
    else: # si c'est le joueur O on essaye de minimiser
        mineval = 100
        for index, coup in enumerate(coup_possibles):
            grille[coup] = "O"
            evaluation = minimax(grille, depth - 1, True, alpha, beta)
            mineval = min(evaluation, mineval)
            grille[coup] = coup + 1
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return mineval        
            
     
while True: # on créer une boucle while, pour que si l'utilisateur veut rejouer, on recommance
    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9] # la grille qui vas stocker l'état de notre jeu
    tour = 1
    symbole = demande_symbole_joueur()
    system(vider_terminal)
    afficher_grille(grille)
    while True:
        
        # si le symbole choisi par l'utilisateur est X alors on lui demande a lui qu'est ce qu'il veut jouer
        if symbole == "X":
            
            grille[demande_case_joueur(grille, "X")] = "X"
        # sinon on demande ac l'ordinateur
        else:
            grille[coup_ordi(grille, "X")] = "X"
        system(vider_terminal)
        print("le joueur X a joué :")
        afficher_grille(grille)
        if (is_win(grille)):
            print("joueur X a gagné !!!")
            break
        # si on est arrivé au 4eme tour et que le joueur X a joué et qu'il n'a pas gagné, 
        # ça veux dire que la grille est remplie completement et c'est un match nul
        if tour > 4: 
            print("match nul")
            break
        
        if symbole == "O":
            grille[demande_case_joueur(grille, "O")] = "O"
        else:
            grille[coup_ordi(grille, "O")] = "O" 
        system(vider_terminal)
        afficher_grille(grille)
        if (is_win(grille)):
            print("le joueur O a gagné !!!")
            break
        tour += 1
    
    if (not demande_rejouer()):
        break
    
    system(vider_terminal)