# 🎯 Number Guessing Game (CLI Version)

A simple Command Line Interface (CLI) number guessing game built with Python.

The computer randomly selects a number between 1 and 100, and the player must guess the number within a limited number of attempts depending on the selected difficulty level.

---

## 📌 Features

- Random number generation between 1 and 100
- Three difficulty levels:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Input validation
- Hints after each guess (Higher or Lower)
- Attempt counter
- Replay option after each game
- Cross-platform terminal clearing

---

## 🕹️ How the Game Works

1. The game starts with a welcome message and instructions.
2. The player selects a difficulty level.
3. The computer generates a random number.
4. The player enters guesses.
5. After each incorrect guess, the game tells the player whether the correct number is higher or lower.
6. The game ends when:
   - The player guesses correctly (Win 🎉)
   - The player runs out of chances (Lose ❌)
7. The player can choose to play again.

---

## 🛠️ Technologies Used

- Python 3
- `random` module (for number generation)
- `os` module (for clearing terminal)
- `time` module (for delay effects)

---

## ▶️ How to Run the Game

1. Make sure Python 3 is installed.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Run the command:

```bash
python filename.py
