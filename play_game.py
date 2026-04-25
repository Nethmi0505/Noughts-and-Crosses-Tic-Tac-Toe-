import random
import os.path
import json

random.seed()

def draw_board(game_board):
    
    print("-------------")
    for row in game_board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

 
def welcome(game_board):
    
    print("Welcome to Tic-Tac-Toe! Ready to play")
    draw_board(game_board)

 
def initialise_board(game_board):
   
    return [[' ' for _ in range(3)] for _ in range(3)]

def get_player_move(game_board):
    
    while True:
        try:
            player_move = int(input("Enter your move (1-9): "))
            if player_move < 1 or player_move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            row, col = divmod(player_move - 1, 3)  
            if game_board[row][col] == ' ':
                return row, col
            else:
                print("Cell already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

 
def choose_computer_move(game_board):
    
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_board[row][col] == ' ':
            return row, col

 
def check_for_win(game_board, player_mark):
    
    for row in range(3):
        if all([cell == player_mark for cell in game_board[row]]):
            return True
    for col in range(3):
        if all([game_board[row][col] == player_mark for row in range(3)]):
            return True
    if all([game_board[i][i] == player_mark for i in range(3)]) or \
       all([game_board[i][2 - i] == player_mark for i in range(3)]):
        return True
    return False

 
def check_for_draw(game_board):
    
    return all([cell != ' ' for row in game_board for cell in row])

 
def play_game(game_board):
    
    game_board = initialise_board(game_board)
    welcome(game_board)
    is_player_turn = True  
    while True:
        if is_player_turn:
            row, col = get_player_move(game_board)
            game_board[row][col] = 'X'
            draw_board(game_board)
            if check_for_win(game_board, 'X'):
                print("You win!")
                return 1
        else:
            row, col = choose_computer_move(game_board)
            game_board[row][col] = 'O'
            draw_board(game_board)
            if check_for_win(game_board, 'O'):
                print("Computer wins!")
                return -1
        if check_for_draw(game_board):
            draw_board(game_board)
            print("It's a draw!")
            return 0
        is_player_turn = not is_player_turn

 
def menu():
    
    print("1 - Play the game")
    print("2 - Save score in leaderboard")
    print("3 - Load and display leaderboard")
    print("q - Quit")
    user_choice = input("Enter your choice: ")
    return user_choice

 
def load_scores():
    
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

 
def save_score(player_score):
    
    player_name = input("Enter your name: ")
    leaderboard = load_scores()
    leaderboard[player_name] = player_score
    with open('leaderboard.txt', 'w', encoding='utf-8') as file:
        json.dump(leaderboard, file)

 
def display_leaderboard(leaderboard):
    
    if leaderboard:
        print("Leaderboard:")
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_leaderboard:
            print(f"{name}: {score}")
    else:
        print("No scores available.")
