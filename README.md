# Obstruction Game

Welcome to the Obstruction Game! This is a two-player strategy game where players take turns placing marks on a grid. The goal is to block your opponent from making a move.

## How to Play

1. **Objective**: The player who cannot make a move loses the game.
2. **Gameplay**:
   - Players take turns placing their marks (X for player, O for computer) on empty cells.
   - After placing a mark, that cell and all adjacent cells (horizontally, vertically, and diagonally) become blocked.
   - The game continues until a player cannot make a move.

## Game Symbols

- **X**: Your marks
- **O**: Computer's marks
- **-**: Blocked squares
- **Empty**: Available for moves

## Example Board

```
    1   2   3
  +---+---+---+
1 | X | - | - |
  +---+---+---+
2 | - | - | - |
  +---+---+---+
3 | - | - | O |
  +---+---+---+
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/obstruction-game.git
   cd obstruction-game
   ```

2. **Run the game**:
   Ensure you have Python installed, then execute:
   ```bash
   python Main/main.py
   ```

## Requirements

- Python 3.x

## Project Structure

- `Main/main.py`: Entry point for the game.
- `ui/user_interface.py`: Handles user interaction and game display.
- `domain/board.py`: Manages the game board and moves.
- `domain/game.py`: Contains game logic and computer's strategy.
- `domain/square.py`: Represents a square on the board.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

# Obstruction-Game
