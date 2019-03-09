#test7
from sys import argv

program_name, file = argv

txt = open(file)
total_file = txt.read()
print(total_file)
txt.close()


word = open(file)
lines = word.readlines()
print(lines)
word.close()

theTing = open(file, "w")
theTing.truncate()

line1 = "new line 1\n"
line2 = "new line 2\n"
line3 = "THis the mufucking line 3"

theTing.write(line1)
theTing.write(line2)
theTing.write(line3)

theTing.close()

text = open(file)
words = text.read()
print("This is what the file has in it now:")
print(words)
text.close()