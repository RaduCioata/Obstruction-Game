import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.user_interface import UI
from domain.game import *
from domain.board import *

lines = 0
columns = 1
option = 2

tempArray = UI.printMenu()
board = Board(tempArray[lines],tempArray[columns])
game = Game(board)
game_ui = UI(board, game, tempArray[lines], tempArray[columns], tempArray[option])
game_ui.start()