file = open("poem.txt", "r")
lines = file.readlines()
file.close()

print(lines[3])
"""
readlines() - reads all lines and makes a list of strings
"""