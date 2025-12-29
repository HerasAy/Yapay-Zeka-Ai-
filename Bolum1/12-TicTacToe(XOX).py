import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 Tahta
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        # Satır kontrolü
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]): return True

        # Sütun kontrolü
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]): return True

        # Çapraz kontrolü
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]): return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]): return True
        return False

def minimax(position, maximize_player):
    """
    Özyinelemeli (Recursive) Minimax Fonksiyonu
    """
    player = 'X' if maximize_player else 'O' # X biziz (MAX), O rakip (MIN)

    # 1. TEMEL DURUM (Base Case): Oyun bitti mi?
    if position.current_winner == 'O': return {'score': -1 * (len(position.available_moves()) + 1), 'position': None}
    if position.current_winner == 'X': return {'score': 1 * (len(position.available_moves()) + 1), 'position': None}
    if not position.empty_squares():   return {'score': 0, 'position': None} # Beraberlik

    if maximize_player:
        best = {'score': -math.inf, 'position': None} # En kötüden başla

        for possible_move in position.available_moves():
            # 1. Hamleyi yap
            position.make_move(possible_move, 'X')

            # 2. Rekürsif çağrı (Sıra MIN'e geçer)
            sim_score = minimax(position, False)

            # 3. Hamleyi geri al (Backtrack)
            position.board[possible_move] = ' '
            position.current_winner = None
            sim_score['position'] = possible_move

            # 4. En iyisini seç (MAX)
            if sim_score['score'] > best['score']:
                best = sim_score
        return best

    else: # Minimize Player (Rakip)
        best = {'score': math.inf, 'position': None}

        for possible_move in position.available_moves():
            position.make_move(possible_move, 'O')
            sim_score = minimax(position, True) # Sıra MAX'a geçer
            position.board[possible_move] = ' '
            position.current_winner = None
            sim_score['position'] = possible_move

            if sim_score['score'] < best['score']:
                best = sim_score
        return best
