def adicao(num1, num2):
    """Retorna a soma de dois números."""
    return num1 + num2

def subtracao(num1, num2):
    """Retorna a subtração de dois números."""
    return num1 - num2

def multiplicacao(num1, num2):
    """Retorna a multiplicação de dois números."""
    return num1 * num2

def divisao(num1, num2):
    """Verifica a divisão por zero e retorna o resultado ou uma mensagem de erro."""
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return num1 / num2

def calculadora(num1, num2, operacao):
    """
    Realiza a operação matemática desejada entre dois números.

    Args:
        num1: O primeiro número.
        num2: O segundo número.
        operacao: A operação a ser realizada ('+', '-', '*', '/', 'adicao', 'subtracao', etc.).

    Returns:
        O resultado da operação ou uma mensagem de erro.
    """
    if operacao in ['+', 'adicao']:
        return adicao(num1, num2)
    elif operacao in ['-', 'subtracao']:
        return subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao']:
        return multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao']:
        return divisao(num1, num2)
    else:
        return "Operação inválida."

saida = ''
while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao_matematica = input("Digite a operação matemática (+, -, *, /): ")

        resultado = calculadora(num1, num2, operacao_matematica)

        print(f"Resultado da operação: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
    
    saida = input("Deseja continuar? (S/N): ")