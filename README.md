# Assignment-4
Task1 and Task2

Asign4-Task1.py- gives the code for a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
4.   TASK1(OUTPUT)- is the result for the following program

Asign4-Task2.py- contains the Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
4.   TASK(OUTPUT)- is the output of the program

Program 1: Read sample.txt and handle error
What the program does (working)
Tries to open sample.txt in read mode.
Reads the file line by line using a loop.
Prints each line on the screen.
If the file does not exist, Python raises FileNotFoundError.
try-except catches the error and prints a message instead of crashing.
Key point
This program only reads a file.
It will NOT create sample.txt. The file must already exist.

Program 2: Write, append, then read output.txt
What the program does (working)
Takes user input and opens output.txt in write mode ("w").
If the file exists → old data is erased.
If it doesn’t exist → Python creates it.
Takes more input and opens the same file in append mode ("a").
New data is added at the end without deleting old data.
Opens the file in read mode ("r").
Reads and displays the final combined content.
Key point
This program creates, modifies, and reads the file in one run.


