def area_retangulo (retangulo):
    """Calcular e mostrar a área do retângulo.

    Args:
    retangulo: largura e altura (inteiro).

    Returns: area do retangulo (inteiro)."""
    area_retangulo = ("altura * largura")

    # saber a largura e altura
    largura_do_retangulo = int(input("Qual a largura do retângulo?"))
    altura_do_retangulo = int(input("Qual a altura do retângulo?"))

    #calcular a area
    area_retangulo = (largura_do_retangulo*altura_do_retangulo);

    # mostrar o resultado
    print (f"A área do retângulo é {area_retangulo}.")

