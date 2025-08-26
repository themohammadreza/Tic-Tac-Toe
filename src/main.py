import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self):
        return "X" if random.randint(0, 1) == 0 else "O"

    def player_movement(self, cell, player):
        self.board[cell] = player

    def has_anyone_won(self, player):
        win_situations = [
                (1, 2, 3), (4, 5, 6), (7, 8, 9), # row 
                (1, 4, 7), (2, 5, 8), (3, 6, 9), # col
                (1, 5, 9), (3, 5, 7), # cross
            ]
        for situation in win_situations:
            if self.board[situation[0]] == self.board[situation[1]] == self.board[situation[2]] == player:
                return True
        return False

    def swap_player_turn(self):
        self.player_turn = "X" if self.player_turn == "O" else "O"

    def is_board_filled(self):
        return ' ' not in self.board[1:]

    def show_board(self):
        print('\n')
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]} ')
        print('-----------')
        print(f' {self.board[4]} | {self.board[5]} | {self.board[6]} ')
        print('-----------')
        print(f' {self.board[7]} | {self.board[8]} | {self.board[9]} ')
        print('\n')

    def show_board_positions(self):
        print('\nCell positions:')
        print(' 1 | 2 | 3 ')
        print('-----------')
        print(' 4 | 5 | 6 ')
        print('-----------')
        print(' 7 | 8 | 9 \n')

    def start_game(self):
        print("Welcome to Tic Tac Toe!")
        self.show_board_positions()
        while True:
            self.show_board()
            try:
                cell = input(f'Player {self.player_turn} turn. Enter Your Cell Number: (q to quit)')
                if cell.lower() == 'q':
                    print("Thanks for playing!")
                    break
                else:
                    cell = int(cell)
                    if cell in range (1, 10) and self.board[cell] == ' ':
                        self.player_movement(cell, self.player_turn)

                        if self.has_anyone_won(self.player_turn):
                            print(f'Player {self.player_turn} Wins!')
                            break
                        
                        if self.is_board_filled():
                            print("It's a Tie!")
                            break

                        self.swap_player_turn()
                    
                    else:
                        print('Invalid Input! Please Try Again.')
                    
            except ValueError:
                print('Invalid Cell Number! Select Between 1 to 9: ')


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()