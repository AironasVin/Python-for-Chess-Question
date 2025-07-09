# 1. creating a list of valid pieces
valid_pieces = {"pawn", "bishop", "knight", "rook", "queen", "king"}  # a set of valid pieces


def is_valid_piece(piece: str) -> bool:
    return piece.lower() in valid_pieces  # checking if a piece is in the set (is valid)


# 2. creating lists of valid positions, from a-h and from 1-8
valid_position_column = {"a", "b", "c", "d", "e", "f", "g", "h"}
valid_position_row = {"1", "2", "3", "4", "5", "6", "7", "8"}


def is_valid_position(position: str) -> bool:
    if len(position) != 2:  # checking if the input length is exactly 2 to avoid invalid positions like 'a10' or 'a20'.
        return False

    position = position.lower()
    col = position[0]
    row = position[1]

    return col in valid_position_column and row in valid_position_row


# 3. parsing an input -> e.g. from ['knight a5'] to ['knight', 'a5']
def parse_piece_input(input_str: str) -> tuple[str, str] | None:
    input_str = input_str.strip().lower()  # removing unnecessary whitespace
    parts = input_str.split()

    if len(parts) != 2:  # checking if there are 2 parts (piece and position) and returning None if false
        return None
    piece, position = parts

    if piece in valid_pieces and is_valid_position(position):
        return piece, position

    return None


# 4. adding a piece to the board
def add_piece(board: dict[str, str], piece: str, position: str) -> bool:

    if position not in board or board[position] is None:  # checking if position is empty
        board[position] = piece
        return True
    return False  # position is occupied


# 5.1. capture logic for pawn
def get_pawn_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [(-1, 1), (1, 1)]  # pawn moving directions

    for dc, dr in moves:
        c = col + dc
        r = row + dr
        if ord("a") <= c <= ord("h") and 1 <= r <= 8:
            pos = chr(c) + str(r)
            if pos in board and board[pos] is not None:
                captures.append(pos)
    return captures


# 5.2. capture logic for rook
def get_rook_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # rook moving directions

    for dc, dr in moves:
        c, r = col, row
        while True:
            c += dc
            r += dr
            if not (ord("a") <= c <= ord("h") and 1 <= r <= 8):
                break
            pos = chr(c) + str(r)
            if pos in board:
                if board[pos] is not None:
                    captures.append(pos)
                    break
    return captures


# 5.3. capture logic for knight
def get_knight_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [
        (1, 2),
        (2, 1),
        (-1, 2),
        (-2, 1),
        (1, -2),
        (2, -1),
        (-1, -2),
        (-2, -1),
    ]

    for dc, dr in moves:
        new_col = col + dc
        new_row = row + dr
        if ord("a") <= new_col <= ord("h") and 1 <= new_row <= 8:
            pos = chr(new_col) + str(new_row)
            if pos in board and board[pos] is not None:
                captures.append(pos)
    return captures


# 5.4. capture logic for bishop
def get_bishop_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]  # bishop moving directions

    for dc, dr in moves:
        c = col
        r = row
        while True:
            c += dc
            r += dr
            if c < ord("a") or c > ord("h") or r < 1 or r > 8:  # stop if out of bounds
                break
            pos = chr(c) + str(r)
            if pos in board and board[pos] is not None:
                captures.append(pos)
                break
    return captures


# 5.5. capture logic for queen
def get_queen_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for dc, dr in moves:
        c = col
        r = row
        while True:
            c += dc
            r += dr
            if c < ord("a") or c > ord("h") or r < 1 or r > 8:  # stop if out of bounds
                break
            pos = chr(c) + str(r)
            if pos in board and board[pos] is not None:
                captures.append(pos)
                break
    return captures


# 5.6. capture logic for king
def get_king_captures(position: str, board: dict[str, str]) -> list[str]:
    captures = []
    col = ord(position[0])
    row = int(position[1])
    moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for dc, dr in moves:
        c = col + dc
        r = row + dr
        if ord("a") <= c <= ord("h") and 1 <= r <= 8:
            pos = chr(c) + str(r)
            if pos in board and board[pos] is not None:
                captures.append(pos)
    return captures


# 6. Check which black pieces the white piece can capture
def get_capturable_pieces(
    board: dict[str, str], white_piece: str, white_position: str
) -> list[str]:
    if white_position in board and board[white_position] == white_piece:
        if white_piece == "pawn":
            return get_pawn_captures(white_position, board)
        elif white_piece == "rook":
            return get_rook_captures(white_position, board)
        elif white_piece == "bishop":
            return get_bishop_captures(white_position, board)
        elif white_piece == "knight":
            return get_knight_captures(white_position, board)
        elif white_piece == "queen":
            return get_queen_captures(white_position, board)
        elif white_piece == "king":
            return get_king_captures(white_position, board)
    return []


# 7. Main function where you reuse all previous functions and assemble working solution
def main():
    board = {col + row: None for col in "abcdefgh" for row in "12345678"}  # creating an empty board

    while True:
        user_input = input("Enter white piece and position, e.g. 'pawn e2': ").strip().lower()
        parsed = parse_piece_input(user_input)
        if parsed:
            piece, position = parsed
            if add_piece(board, piece, position):
                print(f"{piece} added to {position}")
                white_piece = piece
                white_position = position
                break
            else:
                print("Error: Position is occupied or invalid. Try again")
        else:
            print("Error: Invalid input format or invalid piece/position. Try again")

    black_pieces_count = 0

    while True:
        if black_pieces_count == 16:
            print("Maximum number of black pieces reached")
            break
        user_input = input("Enter black piece and position (or 'done' to finish): ").strip().lower()
        if user_input == "done":
            if black_pieces_count >= 1:
                break
            else:
                print("Error: Add at least one black piece before finishing")
                continue
        parsed = parse_piece_input(user_input)
        if parsed:
            piece, position = parsed
            if add_piece(board, piece, position):
                print(f"{piece} added to {position}")
                black_pieces_count += 1
            else:
                print("Error: Position is occupied or invalid. Try again")
        else:
            print("Error: Invalid input format or invalid piece/position. Try again")

    capturable_positions = get_capturable_pieces(board, white_piece, white_position)

    if capturable_positions:
        print(f"White piece can capture at positions: {', '.join(capturable_positions)}")
    else:
        print("White piece cannot capture any black pieces")


if __name__ == "__main__":
    main()
