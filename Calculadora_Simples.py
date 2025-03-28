# Calculadora simples

# Mostra as opções de operações disponíveis
print("Operações disponíveis: \nMultiplicação: * \nDivisão: / \nSoma: + \nSubtração: - \nExponenciação/potenciação: \nRaiz: ")

# Variáveis e inputs para a oscolha da operação e insersão dos números
operacao = str(input("Digite a operação desejada: "))

if operacao == "^":                                     #para fazer a raiz quadrada, só precisa de um numero
    numero_raiz = float(input("Digite um numero: "))    #então foi inserido o if para pedir apenas um número
else:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um numero: "))

# Código para as operações
if operacao == "**":
    print(f"{numero1 ** numero2:.2f}")
elif operacao == "^":                        # poderia usar sqrt(), mas ele só funciona com numeros inteiros
    print(f"{numero_raiz ** (1/2):.2f}")     # como é float ele retornaria um erro dependendo do numero
elif operacao == "*":
    print(f"{numero1 * numero2:.2f}")
elif operacao == "/":
    print(f"{numero1 / numero2:.2f}")
elif operacao == "+":
    print(f"{numero1 + numero2:.2f}")
elif operacao == "-":
    print(f"{numero1 - numero2:.2f}")
else:
    print("Operação invalida")
