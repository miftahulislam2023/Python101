""" print(2**2)
print(2**3)
print(2**4)
print(2**5) """

squares = [x**2 for x in range(1, 11)]
#squares = list(range(1,11))
#even = [2*x for x in range(1, 21)]
even = list(range(0, 41, 2))


print(squares)
print(even)
