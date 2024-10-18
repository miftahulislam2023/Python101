x = int(input("Please enter a number:"))
i = 2
prime  = True
while i < x:
    if x % i == 0: #modulus operator
        prime = False
        break
    i += 1
    #i = i + 1

if prime:
    print("Prime")
else:
    print("Not prime")

#break এর কাজ হলো লুপ থেকে বের হওয়া