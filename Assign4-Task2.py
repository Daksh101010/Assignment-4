# Step 1: take input and write to file...
text = input("Enter text to write to file: ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()

# Step 2: append more data....
more_text = input("Enter text to append: ")

file = open("output.txt", "a")
file.write(more_text + "\n")
file.close()

# Step 3: read and display final content....
file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()

