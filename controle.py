from modelos import Produto

#Armazenamento em memória
estoque = {}
usuarios = {}

def cadastrar_produto(nome, preco, quantidade):
    """Cadastrar um novo produto no estoque"""
    codigo = nome[:3].upper() + str(int(preco * 100))  # Gera um código para o produto
    produto = Produto(nome, codigo, preco, quantidade)
    estoque[produto.codigo] = produto  # Salva o produto no estoque
    print(f"Produto {nome} cadastrado com sucesso!")

def remover_produto(codigo_produto):
    """Remover um produto do estoque"""
    if codigo_produto in estoque:
        del estoque[codigo_produto]
        print(f"Produto {codigo_produto} removido com sucesso!")
    else:
        print(f"Produto {codigo_produto} não foi encontrado.")

def atualizar_produto(codigo_produto, novo_nome=None, novo_preco=None, nova_quantidade=None):
    """Atualizar as informações de um produto no estoque"""
    if codigo_produto in estoque:
        produto = estoque[codigo_produto]
        if novo_nome:
            produto.nome = novo_nome
        if novo_preco is not None:
            produto.preco = novo_preco
        if nova_quantidade is not None:
            produto.quantidade = nova_quantidade
        produto.salvar(estoque)  # Salva o produto no estoque
        print(f"Produto {codigo_produto} atualizado com sucesso!")
    else:
        print(f"Produto {codigo_produto} não foi encontrado")

def listar_produtos():
    """Listar todos os produtos cadastrados"""
    if estoque:
        for produto in estoque.values():
            print(produto)
    else:
        print("Não há produtos cadastrados.")

def cadastrar_usuario(nome_usuario, email, senha):
    """Cadastrar um novo usuário no sistema (em memória)"""
    if nome_usuario not in usuarios and email not in [usuario['email'] for usuario in usuarios.values()]:
        usuarios[nome_usuario] = {'email': email, 'senha': senha}
        return True
    else:
        print("Erro: Nome de usuário ou email já cadastrado.")
        return False
    
def realizar_login(nome_usuario, senha):
    """Realizar o login de um usuário no sistema(em memória)"""
    usuario = usuarios.get(nome_usuario)
    if usuario and usuario['senha'] == senha:
        print (f"Login bem-sucedido! Bem-vindo, {nome_usuario}")
        return True
    else:
        print("Erro: Nome de usuário ou senha incorretos.")
        return False    