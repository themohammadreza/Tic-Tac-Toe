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
        print("\n")
        rows = [[self.board[i+j] for i in range(1, 4)] for j in range(0, 7, 3)]
        for row in rows:
            print(row)
        print("\n")

    def start_game(self):
        while True:
            self.show_board()
            try:
                cell = input(f'Player {self.player_turn} turn. Enter Your Cell Number: (q to quit)')
                if cell == 'q'.lower():
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