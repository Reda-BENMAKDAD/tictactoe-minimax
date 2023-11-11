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
                print("t'es fou ou quoi la case est déja prise")
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
            
def is_win(grille):
    """
    Fonction qui vérifie si il y'a un gagnant dans la positioncls
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
        
while True: # on créer une boucle while, pour que si l'utilisateur veut rejouer, on recommance
    grille = [1, 2, 3, 4, 5, 6, 7, 8, 9] # la grille qui vas stocker l'état de notre jeu
    print("player 1 -> X")
    print("player 2 -> O")
    afficher_grille(grille)
    tour = 1
    while True:
        grille[demande_case_joueur(grille, "X")] = "X"
        system(vider_terminal)
        afficher_grille(grille)
        if (is_win(grille)):
            print("le joueur X a gagné !!!")
            break
        # si on est arrivé au 4eme tour et que le joueur X a joué et qu'il n'a pas gagné, 
        # ça veux dire que la grille est remplie completement et c'est un match nul
        if tour > 4: 
            print("match nul")
            break
        grille[demande_case_joueur(grille, "O")] = "O"
        system(vider_terminal)
        afficher_grille(grille)
        if (is_win(grille)):
            print("le joueur O a gagné !!!")
            break
        tour += 1
    
    if (not demande_rejouer()):
        break
    
    system(vider_terminal)

        

    

    