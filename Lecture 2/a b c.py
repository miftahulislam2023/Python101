x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print("The BIGGEST number is x")
elif y > x and y > z:
    print("The BIGGEST number is y")
else:
    print("The BIGGEST number is z")