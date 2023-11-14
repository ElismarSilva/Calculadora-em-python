#Calculadora com funções
#Autor: Elismar Silva
#Ciencia da Computação - UDF
#Curso: Python Udemy
#Data: 14/11/2023
#Versão: 0.1


while True:# Pede para o usuário digitar a operação
    operacao = input('Escolha uma das operações: [Soma], [Multiplicação], [Subtração], [Divisão]: ')
    print(f'Você escolheu {operacao}')

    if operacao in ['Soma', 'Multiplicação', 'Subtração', 'Divisão']:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        break
    else: # Caso a operação não seja válida, o programa pede para o usuário digitar novamente
        print('Operação inválida. Escolha uma das opções: [Soma], [Multiplicação], [Subtração], [Divisão]')


resultado = 0 # Inicializa a variável resultado

def somar(a, b): # Define a função somar
    return a + b

def multiplicar(a, b): # Define a função multiplicar
    return a * b
    
def subtrair(a, b): # Define a função subtrair
    return a - b

def dividir(a, b):  # Define a função dividir
    while True:     # Verifica se o denominador é diferente de zero
        b = float(input('Digite um valor diferente de zero: ')) 
        if b != 0: # Se o denominador for diferente de zero, a função retorna o resultado da divisão
            return a / b
        else:
            print('Não é possível dividir por zero')      
 
# Verifica qual operação foi escolhida e chama a função correspondente
if operacao == 'Soma':  
    resultado = somar(num1, num2)
elif operacao == 'Multiplicação':
    resultado = multiplicar(num1, num2)
elif operacao == 'Subtração':
    resultado = subtrair(num1, num2)
elif operacao == 'Divisão':
    resultado = dividir(num1, num2)

# Imprime o resultado com duas casas decimais
print(f'Resultado: {resultado:.2f}')
