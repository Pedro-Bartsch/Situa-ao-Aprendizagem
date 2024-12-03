class Produto:
    def __init__(self, nome, codigo, preco, quantidade, tipo):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo  # Novo campo para tipo de medicamento

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - R${self.preco} - Quantidade: {self.quantidade} - Tipo: {self.tipo}"
    
    def atualizar_estoque(self,quantidade_vendida):
        """Função para atualizar a quantidade de produto após uma venda"""
        if self.quantidade >= quantidade_vendida:
            self.quantidade -= quantidade_vendida
            return True
        return False
    
    def salvar(self, estoque):
        """Salva ou atualiza o produto no estoque"""
        estoque[self.codigo] = self
    
