file = open("poem.txt", "r")
lines = file.readlines()
file.close()

lineNumber = 1
for line in lines:
    print("Line-", lineNumber, ":", line,
          sep= "",
          )
    lineNumber +=  1