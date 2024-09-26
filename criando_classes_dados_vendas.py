

'''
Como usar o código:

Entrada de Dados:

Execute o código.
Digite os dados de cada venda no formato: Produto Quantidade Valor (separados por espaço).
Pressione Enter após cada venda.
Para finalizar a entrada de dados, pressione Enter sem digitar nada.
Saída:

O programa calculará e exibirá o total de vendas no formato: Total de Vendas: [valor total] com uma casa decimal.
Exemplo de Uso:

CopiarNotebook 3 1500.00
Mouse 10 50.00
Teclado 5 100.00
<Pressione Enter>
Total de Vendas: 5500.0

Descrição
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI.
Você tem a estrutura de duas classes, Venda e Relatorio, já definidas.
Sua tarefa é implementar partes específicas do código dentro dessas classes.


'''


class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor


class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("Erro: Objeto inválido. Adicione apenas objetos do tipo 'Venda'.")

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()

    while True:
        entrada = input().strip()
        if entrada == "":  # Pressione Enter para finalizar a entrada de dados
            break

        produto, quantidade, valor = entrada.split()
        venda = Venda(produto, int(quantidade), float(valor))
        relatorio.adicionar_venda(venda)

    print(f"Total de Vendas: {relatorio.calcular_total_vendas():.1f}")


if __name__ == "__main__":
    main()
