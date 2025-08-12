def area_retangulo (retangulo):
    """Calcular o troco.

    Args:
    compra: valor da compra (inteiro).

    Returns: valor do troco (inteiro)."""
    valor_troco = ("valor recebido - valor da compra")

    # saber o valor da compra e o valor recebido
    valor_da_compra = int(input("Qual o valor da compra?"))
    valor_recebido = int(input("Qual o valor recebido?"))

    #calcular o troco
    valor_troco = (valor_recebido - valor_da_compra);

    # mostrar o resultado
    print (f"O valor do seu troco é {valor_troco}.")

