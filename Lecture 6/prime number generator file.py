file = open("prime numbers.txt", "w")
#prime number part
x = 2
count = 1
while x <= 100:
    i = 2
    prime  = True
    while i < x:
        if x % i == 0:
            prime = False
            break
        i += 1
        #i = i + 1

    if prime:
        line = "Prime-" + str(count) + ": " + str(x) + "\n"
        count += 1
        file.write(line)
    x += 1

file.close()