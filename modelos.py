class Produto:
    def __init__(self,nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.nome} - Preço: R${self.preco} - Estoque: {self.quantidade}'
    
    def atualizar_estoque(self,quantidade_vendida):
        """Função para atualizar a quantidade de produto após uma venda"""
        if self.quantidade >= quantidade_vendida:
            self.quantidade -= quantidade_vendida
            return True
        return False
    
    def salvar(self, estoque):
        """Salva ou atualiza o produto no estoque"""
        estoque[self.codigo] = self

    