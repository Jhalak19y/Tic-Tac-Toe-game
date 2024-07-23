def print_board(board):
  # Display the board with X, O, or numbers
  print("\n" + " | ".join(str(cell) for cell in board[:3]))
  print("--|---|--")
  print(" | ".join(str(cell) for cell in board[3:6]))
  print("--|---|--")
  print(" | ".join(str(cell) for cell in board[6:]) + "\n")

def check_win(board, player):
  # Define winning combinations
  wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
          (0, 3, 6), (1, 4, 7), (2, 5, 8), 
          (0, 4, 8), (2, 4, 6)]
  # Check if the player has a winning combination
  for a, b, c in wins:
      if board[a] == board[b] == board[c] == player:
          return True
  return False

def main():
  # Initialize the game board and player turn
  board = list(range(9))
  current_player = 'X'

  print("Welcome to Tic Tac Toe")

  while True:
      print_board(board)
      try:
          move = int(input(f"Player {current_player}, enter your move (0-8): "))
          if board[move] not in ['X', 'O']:
              board[move] = current_player
          else:
              print("Cell already taken. Try again.")
              continue
      except (IndexError, ValueError):
          print("Invalid move. Enter a number between 0 and 8.")
          continue

      if check_win(board, current_player):
          print_board(board)
          print(f"Player {current_player} wins!")
          break

      if all(cell in ['X', 'O'] for cell in board):
          print_board(board)
          print("It's a draw!")
          break

      current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  main()
