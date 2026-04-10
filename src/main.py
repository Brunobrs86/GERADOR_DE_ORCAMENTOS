def calcular_orcamento(projeto, valor_hora, horas_estimadas):
    """Calcula o valor total do orçamento."""
    if valor_hora < 0 or horas_estimadas < 0:
        raise ValueError("Valores não podem ser negativos")
    return valor_hora * horas_estimadas

def main():
    print("=== Gerador de Orçamentos para Autônomos ===")
    try:
        projeto = input("Descrição do projeto: ")
        v_hora = float(input("Valor da sua hora (R$): "))
        h_estimadas = float(input("Total de horas estimadas: "))

        total = calcular_orcamento(projeto, v_hora, h_estimadas)

        print("\n--- RESUMO DO ORÇAMENTO ---")
        print(f"Projeto: {projeto}")
        print(f"Valor Total Estimado: R$ {total:.2f}")
        print("---------------------------")
        
    except ValueError as e:
        print(f"Erro: Entrada inválida. {e}")

if __name__ == "__main__":
    main()