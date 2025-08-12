def calculadora():
    """Calcula as quatro operações básicas com dois números"""

    try:
        num1 = float (input("digite o primeiro número"))
        num2 = float (input("digite o segundo número"))

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2

        print (f"Soma: {soma}")
        print (f"Subtracao: {subtracao}")
        print (f"Multiplicacao: {multiplicacao}")
        print (f"Divisao: {divisao}")

    except ValueError:
        print ("Inválido, tente novamente")

        calculadora ()
