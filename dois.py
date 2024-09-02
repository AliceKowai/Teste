# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


t1 = 0
t2 = 1
count = 3
numero = int(input("Digite um número: "))

fibonacci_presente = False 

if numero == 0 or numero == 1:
    fibonacci_presente = True
else:
    while True:
        t3 = t1 + t2
        if numero == t3:
            fibonacci_presente = True
            break
        elif t3 > numero:
            break
        t1 = t2
        t2 = t3
        count += 1

if fibonacci_presente:
    print(f'O número {numero} está contido na sequência de Fibonacci.')
else:
    print(f'O número {numero} não está contido na sequência de Fibonacci.')
