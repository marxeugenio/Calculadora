class CalculadoraComplexa:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

calc = CalculadoraComplexa()

while True:
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        break

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = calc.somar(numero1, numero2)
        print("Resultado:", resultado)
    elif opcao == 2:
        resultado = calc.subtrair(numero1, numero2)
        print("Resultado:", resultado)
    elif opcao == 3:
        resultado = calc.multiplicar(numero1, numero2)
        print("Resultado:", resultado)
    elif opcao == 4:
        resultado = calc.dividir(numero1, numero2)
        print("Resultado:", resultado)
    else:
        print("Opção inválida. Por favor, tente novamente.")
