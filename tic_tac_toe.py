def display_board(board: list[str]) -> None:
    for row in range(3):
        start = row * 3
        cells = [
            board[position] if board[position] != " " else str(position + 1)
            for position in range(start, start + 3)
        ]
        print(" | ".join(cells))
        if row < 2:
            print("--+---+--")


def choose_symbols() -> tuple[str, str]:
    while True:
        symbol = input("Player 1, choose X or O: ").strip().upper()
        if symbol in ("X", "O"):
            other_symbol = "O" if symbol == "X" else "X"
            return symbol, other_symbol
        print("Please choose X or O.")


def get_player_move(board: list[str], symbol: str) -> int:
    while True:
        choice = input(f"Player {symbol}, choose a position (1-9): ").strip()
        try:
            position = int(choice) - 1
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if position not in range(9):
            print("Please choose a position from 1 to 9.")
        elif board[position] != " ":
            print("That position is already taken.")
        else:
            return position


def has_winner(board: list[str], symbol: str) -> bool:
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    return any(all(board[position] == symbol for position in line) for line in winning_lines)


def is_draw(board: list[str]) -> bool:
    return all(cell != " " for cell in board)


def main() -> None:
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = [" "] * 9
    player_one, player_two = choose_symbols()
    players = (player_one, player_two)
    turn = 0

    while True:
        display_board(board)
        symbol = players[turn % 2]
        position = get_player_move(board, symbol)
        board[position] = symbol

        if has_winner(board, symbol):
            display_board(board)
            print(f"Player {symbol} wins!")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        turn += 1


# Tic-tac-toe game
if __name__ == "__main__":
    main()
