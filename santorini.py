import numpy as np

# représentation d'un joueur: une fonction d'évaluation.
class Player():
    def evaluate_position():
        # fonction qui évalue une position
        return 0

    def play(possible_moves, evaluate):
            # fonction détermine le prochain coup optimal.
            evaluations = map(possible_moves, evaluate)
            ix = np.argmax(evaluations)
            return possible_moves[ix]


class Santorini:
    # représentation d'un état du jeu
    # - matrice 5x5, avec niveau 0 à 4
    # - position joueur 0, 2x tuple
    # - position joueur 1, 2x tuple.
    # - PLAYER_TO_PLAY: un int, 0 ou 1, qui indique à qui le tour.
    # - EOG: boolean qui indique si le jeu est terminé ou pas.
    matrix board

    # un mouvement:
    # - matrice 5x5, avec niveau 0 ou 1
    # - mouvement joueur 1, 2x tuple
    # - mouvement joueur 2, 2x tuple

    def Santorini(player1, player2):
        # constructeur

    def list_possible_moves():
        # fonction qui liste les mouvements possibles
        return []

    def game():
        # fonction qui simule un match entre 2 joueurs.
        while not EOG:
            # next player joue.
        return not PLAYER_TO_PLAY


def run():
    player1 = Player()
    player2 = Player()
    s = Santorini(player1, player2)
    winner = s.game()
