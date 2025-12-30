"""
Opens and reads a text file named sample.txt.
Prints its content line by line.
Handles errors gracefully if the file does not exist.

fh= open("sample.txt","xt")
fh.write("This is a sample text file.\n")
fh.write("It contains multiple lines.")
fh.close()
"""
#read file line by line
try:
 with open("sample.txt","rt") as fh:
    line1= fh.readline()
    line2= fh.readline()
 print(line1)
 print(line2)
 fh.close()
except FileNotFoundError as file_err:
    print("The file sample.txt was not found.")
