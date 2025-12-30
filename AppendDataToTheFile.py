"""
Takes user input and writes it to a file named output.txt.
Appends additional data to the same file.
Reads and displays the final content of the file.
"""
with open("output.txt", "wt") as fh:
    data= input("Enter text to write to the file:")
    #Hello, Python!
    fh.write(data)
    fh.write('\n')
    print("Data successfully written to output.txt.")
    fh.close()
#append data to file
with open("output.txt", "at") as fh:
  data1= input("Enter additional text to append:")
  #Learning file handling in Python.
  fh.write(data1)
  print("Data successfully appended.")
  fh.close()
try:
 with open("output.txt", "rt") as fh:
    content1= fh.readline()
    content2= fh.readline()
    print("Final content of output.txt")
    print(content1)
    print(content2)
    fh.close()
except FileNotFoundError as file_err:
    print("The file you are trying to open doesn't exist.")
    print(file_err)

