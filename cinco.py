texto = input("Digite um nome: ")[::-1]
print(texto)
texto1 = "Target"

def reversed_string(texto):
    count = int(len(texto))-1
    palavra_reversa = ''
    while count >= 0:
        palavra_reversa = palavra_reversa + texto[count]
        count= count - 1
    return palavra_reversa

print(reversed_string(texto1))