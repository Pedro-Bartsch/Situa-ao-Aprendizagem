import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from modelos import Produto

# Armazenar produtos e usuários em memória
estoque = {}
usuarios = {}

class FarmaciaApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Farmácia App")
        self.root.geometry("800x400")

        # Menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # Criar os itens do menu 
        self.menu_produtos = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Produto", menu=self.menu_produtos)
        self.menu_produtos.add_command(label="Cadastrar Medicamento", command=self.cadastrar_produto)
        self.menu_produtos.add_command(label="Remover Medicamento", command=self.remover_produto)
        self.menu_produtos.add_command(label="Atualizar Medicamento", command=self.atualizar_produto)
        self.menu_produtos.add_command(label="Listar Produtos", command=self.listar_produtos)

        # Item para saída do aplicativo
        self.menu.add_command(label="Sair", command=root.quit)

        # Adicionar login ou cadastro ao iniciar
        self.login_janela()

    def login_janela(self):
        """Janela de login/cadastro"""
        self.login_janela = tk.Toplevel(self.root)
        self.login_janela.title("Login")
        self.login_janela.geometry("400x250")

        # Configuração de tamanho
        self.login_janela.grid_columnconfigure(0, weight=1)
        self.login_janela.grid_columnconfigure(1, weight=3)
        
        # Nome de usuário
        self.label_nome_usuario_login = tk.Label(self.login_janela, text="Nome de Usuário")
        self.label_nome_usuario_login.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_usuario_login = tk.Entry(self.login_janela)
        self.entry_nome_usuario_login.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Senha
        self.label_senha_login = tk.Label(self.login_janela, text="Senha")
        self.label_senha_login.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha_login = tk.Entry(self.login_janela, show="*")
        self.entry_senha_login.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Botão Login
        self.botao_login = tk.Button(self.login_janela, text="Login", width=20, height=2, command=self.login)
        self.botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.login_janela, text="Cadastrar", width=20, height=2, command=self.cadastrar)
        self.botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        nome_usuario = self.entry_nome_usuario_login.get()  # Corrigido para nome de usuário
        senha = self.entry_senha_login.get()

        # Verificar se o usuário existe e a senha está correta
        if self.realizar_login(nome_usuario, senha):
            self.login_janela.destroy()
            messagebox.showinfo("Concluído", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nome de usuário/senha inválidos. Tente novamente.")

    def cadastrar(self):
        self.cadastro_janela = tk.Toplevel(self.root)
        self.cadastro_janela.title("Cadastro de Usuário")
        self.cadastro_janela.geometry("400x250")

        # Configuração de tamanho
        self.cadastro_janela.grid_columnconfigure(0, weight=1)
        self.cadastro_janela.grid_columnconfigure(1, weight=3)

        # Nome de usuário
        self.label_nome = tk.Label(self.cadastro_janela, text="Nome de Usuário")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.cadastro_janela)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Email
        self.label_email = tk.Label(self.cadastro_janela, text="Email")
        self.label_email.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(self.cadastro_janela)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Senha
        self.label_senha = tk.Label(self.cadastro_janela, text="Senha")
        self.label_senha.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha = tk.Entry(self.cadastro_janela, show="*")
        self.entry_senha.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.cadastro_janela, text="Cadastrar", width=20, height=2, command=self.finalizar_cadastro)
        self.botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def finalizar_cadastro(self):
        nome_usuario = self.entry_nome.get()  # Nome de usuário
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if self.cadastrar_usuario(nome_usuario, email, senha):
            messagebox.showinfo("Concluído", "Cadastro realizado com sucesso!")
            self.cadastro_janela.destroy()  # Fechar a tela de cadastro
            self.login_janela.deiconify()  # Mostrar a tela de login novamente
        else:
            messagebox.showerror("Erro", "Nome de usuário ou email já cadastrado.")

    def cadastrar_produto(self):
       
        """Tela para cadastrar um novo produto"""
        self.cadastro_produto_janela = tk.Toplevel(self.root)
        self.cadastro_produto_janela.title("Cadastro de Produto")
        self.cadastro_produto_janela.geometry("400x250")

        # Configuração de tamanho
        self.cadastro_produto_janela.grid_columnconfigure(0, weight=1)
        self.cadastro_produto_janela.grid_columnconfigure(1, weight=3)

        # Nome do Produto
        self.label_nome_produto = tk.Label(self.cadastro_produto_janela, text="Nome do Produto")
        self.label_nome_produto.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_nome_produto.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Preço do Produto
        self.label_preco_produto = tk.Label(self.cadastro_produto_janela, text="Preço do Produto")
        self.label_preco_produto.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_preco_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_preco_produto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Quantidade do Produto
        self.label_quantidade_produto = tk.Label(self.cadastro_produto_janela, text="Quantidade do Produto")
        self.label_quantidade_produto.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_quantidade_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_quantidade_produto.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

            # Botão Cadastrar Produto
        self.botao_cadastrar_produto = tk.Button(self.cadastro_produto_janela, text="Cadastrar Produto", width=20, height=2, command=self.finalizar_cadastro_produto)
        self.botao_cadastrar_produto.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def finalizar_cadastro_produto(self):
        """Função para finalizar o cadastro do produto"""
        nome_produto = self.entry_nome_produto.get()
        preco_produto = self.entry_preco_produto.get()
        quantidade_produto = self.entry_quantidade_produto.get()

        # Validação se os campos foram preenchidos
        if not nome_produto or not preco_produto or not quantidade_produto:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            preco_produto = float(preco_produto)
            quantidade_produto = int(quantidade_produto)

            # Verifica se os valores são válidos
            if preco_produto <= 0 or quantidade_produto <= 0:
                messagebox.showerror("Erro", "Preço e quantidade devem ser maiores que zero!")
                return

            # Gerando o código do produto
            codigo_produto = nome_produto[:3].upper() + str(int(preco_produto * 100))
            produto = Produto(nome_produto, codigo_produto, preco_produto, quantidade_produto)
            estoque[produto.codigo] = produto  # Salva no estoque
            messagebox.showinfo("Concluído", "Produto cadastrado com sucesso!")
        
            # Fechar a janela após cadastro
            self.cadastro_produto_janela.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para preço e quantidade.")

    def remover_produto(self):
        codigo = self.ask_input("Código do medicamento para remover: ")
        if codigo in estoque:
            del estoque[codigo]
            messagebox.showinfo("Concluído", f"Medicamento {codigo} removido com sucesso!")

    def atualizar_produto(self):
        codigo = self.ask_input("Código do medicamento para atualizar:")
        if codigo in estoque:
            novo_nome = self.ask_input("Novo nome do medicamento")
            novo_preco = self.ask_input("Novo preço do medicamento: ", is_number=True)
            nova_quantidade = self.ask_input("Nova quantidade do medicamento: ", is_number=True)

            produto = estoque[codigo]
            produto.nome = novo_nome if novo_nome else produto.nome
            produto.preco = novo_preco if novo_preco else produto.preco
            produto.quantidade = nova_quantidade if nova_quantidade else produto.quantidade

            messagebox.showinfo("Concluído", f"Medicamento {codigo} atualizado com sucesso!")

    def listar_produtos(self):
        if estoque:
            produto_list = "\n".join([str(produto) for produto in estoque.values()])
            messagebox.showinfo("Lista de Produtos", produto_list)
        else:
            messagebox.showinfo("Lista de Produtos", "Não há produtos cadastrados.")

    def ask_input(self, pergunta, is_number=False):
        resposta = simpledialog.askstring("Entrada", pergunta)
        if is_number:
            try:
                return float(resposta) if resposta else None
            except ValueError:
                messagebox.showerror("Erro", "Por favor insira um número válido!")
                return None
        return resposta

    def realizar_login(self, nome_usuario, senha):
        """Verifica as credenciais de login no dicionário de usuários"""
        usuario = usuarios.get(nome_usuario)
        if usuario and usuario['senha'] == senha:
            return True
        return False

    def cadastrar_usuario(self, nome_usuario, email, senha):
        """Cadastrar um novo usuário no sistema"""
        if nome_usuario not in usuarios and email not in [usuario['email'] for usuario in usuarios.values()]:
            usuarios[nome_usuario] = {'email': email, 'senha': senha}
            return True
        return False

def main():
    root = tk.Tk()
    app = FarmaciaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()