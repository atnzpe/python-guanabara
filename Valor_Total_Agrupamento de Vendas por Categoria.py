class Venda:
    """
    Representa uma venda individual com produto, quantidade e valor.
    """
    def __init__(self, produto, quantidade, valor):
        """
        Inicializa uma nova venda.

        Args:
            produto (str): Nome do produto vendido.
            quantidade (int): Quantidade do produto vendido.
            valor (float): Valor unitário do produto.
        """
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    """
    Representa uma categoria de vendas, contendo um nome e uma lista de vendas.
    """
    def __init__(self, nome):
        """
        Inicializa uma nova categoria.

        Args:
            nome (str): Nome da categoria.
        """
        self.nome = nome
        self.vendas = []  # Lista para armazenar as vendas da categoria

    def adicionar_venda(self, venda):
        """
        Adiciona uma venda à lista de vendas da categoria.

        Args:
            venda (Venda): Objeto Venda a ser adicionado.
        """
        self.vendas.append(venda)

    def total_vendas(self):
        """
        Calcula o total de vendas da categoria.

        Returns:
            float: Valor total das vendas na categoria.
        """
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor
        return total

def main():
    """
    Função principal para ler os dados de vendas, organizá-los por categoria
    e exibir o total de vendas por categoria.
    """
    categorias = []

    # Loop para ler os dados de 2 categorias
    for i in range(2):  
        nome_categoria = input("Digite o nome da categoria: ")
        categoria = Categoria(nome_categoria)  # Cria um objeto Categoria

        # Loop para ler os dados de 2 vendas por categoria
        for j in range(2):  
            entrada_venda = input("Digite os dados da venda (produto,quantidade,valor): ")
            produto, quantidade, valor = entrada_venda.split(',')  # Divide a entrada
            quantidade = int(quantidade.strip())  # Converte a quantidade para inteiro
            valor = float(valor.strip())  # Converte o valor para float

            venda = Venda(produto.strip(), quantidade, valor)  # Cria um objeto Venda
            categoria.adicionar_venda(venda)  # Adiciona a venda à categoria

        categorias.append(categoria)  # Adiciona a categoria à lista de categorias

    # Exibe o total de vendas para cada categoria
    for categoria in categorias:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas():.1f}")

if __name__ == "__main__":
    main()
