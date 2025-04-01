from domain.game import *
from domain.board import *
from domain.square import *
import time
import os


class UI:
    def __init__(self, board, game, lines, columns, option):
        self.board = board
        self.game = game
        self.lines = lines
        self.columns = columns
        self.option = option

    def clear_screen(self):
        """Clear the console screen based on operating system"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_tutorial(self):
        """Display a tutorial with nice graphics for the Obstruction game"""
        self.clear_screen()
        print("\n" + "="*60)
        print("            WELCOME TO OBSTRUCTION GAME!            ")
        print("="*60 + "\n")
        
        print("HOW TO PLAY:\n")
        print("1. Players take turns placing marks on the board")
        print("2. After placing a mark, that square and all adjacent squares")
        print("   become blocked and cannot be used")
        print("3. The player who cannot make a move loses\n")
        
        print("GAME SYMBOLS:")
        print("   X  - Your marks")
        print("   O  - Computer's marks")
        print("   -  - Blocked squares")
        print("      - Empty squares (available for moves)\n")
        
        # Sample board to show gameplay
        print("EXAMPLE BOARD:")
        print("    1   2   3  ")
        print("  +-----------+")
        print("1 | X | - | - |")
        print("  +-----------+")
        print("2 | - | - | - |")
        print("  +-----------+")
        print("3 | - | - | O |")
        print("  +-----------+\n")
        
        print("HOW TO ENTER MOVES:")
        print("   When prompted, enter coordinates as: row,column")
        print("   Example: '1,2' places your mark at row 1, column 2\n")
        
        input("Press Enter to start the game... ")
        self.clear_screen()

    @staticmethod
    def printMenu():
        print("\n" + "="*40)
        print("        OBSTRUCTION GAME SETUP        ")
        print("="*40 + "\n")
        
        while True:
            try:
                l = input("Please give the size of the table (rows,columns): ")
                lines = int(l[0:l.find(',')])
                columns = int(l[l.find(',') + 1:])
                break
            except ValueError:
                print("\nInvalid size. Ex: 2,3  -  please insert integers\n")

        if l.find(',') == -1:
            print("\nInvalid size. Ex: 2,3\n")
            l = input("Please give the size of the table (rows,columns): ")

        print("\n" + "-"*40)
        o = input("\nPress 1 if you want to start, 2 if you want the computer to start: ")
        while o != '1' and o != '2':
            print("\nPlease press 1 or 2\n")
            o = input("Press 1 if you want to start, 2 if you want the computer to start: ")
        return [lines, columns, o]

    def start(self):
        # Display tutorial at the beginning
        self.display_tutorial()
        
        ok = 0
        cpu = 1
        if self.option == '2':
            print("\nComputer moves first...\n")
            time.sleep(1)
        contor = 0
        square = Square(0, 0)
        
        while not self.board.isWon(self.lines, self.columns):
            if self.option == '2':
                if self.lines % 2 == 1 and self.columns % 2 == 1:
                    if cpu != 0:
                        contor = contor + 1
                        self.game.moveComputer(self.lines, self.columns, contor, square)
                else:
                    if cpu != 0:
                        contor = contor + 1
                        self.game.moveRandomEf(self.lines, self.columns)
                print("\nCurrent board state:")
                print(self.board)
                print()

                if not self.board.isWon(self.lines, self.columns):
                    while True:
                        try:
                            l = input("Your turn! Enter position (row,column): ")
                            x = int(l[0:l.find(',')])
                            y = int(l[l.find(',') + 1:])
                            break
                        except ValueError:
                            print("\nInvalid data format. Please enter as row,column (e.g., 2,3)\n")

                    try:
                        square = Square(x, y)
                        self.game.movePlayer(square, self.lines, self.columns)
                        cpu = 1
                    except ValueError as ve:
                        cpu = 0
                        print("\nError: " + str(ve) + "\n")
            else:
                print("\nCurrent board state:")
                print(self.board)
                print()
                
                while True:
                    try:
                        l = input("Your turn! Enter position (row,column): ")
                        x = int(l[0:l.find(',')])
                        y = int(l[l.find(',') + 1:])
                        break
                    except ValueError:
                        print("\nInvalid data format. Please enter as row,column (e.g., 2,3)\n")

                try:
                    square = Square(x, y)
                    self.game.movePlayer(square, self.lines, self.columns)
                    cpu = 1
                    ok = 1
                except ValueError as ve:
                    cpu = 0
                    print("\nError: " + str(ve) + "\n")
                    
                if cpu != 0 and self.board.isWon(self.lines, self.columns) == False:
                    print("\nComputer is thinking...\n")
                    time.sleep(0.5)
                    contor = contor + 1
                    self.game.moveRandomEf(self.lines, self.columns)
                    ok = 0

        print("\nFinal board state:")
        print(self.board)
        print()

        print("="*40)
        if ok == 0:
            print("     GAME OVER - COMPUTER WINS!     ")
        else:
            print("       GAME OVER - YOU WIN!       ")
        print("="*40 + "\n")