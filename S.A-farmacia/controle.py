from database import conectar
from modelos import Produto
from modelos import Venda

class Farmacia:
    def __init__(self):
        self.estoque = {}

    def cadastrar_produto(self, codigo, nome, quantidade, preco):
        if codigo not in self.estoque:
            produto = Produto(codigo, nome, quantidade, preco)
            self.estoque [codigo] = produto
        else:
            print ("Produto já cadastrado!")
        
    def exibir_estoque(self):
            for produto in self.estoque.values():
                print (produto)

    def realizar_venda(self, produtos_e_quantidades):
        produtos_vendidos = []
        for codigo_produto, quantidade in produtos_e_quantidades:
            produto = self.estoque.get(codigo_produto)
            if produto:
                if produto.quantidade >= quantidade:
                    produto.atualizar_estoque(quantidade)
                    produtos_vendidos.append(Produto(produto.codigo, produto.nome, quantidade, produto.preco))
                else:
                    print(f"Estoque insuficiente para {produto.nome}.")
            else:
                print(f"Produto com código {codigo_produto} não encontrado.")
        
        if produtos_vendidos:
            print(Venda(produtos_vendidos))
        else:
            print("Nenhum produto foi vendido.")
            
    def relatorio_estoque(self):
        print ("\nRelatório de Estoque: ")
        self.exibir_estoque()

medicamentos = []

def adicionar_medicamento():
    conn = conectar()
    cursor = conn.cursor()
    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))
    quantidade = int(input("Digite a quantidade disponível: "))
    conn.commit()
    conn.close()
    medicamento = {"nome": nome, "preco": preco, "quantidade": quantidade}
    medicamentos.append (medicamento)

def remover_medicamento():
    nome = input("Digite o nome do medicamento que deseja remover: ") 

    #Encontra o medicamento na lista
    for med in Produto:
        if med["nome"] == nome:
            medicamentos.remove(med)
            print (f'Medicamento {nome} removido com sucesso!')
            return
    print (f'Medicamento {nome} não encontrado.')
    
def atualizar_medicamento():
    pass

def mostrar_medicamento():
    if not medicamentos:
        print ("Não há medicamentos cadastrados")
    else:
        print ("Medicamentos na farmácia: ")
        for med in medicamentos:
            print (f'{med['nome']} - R${med['preco']} - Estoque: {med['quantidade']}')
