import random

abc = "abcd"
ABC = "ABCD"
nunmbers = "1234"
spec = "[]:;"

symb = abc+ ABC+nunmbers+spec

lenght = 8

for i in range(10):
    password = "".join(random.sample(symb,lenght))
    print(password)