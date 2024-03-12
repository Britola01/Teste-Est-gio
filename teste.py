# Questão 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("Questao 1 =", SOMA)

#Questão 2

def pertence_fibonacci(numero):

    a, b = 0, 1
    fib_sequence = [a, b]

    while b < numero:
        a, b = b, a + b
        fib_sequence.append(b)

    if numero in fib_sequence:
        return f"Questao 2 = O numero {numero} pertence a sequencia de Fibonacci."
    else:
        return f"Questao 2 = O numero {numero} NAO pertence a sequencia de Fibonacci."

print(pertence_fibonacci(34))

#Questão 3

#a = 9
#b = 128
#c = 49
#d = 100
#e = 13

#Questão 4 
#A complexidade da pergunta em si, seria O(1), já que eu teria que verificar cada interruptor, um por um,\
#até saber qual é o correto de cada lâmpada.

#Questão 5

def inverter_string(string_original):
    string_invertida = ""  # Inicializa a string invertida vazia
    for i in range(len(string_original) - 1, -1, -1):
        string_invertida += string_original[i]
    return string_invertida
print(("Questao 5 ="), inverter_string("exemplo"))



