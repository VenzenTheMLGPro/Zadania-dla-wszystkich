from random import randint
a = int(input("Podaj całkowitą liczbę nieujemną: "))
i = 0
print(a * " ", "X")
while i < a - 1:
    i += 1
    print((a - i) * " ", "*" * (i * 2 + 1))
print(a * " ", "U")



