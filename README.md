# TicTacToe with minimax algorithm
> this is a simple TicTacToe game made with python, that uses my implementation of the minimax algorithm to play against the computer.

## TicTacToe implementation
The making of the TicTacToe game itself is pretty straight forward, i don't think i need to explain it, any first year CS student can make it.
The game state is respresented by a 1 dimensional array that holds 9 numbers at first, each number represents a cell in the board,
then a loop does the following repeatedly:
1. prints the board
2. asks user 1 to enter the number of the cell where he want to play
3. checks if the cell is valid and empty, if not it goes to step 2 until it gets a valid input
4. updates the game state with the new move
4. checks if the game is over, if yes it prints the winner or "tie" and exits the loop, if not clears the screen and prints updated board
5. does the same for user 2 and goes back to step

> if you want to play against a friend run
```bash
python3 contre_humain.py
```
> if you want to play against the computer run
```bash
python3 contre_ordi.py computer
```

## Minimax algorithm

The minimax algorithm is an algorithm used to find the best move in a zero sum game, it is used in games like chess, checkers, tic tac toe, etc... 
There are many great ressources online to learn about this algorithm, here i will explain my implementation and how i used it for my tictactoe game. two great videos i found that explain the subject are :
- [Algorithms Explained – minimax and alpha-beta pruning](https://youtu.be/l-hh51ncgDI?si=XznxxhZCMncEjsY-)

- [The Coding Train video about TicTacToe AI](https://youtu.be/trKjYdBASyQ?si=9Oax3nTOLrYQrBQt)


### How the algorithm works
the algorithm is a recursive function that takes in as parameters __the current game state__, __the current player__, __and the maximum depth of the recursion__.
how does this function return the best move ? it simply plays the best moves for the current player, and then the opponent, alternating like that starting from the current game state, until the game is over or the maximum depth is reached, it then returns who won, by that we have calculations about if we play a move what will happen ? -> will we win ? lose ? or tie ? and we can choose the best move based on that.

## My implementation
> i wrote my code in french because i was doing it with some french speaking friends, but the code is so simple that you'll be able to understand it even if you don't speak french.

First thing we need in a minimax algorithm is a function that evaluates the current position of the game, it should return who is winning or if the game is a tie. for that i created a `evaluer_position` function that takes in the current game array and returns 1 if X is winning, -1 if O is winning, and 0 if the game is a tie.
```python
def evaluer_position(grille):
    if ((grille[0] == grille[1] == grille[2] == "X") or
        (grille[3] == grille[4] == grille[5] == "X") or
        (grille[6] == grille[7] == grille[8] == "X") or
        (grille[0] == grille[3] == grille[6] == "X") or
        (grille[1] == grille[4] == grille[7] == "X") or
        (grille[2] == grille[5] == grille[8] == "X") or
        (grille[0] == grille[4] == grille[8] == "X") or
        (grille[2] == grille[4] == grille[6] == "X")):
        return 1

    elif ((grille[0] == grille[1] == grille[2] == "O") or
          (grille[3] == grille[4] == grille[5] == "O") or
          (grille[6] == grille[7] == grille[8] == "O") or
          (grille[0] == grille[3] == grille[6] == "O") or
          (grille[1] == grille[4] == grille[7] == "O") or
          (grille[2] == grille[5] == grille[8] == "O") or
          (grille[0] == grille[4] == grille[8] == "O") or
          (grille[2] == grille[4] == grille[6] == "O")):
        return -1
    
    else:
        return 0
```
This function checks if a symbole repeats three times in a row in the board and checks whick symbole repeats and returns 1 if it's X, 0 if it's a tie, and -1 if it's O.

Now that we can evaluate the position, we need to play the best move again and again for each player until the game is over or the maximum depth is reached, for that i created a `minimax` function that takes in the current game state, the current player, and the maximum depth, and returns the best move for the current player.
```python
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
```
First we check if we reacehed the maximum depth or if the game is over, if yes we return the evaluation of the position (who is winning at the end), if not we get all the possible moves for the current player, and we loop through them, for each move we play it and call the minimax function again with the new game state, and we alternate between maximizing and minimizing (we want to go towards 1 meaning X is playing and wants to win, or we want to go towards -1 meaning O is playing), and we return the best move for the current player.

Now all there's to do is call the minimax function on all the moves available for the computer, and choose the one that returns the highest value if the computer is playing as X or the lowest value if the computer is playing as O.


# Conclusion
This was a fun project to do, i learned a lot about the minimax algorithm, and i hope you learned something too with me about how computers play games.







