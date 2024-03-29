import copy

PLAYER0 = 0
PLAYER1 = 1

moves = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
_add_ = lambda x,y: tuple(map(sum, zip(x, y)))
on_board = lambda x, y: (x >= 0) and (x < 5) and (y >= 0) and (y < 5)
occupied = lambda pawns, location: (location in pawns[0]) or (location in pawns[1])

class Player:
    def __init__(self, side):
        self.side = side
        self.COUNTER = 0
        self.tactic_depth = 2

    def evaluate(self, game): # c'est une position de jeu à considérer après l'action du joueur Player.
        def pawn_score(pawn, mult):
            h = game.board[pawn[0]][pawn[1]]
            return (h*(h!=3) + 100*(h==3)) * mult
        return pawn_score(game.pawns[self.side][0], 1.0) + \
               pawn_score(game.pawns[self.side][1], 1.0) + \
               pawn_score(game.pawns[1 - self.side][0], -1.0) + \
               pawn_score(game.pawns[1 - self.side][1], -1.0)

    def min_play(self, game, depth):
        if game.end_of_game() or (depth == 0):
          return self.evaluate(game)
        return min(map(lambda s: self.max_play(s, depth - 1),
                   game.list_possible_states()))

    def max_play(self, game, depth):
        self.COUNTER = self.COUNTER + 1
        print(self.COUNTER, depth)
        if game.end_of_game() or (depth == 0):
          return self.evaluate(game)
        return max(map(lambda s: self.min_play(s, depth - 1),
                   game.list_possible_states()))

    def play(self, game):
       return max(
                map(lambda move: (move, self.min_play(move, self.tactic_depth)),
                    game.list_possible_states()),
                    key = lambda x: x[1])[0]


class Santorini:
    def __init__(self):
        # constructeur
        self.pawns = [[(1,2),(2,1)],[(2,3),(3,2)]]
        self.board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.EOG = False
        self.PLAYER_TO_PLAY = PLAYER0

    def update(self, game):
        self.pawns = game.pawns
        self.board = game.board

    def end_of_game(self):
        return True in [self.board[p[0]][p[1]] == 3 for p in self.pawns[0]+self.pawns[1]]

    def move_allowed(self, position_start, position_end):
        (a, b) = position_start
        (x, y) = position_end
        level_4 = lambda x, y: self.board[x][y] < 4
        jump_max_1 = lambda x, y, a, b: self.board[x][y] - self.board[a][b] <= 1
        return on_board(x, y) and not(occupied(self.pawns, position_end)) and level_4(x, y) and jump_max_1(x, y, a, b)

    def build_allowed(self, board_location):
        (x, y) = board_location
        level_4 = lambda x, y: self.board[x][y] < 4
        return  on_board(x, y) and level_4(x, y) and not(occupied(self.pawns, board_location))

    def list_possible_states(self):
        # return a list of possible game states.
        def aux(game, player, pawn_ix):
            possible_states = []
            position_start = game.pawns[player][pawn_ix]
            pawn_moves = filter(lambda m: game.move_allowed(position_start, m),
                                  [_add_(position_start, x) for x in moves])
            for pawn_move in pawn_moves:
                game.pawns[player][pawn_ix] = pawn_move # modifying the pawn vector.
                builds = filter(game.build_allowed, [_add_(pawn_move, x) for x in moves])
                for build in builds:
                    (a, b) = build
                    gclone = copy.deepcopy(game) # c'est moche, mais ça ira pour l'instant.
                    gclone.board[a][b] += 1
                    possible_states.append(gclone)
            game.pawns[player][pawn_ix] = position_start  # resetting the pawn vector.
            return possible_states
        return aux(self, self.PLAYER_TO_PLAY, 0) + aux(self, self.PLAYER_TO_PLAY, 1)


def __main__():
    # fonction qui simule un match entre 2 joueurs.
    player0 = Player(PLAYER0)
    player1 = Player(PLAYER1)
    game = Santorini()
    # player.play(game)
    while not game.end_of_game():
        player = player0 if game.PLAYER_TO_PLAY == 0 else player1
        game.update(player.play(game)) # modifie l'état du jeu.
        game.PLAYER_TO_PLAY = 1 - player.side
    return not game.PLAYER_TO_PLAY

# implémenter alpha beta pruning.
# implémenter multiprocessing.
# passer le code en Cython ou en Go.
