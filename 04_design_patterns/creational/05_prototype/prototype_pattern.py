from typing import List
import copy


# ==================================
# 1. PROTOTYPE
# ==================================

class ChessPiece:

    def __init__(self, name: str, position: str, color: str):
        self.name = name
        self.position = position
        self.color = color

    def display(self):
        return f"{self.color} {self.name} is at {self.position}"

    def clone(self):
        return copy.deepcopy(self)


# ==================================
# 2. CHESS BOARD
# ==================================

class ChessBoard:

    def __init__(self):
        self.pieces: List[ChessPiece] = []

    def add_piece(self, piece: ChessPiece):
        self.pieces.append(piece)

    def display_board(self):
        print("\nBoard State")

        for piece in self.pieces:
            print(piece.display())

    def clone(self):
        return copy.deepcopy(self)


# ==================================
# 3. CLIENT
# ==================================

piece1 = ChessPiece("King", "e2", "Black")
piece2 = ChessPiece("Queen", "a1", "Black")
piece3 = ChessPiece("King", "c3", "White")
piece4 = ChessPiece("Queen", "d2", "White")

# Original Board
chess_board = ChessBoard()

chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)

chess_board.display_board()


# Clone the entire board
new_chess_board = chess_board.clone()

print("\nCloned Board:")
new_chess_board.display_board()


# Verify independent objects
print("\nOriginal Board ID:", id(chess_board))
print("Cloned Board ID:", id(new_chess_board))

print("\nOriginal Piece ID:", id(chess_board.pieces[0]))
print("Cloned Piece ID:", id(new_chess_board.pieces[0]))


# Modify cloned board
new_chess_board.pieces[0].position = "e4"

print("\nAfter Modification:")

chess_board.display_board()
new_chess_board.display_board()





# Key Observation:
# - Original and cloned boards have different IDs.
# - Their corresponding chess pieces also have different IDs.
# - Modifying a piece in the cloned board doesn't affect the original board.