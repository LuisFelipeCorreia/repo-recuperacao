from app import calcular_desconto, somar_itens, finalizar_compra

# 3 Testes Unitários
def test_calcular_desconto():
    assert calcular_desconto(100, 20) == 80

def test_somar_itens():
    assert somar_itens([10, 20, 30]) == 60

def test_somar_itens_vazio():
    assert somar_itens([]) == 0

# 1 Teste de Integração (testa o fluxo completo combinando funções)
def test_finalizar_compra_integracao():
    itens_carrinho = [50, 50, 100]
    total_com_desconto = finalizar_compra(itens_carrinho, 10)
    assert total_com_desconto == 180