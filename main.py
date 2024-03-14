import chess
import random

class RandomBot:
    def choose_move(self, board):
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)

if __name__ == "__main__":
    bot = RandomBot()
    board = chess.Board()

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = bot.choose_move(board)
            board.push(move)
            print("White's move:", move.uci())
        else:
            move = input("Enter your move (in UCI notation): ")
            move = chess.Move.from_uci(move)
            board.push(move)
    
    print("Game Over")
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Insufficient material!")
    elif board.is_seventyfive_moves():
        print("Seventy-five moves rule!")
    elif board.is_fivefold_repetition():
        print("Fivefold repetition!")
