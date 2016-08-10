## The Problem

The problem is to find all unique configurations of a set of normal chess pieces on a chess board with dimensions M×N where none of the pieces is in a position to take any of the others. Assume the colour of the piece does not matter, and that there are no pawns among the pieces.

Write a program which takes as input:
- The dimensions of the board: M, N
- The number of pieces of each type (King, Queen, Bishop, Rook and Knight) to try and place on the board.

As output, the program should list all the unique configurations to the console for which all of the pieces can be placed on the board without threatening each other.

When returning your solution, please provide with your answer the total number of unique configurations for a **7×7 board with 2 Kings, 2 Queens, 2 Bishops and 1 Knight. Also provide the time it took to get the final score. Needless to say, the lower the time, the better**.

### Examples

Input: 3×3 board containing 2 Kings and 1 Rook.

| K |   | K |
|---|---|---|
|   |   |   |
|   | R |   |

| K |   |   |
|---|---|---|
|   |   | R |
| K |   |   |

|   |   | K |
|---|---|---|
| R |   |   |
|   |   | K |

|   | R |   |
|---|---|---|
|   |   |   |
| K |   | K |

Input: 4×4 board containing 2 Rooks and 4 Knights.

|   | N |   | N |
|---|---|---|---|
|   |   | R |   |
|   | N |   | N |
| R |   |   |   |

|   | N |   | N |
|---|---|---|---|
| R |   |   |   |
|   | N |   | N |
|   |   | R |   |

| R |   |   |   |
|---|---|---|---|
|   | N |   | N |
|   |   | R |   |
|   | N |   | N |

|   |   | R |   |
|---|---|---|---|
|   | N |   | N |
| R |   |   |   |
|   | N |   | N |

|   | R |   |   |
|---|---|---|---|
| N |   | N |   |
|   |   |   | R |
| N |   | N |   |

|   |   |   | R |
|---|---|---|---|
| N |   | N |   |
|   | R |   |   |
| N |   | N |   |

| N |   | N |   |
|---|---|---|---|
|   |   |   | R |
| N |   | N |   |
|   | R |   |   |

| N |   | N |   |
|---|---|---|---|
|   | R |   |   |
| N |   | N |   |
|   |   |   | R |

### Hints

Please follow best practices whilst writing your code. Tests, proper commits, proper configuration, good code structure, clean code practices are among others, good signs of your professional approach. Your code will be used as a proof of your capabilities. Below you can find some important hints (feel free to comment on them and send your remarks in case you have any)

- Code has to comply to https://www.python.org/dev/peps/pep-0008/
- Code should be covered with unit tests in at least 90%
- Pylint score should be at least 9.0/10
- docstrings should comply to pep257 for every public class and method and module function (except from tests)
