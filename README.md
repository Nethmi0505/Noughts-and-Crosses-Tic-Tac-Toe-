# ❌⭕ Noughts and Crosses (Tic-Tac-Toe) — Python CLI Game

A terminal-based **Tic-Tac-Toe** game written in Python, featuring player vs. computer gameplay, score tracking, and a persistent leaderboard system.

---

## 🎮 Features

- **Player vs. Computer** — You play as `X`, the computer plays as `O`
- **Interactive CLI Board** — A clean, readable 3×3 grid rendered in the terminal
- **Win / Draw Detection** — Checks rows, columns, and both diagonals after every move
- **Score Tracking** — Accumulate a running score across multiple rounds (`+1` win, `-1` loss, `0` draw)
- **Persistent Leaderboard** — Save and load scores from `leaderboard.txt` (JSON format)
- **Menu-Driven Interface** — Simple numbered menu to navigate between game modes

---

## 📁 Project Structure

```
Python 2/
├── noughtsandcrosses.py   # Core game logic (board, moves, win checks, leaderboard)
├── play_game.py           # Entry point — main loop and menu navigation
└── leaderboard.txt        # Persistent score storage (JSON)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the Game

```bash
git clone https://github.com/your-username/noughts-and-crosses.git
cd noughts-and-crosses
python play_game.py
```

---

## 🕹️ How to Play

1. Run `play_game.py`
2. The board positions are numbered **1–9** (left to right, top to bottom):

```
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
```

3. Use the menu to:
   - `1` — Start a new game
   - `2` — Save your score to the leaderboard
   - `3` — View the leaderboard
   - `q` — Quit

---

## 📊 Scoring

| Result       | Score |
|--------------|-------|
| You win      | +1    |
| Computer wins| -1    |
| Draw         |  0    |

Scores accumulate across rounds in a single session and can be saved to the leaderboard by name.

---

## 🛠️ Key Functions

| Function | Description |
|---|---|
| `draw_board()` | Renders the current board state |
| `initialise_board()` | Resets the board for a new game |
| `get_player_move()` | Validates and accepts player input (1–9) |
| `choose_computer_move()` | Randomly selects an available cell |
| `check_for_win()` | Checks all win conditions for a given mark |
| `check_for_draw()` | Returns `True` if no cells remain |
| `save_score()` | Saves a named score to `leaderboard.txt` |
| `load_scores()` | Reads and returns the leaderboard dictionary |
| `display_leaderboard()` | Prints scores sorted highest to lowest |

---

## 📌 Notes

- The computer uses a **random move strategy** — it picks any available cell.
- The leaderboard is stored as a JSON dictionary in `leaderboard.txt`.
- Multiple players can save their scores; the leaderboard sorts by highest score.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
