import tkinter as tk
from tkinter import messagebox, simpledialog
from modelos import Produto

#Armazenar produtos e usuários em memória
estoque = {}
usuarios = {}

class FarmaciaApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Farmácia App")
        self.root.geometry("800x400")

        #Menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        #Criar os itens do menu 
        self.menu_produtos = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Produto", menu=self.menu_produtos)
        self.menu_produtos.add_command(label="Cadastrar Medicamento", command=self.cadastrar_produto)
        self.menu_produtos.add_command(label="Remover Medicamento", command=self.remover_produto)
        self.menu_produtos.add_command(label="Atualizar Medicamento", command=self.atualizar_produto)
        self.menu_produtos.add_command(label="Listar Produtos", command=self.listar_produtos)

        #Item para saída do aplicativo
        self.menu.add_command(label="Sair", command=root.quit)

        #Adicionar login ou cadastro ao iniciar
        self.login_janela()

    def login_janela(self):
        """Janela de login/cadastro"""
        self.login_janela = tk.Toplevel(self.root)
        self.login_janela.title("Login")
        self.login_janela.geometry("400x200")

        #Configuração de tamanho
        self.login_janela.grid_columnconfigure(0, weight = 1)
        self.login_janela.grid_columnconfigure(1, weight = 3)
        
        #Email
        self.label_email = tk.Label(self.login_janela, text="Email")
        self.label_email.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(self.login_janela)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        #Senha
        self.label_senha = tk.Label(self.login_janela, text="Senha")
        self.label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha = tk.Entry(self.login_janela, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady= 5, sticky="ew")
        

        #Botão Login
        self.botao_login = tk.Button(self.login_janela, text="Login", width = 20, height = 2,command=self.login)
        self.botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        #Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.login_janela, text="Cadastrar", width = 20, height = 2, command=self.cadastrar)
        self.botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        nome_usuario = self.entry_email.get()
        senha = self.entry_senha.get()

        if self.realizar_login(nome_usuario, senha):
            self.login_janela.destroy()
            messagebox.showinfo("Concluído", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nome de usuário/senha inválidos. Tente novamente.")

    def cadastrar(self):
        nome_usuario = self.ask_input("Nome de Usuário")
        email = self.ask_input("Email")
        senha = self.ask_input("Senha")

        if self.cadastrar_usuario(nome_usuario, email, senha):
            self.login_janela.destroy()
            messagebox.showinfo("Concluído", "Cadastro realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nome de usuário ou email já cadastrado.")

    def cadastrar_produto(self):
        nome = self.ask_input("Nome do Medicamento: ")
        preco = self.ask_input("Preço do Medicamento: ", is_number=True)
        quantidade = self.ask_input("Quantidade Disponível: ", is_number=True)

        if nome and preco is not None and quantidade is not None:
            try:
                #Gerando o código do medicamento
                codigo = nome[:3].upper() + str(int(preco * 100))
                produto = Produto(nome, codigo, preco, quantidade)
                estoque[produto.codigo] = produto  # Salva no estoque
                messagebox.showinfo("Concluído", "Medicamento cadastrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

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
        return nome_usuario in usuarios and usuarios[nome_usuario] == senha

    def cadastrar_usuario(self, nome_usuario, email, senha):
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