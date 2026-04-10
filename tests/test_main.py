import pytest
from src.main import calcular_orcamento

# 1. Cenário de uso correto ("caminho feliz")
def test_calcular_orcamento_sucesso():
    assert calcular_orcamento("Site", 100, 10) == 1000

# 2. Entrada inválida (valores negativos)
def test_calcular_orcamento_negativo():
    with pytest.raises(ValueError):
        calcular_orcamento("Logo", -50, 5)

# 3. Caso limite (zero horas)
def test_calcular_orcamento_zero():
    assert calcular_orcamento("Consultoria", 50, 0) == 0