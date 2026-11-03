def calcular_desconto(valor, percentagem):
    return valor - (valor * (percentagem / 100))

def somar_itens(itens):
    return sum(itens)

def finalizar_compra(itens, desconto):
    total = somar_itens(itens)
    return calcular_desconto(total, desconto)