import numpy as np

PLAYER0 = 0
PLAYER1 = 1

class Player:
    def evaluate_position():
        # fonction qui évalue une position
        # MinMax aglorightm https://en.wikipedia.org/wiki/Minimax
        # avec une évaluation naive en fonction de la hauteur des
        # pion du joueur.
        return 0

    def play(possible_moves, evaluate):
            # fonction détermine le prochain coup optimal.
            evaluations = map(possible_moves, evaluate)
            ix = np.argmax(evaluations)
            return possible_moves[ix]


class Santorini:
    def __init__(self):
        # constructeur
        self.moves = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        self.pawns = [[(2,3),(3,2)],[(3,4),(4,3)]]
        self.board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.EOG = False
        self.PLAYER_TO_PLAY = PLAYER0

    def move_allowed(position_start, position_end):
        (i,j) = position_start
        (a,b) = position_end
        on_board = (a>-1) and (a<6) and (b>-1) and (b<6)
        not_occupied = not(x in self.pawns[0]) and not(x in self.pawns[1])
        level_4 = self.board[a][b] < 4
        jump_max_1 = self.board[a][b] - self.board[i][j] <= 1
        return on_board and not_occupied and level_4 and jump_max_1

    def list_possible_moves(self):
        # return a list of reachable board states.
        position_start = pawns[self.PLAYER_TO_PLAY][0]
        pawn_moves = [tuple(map(sum, zip(position_start, x))) for x in self.moves]

    def game():
        # fonction qui simule un match entre 2 joueurs.
        while not EOG:
            pass
            # next player joue.
        return not PLAYER_TO_PLAY


def run():
    player1 = Player()
    player2 = Player()
    s = Santorini(player1, player2)
    winner = s.game()

# faire jouer 1 milion de parties
# recorder les configurations
# classer les configurations suivant qu'elles appartiennent à un arbre gagnant ou perdant
# incorporer l'histoire dans la fonction d'évaluation
