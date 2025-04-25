
# 🎮 Tic-Tac-Toe

A simple yet engaging implementation of the classic Tic-Tac-Toe game, developed as part of the CS492 Special Topics in Computer Science course. This project offers both command-line and graphical user interface (GUI) versions, allowing players to compete against each other or challenge a computer opponent.

## 📌 Features

- **Two Game Modes**:
  - **Two-Player Mode**: Play against a friend.
  - **Single-Player Mode**: Challenge a computer opponent with two difficulty modes.
- **User Interfaces**:
  - **Command-Line Interface (CLI)**: Simple text-based gameplay.
  - **Graphical User Interface (GUI)**: Interactive GUI using Tkinter.
- **Robust Gameplay Mechanics**:
  - Input validation to prevent invalid moves.
  - Automatic detection of game outcomes: win, lose, or tie.
  - Option to restart the game after completion.

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system.

### Steps to Run the Game

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ehrg1/Tic-Tac-Toe.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Tic-Tac-Toe
   ```

3. **Run the Game**:

   - **For CLI Version**:

     ```bash
     python Tic-Tac-Toe.py
     ```

   - **For GUI Version**:

     ```bash
     python Tic-Tac-Toe-GUI.py
     ```

## 🎮 How to Play

1. **Choose Game Mode**:
   - Select between two-player mode or single-player mode against the computer.

2. **Gameplay**:
   - Players take turns marking the 3x3 grid with their respective symbols (X or O).
   - The first player to align three of their symbols horizontally, vertically, or diagonally wins.
   - If all cells are filled without a winning combination, the game ends in a tie.

3. **Post-Game Options**:
   - After a game concludes, players have the option to restart or exit.

## 📁 Project Structure

```
Tic-Tac-Toe/
├── Tic-Tac-Toe.py         # Command-line version of the game
├── Tic-Tac-Toe-GUI.py     # GUI version using Tkinter
└── README.md              # Project documentation
```

## 📚 Technologies Used

- **Programming Language**: Python 3
- **GUI Library**: Tkinter (for the GUI version)

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the game, fix bugs, or add new features, please fork the repository and submit a pull request.

