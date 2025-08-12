def dias_já_vividos(idade):
    """Calcular quantos dias a pessoa já viveu, sem considerar anos bissextos.

    Args:
    idade: a idade em anos (inteiro).

    Returns: a quantidade de dias já vividos (inteiro)."""

    dias_por_ano = 365

    # saber a idade
    idade_da_pessoa = int(input("Qual a sua idade?"))

    #calcular os dias
    dias = dias_já_vividos (idade_da_pessoa)

    # mostrar o resultado
    print (f"Você já viveu aproximadamente {dias} dias.")

