class Produto:
    def __init__(self, nome, codigo ,preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.nome} - Preço: R${self.preco} - Estoque: {self.quantidade}'
    

    def atualizar_estoque(self,quantidade_vendida):
        """Atualiza a quantidade de produto após uma venda"""
        if self.quantidade >= quantidade_vendida:
            self.quantidade -= quantidade_vendida
        else: 
            raise ValueError (f'Estoque insuficiente para {self.nome}. Disponível: {self.quantidade}')

    def salvar(self, cursor):
        """Salva ou atualiza o produto no banco de dados"""
        cursor.execute(""" 
        INSERT OR REPLACE INTO produtos (id, nome, codigo, preco, quantidade) VALUES (?, ?, ?, ?, ?)
""", (self.id, self.nome, self.preco, self.quantidade))

class Venda:
    def __init__(self, produtos_vendidos):
        self.produtos_vendidos = produtos_vendidos
        self.total = sum([produto.preco * produto.quantidade for produto in produtos_vendidos])

    def __str__(self):
        detalhes = "\n".join([f'{produto.nome} - Quantidade: {produto.quantidade} - R${produto.preco * produto.quantidade: .2f}' for produto in self.produtos_vendidos])
        return f"Venda: \n{detalhes}\nTotal: R${self.total: .2f}"
    
    
    def salvar(self, cursor):
        """Salva ou atualiza o produto no banco de dados"""
        cursor.execute(""" 
        INSERT OR REPLACE INTO produtos (venda_id, produto_id, quantidade, preco) VALUES (?, ?, ?, ?)
""", (venda_id, produto.id, produto.quantidade, produto.preco))
        
