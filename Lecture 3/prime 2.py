x = 2
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
        print(x)
    
    x += 1