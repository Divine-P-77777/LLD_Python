from typing import List


class ChessPiece:
    def __init__(self, name: str, position: str, color: str):
        self.name = name
        self.position = position
        self.color = color

    def display(self):
        return f"{self.color} {self.name} is at {self.position}"


class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []

    def add_piece(self, piece: ChessPiece):
        self.pieces.append(piece)

    def display_board(self):
        print("\nBoard State")
        for piece in self.pieces:
            print(piece.display())


# Create chess pieces
piece1 = ChessPiece("King", "e2", "Black")
piece2 = ChessPiece("Queen", "a1", "Black")
piece3 = ChessPiece("King", "c3", "White")
piece4 = ChessPiece("Queen", "d2", "White")

# Original board
chess_board = ChessBoard()

chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)

chess_board.display_board()


# Manually copy pieces
new_chess_board = ChessBoard()

for piece in chess_board.pieces:
    new_chess_board.add_piece(piece)

new_chess_board.display_board()




# Problems:
# 1. Manual Copying: Requires explicitly iterating through all pieces.
# 2. Repetitive Logic: Copying logic must be repeated wherever cloning is required.
# 3. Maintenance: Changes to object structure can make copying more complicated.
# Important
#  This bad example copies references, not independent objects. Both boards share the same ChessPiece instances.