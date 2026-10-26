lab_01: reading data from keyboard

# lab01_yourname

## Description
This is a small Python program made for Lab 2. It does three things:

1. Reads a sequence of numbers from the keyboard and displays it.
2. Reads an array of numbers, where the user chooses the number of rows and columns, and displays it.
3. Reads a string of numbers from a text file, where the user types the file name, and displays it. If the file does not exist, an error message is shown.

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with:

       python main.py

5. Follow the instructions on the screen:
   - Type the numbers separated by spaces (for example: `3 5 8 10`).
   - Type the number of rows and columns, then each element of the array.
   - For the file part, type `numbers.txt` (the example file included in the project).
     If you type a name that does not exist, the program shows an error message.

## Branches
- `feature/console-input` - reading data from the keyboard (Requirement 1)
- `feature/array-file-input` - reading data from a file (Requirement 2)