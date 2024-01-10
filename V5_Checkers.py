def start_checkerboard(board, current_player):
    full_board = []
    print(f"Current Turn: {current_player}")
    print("  0 1 2 3 4 5 6 7")

    for row in range(8):
        row_board = [str(row)]
        for col in range(8):
            if (row + col) % 2 == 0:
                row_board.append("⬛")
            else:
                piece = board[row][col]
                if piece == "🔴" or piece == "🟣":
                    row_board.append(piece)
                else:
                    row_board.append("⬜")
        full_board.append(row_board)

    for row_board in full_board:
        print("".join(row_board))


def display_checkerboard(board, current_player, start_position):
    full_board = []
    print(f"Current Turn: {current_player}")
    print("  0 1 2 3 4 5 6 7")

    for row in range(8):
        row_board = [str(row)]
        for col in range(8):
            if (row + col) % 2 == 0:
                row_board.append("⬛")
            else:
                piece = board[row][col]
                if (col, row) == start_position:
                    row_board.append("🟡")
                elif piece == "🔴" or piece == "🟣" or piece == "🟥" or piece == "🟪":
                    row_board.append(piece)
                elif valid_move(board, (col, row), (col, row), current_player):
                    row_board.append("🟨")
                else:
                    row_board.append("⬜")
        full_board.append(row_board)

    for row_board in full_board:
        print("".join(row_board))


def get_legal_moves(board, start, current_player):
    legal_moves = []
    capturing_moves = []

    for row in range(8):
        for col in range(8):
            end = (col, row)
            if valid_move(board, start, end, current_player):
                legal_moves.append(end)
                if is_capture_move(board, start, end, current_player):
                    capturing_moves.append(end)
    return legal_moves, capturing_moves


def is_capture_move(board, start, end, current_player):
    start_col, start_row = start
    end_col, end_row = end

    if (end_row == start_row - 2 or end_row == start_row + 2) and (end_col - start_col == 2 or end_col - start_col == -2):
        captured_row = (start_row + end_row) // 2
        captured_col = (start_col + end_col) // 2
        opponent_player = "🟣" if current_player == "🔴" else "🔴"
        return board[captured_row][captured_col].startswith(opponent_player)
    return False


def check_winner(board):
    for row in board:
        for piece in row:
            if piece == "🔴" or piece == "🟥":
                return False
            elif piece == "🟣" or piece == "🟪":
                return False
    return True


def valid_move(board, start, end, current_player):
    start_col, start_row = start
    end_col, end_row = end

    if not (0 <= start_row < 8) or not (0 <= start_col < 8) or not (0 <= end_row < 8) or not (0 <= end_col < 8):
        return False

    if board[end_row][end_col] != "":
        return False

    if current_player == "🔴" and end_row == start_row + 1 and (end_col - start_col == 1 or end_col - start_col == -1):
        return True
    elif current_player == "🟣" and end_row == start_row - 1 and (end_col - start_col == 1 or end_col - start_col == -1):
        return True

    opponent_player = "🟣" if current_player == "🔴" else "🔴"

    if board[start_row][start_col] == "🟥":
        if (end_row == start_row - 1 or end_row == start_row + 1) and (end_col - start_col == 1 or end_col - start_col == -1):
            return True

    if (end_row == start_row - 2 or end_row == start_row + 2) and (end_col - start_col == 2 or end_col - start_col == -2):
        captured_row = (start_row + end_row) // 2
        captured_col = (start_col + end_col) // 2
        if board[captured_row][captured_col].startswith(opponent_player):
            return True

    return False


def clear_old_start_position(board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == "🟡":
                board[row][col] = ""


def clear_valid_moves(board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == "🟨":
                board[row][col] = ""


def move_piece(board, start, end, current_player):
    start_col, start_row = start
    end_col, end_row = end

    if valid_move(board, start, end, current_player):
        if (end_row == start_row - 2 or end_row == start_row + 2) and (end_col - start_col == 2 or end_col - start_col == -2):
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2
            board[captured_row][captured_col] = ""

        if current_player == "🔴" and end_row == 7:
            board[end_row][end_col] = "🟥"
        elif current_player == "🟣" and end_row == 0:
            board[end_row][end_col] = "🟪"
        else:
            if board[start_row][start_col] == "🟥" or board[start_row][start_col] == "🟪":
                board[end_row][end_col] = board[start_row][start_col]
            else:
                board[end_row][end_col] = current_player

        board[start_row][start_col] = ""
    else:
        print("Invalid move. Please try again.")

    return board


def starting_input():
    start_col = int(input("Enter the starting column (0-7): "))
    start_row = int(input("Enter the starting row (0-7): "))
    return start_col, start_row


def ending_input():
    end_col = int(input("Enter the ending column (0-7): "))
    end_row = int(input("Enter the ending row (0-7): "))
    return end_col, end_row


def main_game():
    while True:
        current_player = "🔴"

        checkerboard = [
            ["", "🔴", "", "🔴", "", "🔴", "", "🔴"],
            ["🔴", "", "🔴", "", "🔴", "", "🔴", ""],
            ["", "🔴", "", "🔴", "", "🔴", "", "🔴"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["🟣", "", "🟣", "", "🟣", "", "🟣", ""],
            ["", "🟣", "", "🟣", " ", "🟣", "", "🟣"],
            ["🟣", "", "🟣", "", "🟣", "", "🟣", ""]
        ]

        start_checkerboard(checkerboard, current_player)

        while True:
            valid_move_entered = False
            has_captured = False
            while not valid_move_entered:
                start_position = starting_input()
                display_checkerboard(checkerboard, current_player, start_position)
                end_position = ending_input()

                legal_moves, capturing_moves = get_legal_moves(checkerboard, start_position, current_player)
                if end_position in legal_moves:
                    valid_move_entered = True
                    if end_position in capturing_moves:
                        has_captured = True
                else:
                    print("Invalid move. Please try again.")

            checkerboard = move_piece(checkerboard, start_position, end_position, current_player)
            display_checkerboard(checkerboard, current_player, clear_old_start_position(checkerboard))

            while has_captured:
                additional_captures = get_legal_moves(checkerboard, end_position, current_player)[1]
                if additional_captures and is_capture_move(checkerboard, end_position, additional_captures[0], current_player):
                    print("Additional capture possible!")
                    next_end_position = ending_input()
                    checkerboard = move_piece(checkerboard, end_position, next_end_position, current_player)
                    display_checkerboard(checkerboard, current_player, clear_old_start_position(checkerboard))
                    end_position = next_end_position
                else:
                    has_captured = False

            if check_winner(checkerboard):
                print(f"{current_player} wins!")
                break

            if current_player == "🔴":
                current_player = "🟣"
            else:
                current_player = "🔴"

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


main_game()
