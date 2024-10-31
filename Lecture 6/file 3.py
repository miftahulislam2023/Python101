file = open("poem.txt", "r")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
file.close()

print(line1)
print(line2)
print(line3)

"""
read() - reads the entire file
readline() - reads a single line
"""