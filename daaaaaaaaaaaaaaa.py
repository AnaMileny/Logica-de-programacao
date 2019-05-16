from random import randint

dado1 =randint(1, 6)
dado2 =randint(1, 6)
dado3 =randint(1, 6)
dado4 =randint(1, 6)

jogador1 =dado1 + dado2
jogador2 =dado3 + dado4

print(jogador1)
print("primeiro dado:", dado1)
print("segundo dado:", dado2)
print("\tTotal:",jogador1)

print(jogador2)
print("terceiro dado:", dado3)
print("quarto dado:", dado4)
print("\tTotal:", jogador2)