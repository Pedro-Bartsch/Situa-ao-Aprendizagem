import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
from modelos import Produto

# Armazenar produtos e usuários em memória
estoque = {}
usuarios = {}  # Dicionário para armazenar dados dos usuários

class FarmaciaApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Farmácia App")
        self.root.geometry("800x600")  # Tamanho maior para acomodar os botões

        # Inicializa a tela de login
        self.login_janela()

    def login_janela(self):
        """Janela de login/cadastro"""
        self.clear_window()  # Limpa a janela antes de mostrar os componentes de login
        
        # Configuração de layout da tela de login
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        
        # Nome de usuário
        self.label_usuario = tk.Label(self.root, text="Nome de Usuário", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_usuario = tk.Entry(self.root, font=("Helética", 12))
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Senha
        self.label_senha = tk.Label(self.root, text="Senha", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha = tk.Entry(self.root, font=("Helvética", 12), show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Botão Login
        self.botao_login = tk.Button(self.root, text="Login", width=20, height=2, command=self.login, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.root, text="Cadastrar", width=20, height=2, command=self.cadastrar, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def login(self):
        nome_usuario = self.entry_usuario.get().strip()  # Remove espaços extras
        senha = self.entry_senha.get().strip()  # Remove espaços extras

        print(f"Tentando login com Nome de Usuário: '{nome_usuario}' e Senha: '{senha}'")  # Depuração

        if self.realizar_login(nome_usuario, senha):
            self.show_funcionalidades()  # Exibe a tela de funcionalidades após o login
            messagebox.showinfo("Concluído", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nome de usuário/senha inválidos. Tente novamente.")

    def realizar_login(self, nome_usuario, senha):
        """Verifica se o nome de usuário e senha correspondem aos dados cadastrados"""
        if nome_usuario in usuarios:
            print(f"Usuário encontrado no cadastro: {usuarios[nome_usuario]}")  # Depuração
            if usuarios[nome_usuario]["senha"] == senha:
                return True
        print("Usuário ou senha inválidos.")  # Depuração
        return False

    def cadastrar(self):
        self.cadastro_janela = tk.Toplevel(self.root)
        self.cadastro_janela.title("Cadastro de Usuário")
        self.cadastro_janela.geometry("400x250")

        # Configuração de tamanho
        self.cadastro_janela.grid_columnconfigure(0, weight=1)
        self.cadastro_janela.grid_columnconfigure(1, weight=3)

        # Nome de usuário
        self.label_nome = tk.Label(self.cadastro_janela, text="Nome de Usuário", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.cadastro_janela, font=("Helvética", 12))
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Email
        self.label_email = tk.Label(self.cadastro_janela, text="Email", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_email.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(self.cadastro_janela, font=("Helvética", 12))
        self.entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
       
        # Senha
        self.label_senha = tk.Label(self.cadastro_janela, text="Senha", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_senha.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha = tk.Entry(self.cadastro_janela, font=("Helvética", 12), show="*")
        self.entry_senha.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.cadastro_janela, text="Cadastrar", width=20, height=2, command=self.finalizar_cadastro, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def finalizar_cadastro(self):
        nome_usuario = self.entry_nome.get().strip()  # Remove espaços extras
        email = self.entry_email.get().strip()  # Remove espaços extras
        senha = self.entry_senha.get().strip()  # Remove espaços extras

        # Verificando se o nome de usuário já existe
        if nome_usuario in usuarios:
            messagebox.showerror("Erro", "Nome de usuário já cadastrado.")
        else:
            # Salvar o nome de usuário como chave e email e senha como valores no dicionário
            usuarios[nome_usuario] = {"email": email, "senha": senha}
            print(f"Usuário cadastrado: {usuarios[nome_usuario]}")  # Depuração
            messagebox.showinfo("Concluído", "Cadastro realizado com sucesso!")
            self.cadastro_janela.destroy()  # Fechar a tela de cadastro
            self.login_janela()  # Mostrar a tela de login novamente

    def show_funcionalidades(self):
        """Exibe as funcionalidades após o login/cadastro"""
        self.clear_window()  # Limpa a janela de login
        
        # Botões para as funcionalidades
        self.botao_cadastrar_produto = tk.Button(self.root, text="Cadastrar Medicamento", width=20, height=4, command=self.cadastrar_produto, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_cadastrar_produto.grid(row=0, column=0, padx=20, pady=20)

        self.botao_remover_produto = tk.Button(self.root, text="Remover Medicamento", width=20, height=4, command=self.remover_produto, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_remover_produto.grid(row=0, column=1, padx=20, pady=20)

        self.botao_atualizar_produto = tk.Button(self.root, text="Atualizar Medicamento", width=20, height=4, command=self.atualizar_produto, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_atualizar_produto.grid(row=1, column=0, padx=20, pady=20)

        self.botao_listar_produtos = tk.Button(self.root, text="Listar Produtos", width=20, height=4, command=self.listar_produtos, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_listar_produtos.grid(row=1, column=1, padx=20, pady=20)

    def cadastrar_produto(self):
        """Tela para cadastrar um novo produto"""
        self.cadastro_produto_janela = tk.Toplevel(self.root)
        self.cadastro_produto_janela.title("Cadastro de Produto")
        self.cadastro_produto_janela.geometry("400x300")

        # Configuração de tamanho
        self.cadastro_produto_janela.grid_columnconfigure(0, weight=1)
        self.cadastro_produto_janela.grid_columnconfigure(1, weight=3)

        # Nome do Produto
        self.label_nome_produto = tk.Label(self.cadastro_produto_janela, text="Nome do Produto", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_nome_produto.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_nome_produto.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Preço do Produto
        self.label_preco_produto = tk.Label(self.cadastro_produto_janela, text="Preço do Produto", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_preco_produto.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_preco_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_preco_produto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Quantidade do Produto
        self.label_quantidade_produto = tk.Label(self.cadastro_produto_janela, text="Quantidade do Produto", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_quantidade_produto.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_quantidade_produto = tk.Entry(self.cadastro_produto_janela)
        self.entry_quantidade_produto.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Tipo do Medicamento
        self.label_tipo_produto = tk.Label(self.cadastro_produto_janela, text="Tipo do Medicamento", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=5)
        self.label_tipo_produto.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        
        # Opções para o tipo de medicamento
        tipos_produto = ["Antibiótico", "Analgésico", "Anti-inflamatório", "Vitaminas"]
        self.tipo_produto_var = tk.StringVar()
        self.tipo_produto_var.set(tipos_produto[0])  # Define o tipo padrão
        
        self.menu_tipo_produto = tk.OptionMenu(self.cadastro_produto_janela, self.tipo_produto_var, *tipos_produto)
        self.menu_tipo_produto.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Botão Cadastrar Produto
        self.botao_cadastrar_produto = tk.Button(self.cadastro_produto_janela, text="Cadastrar Produto", width=20, height=2, command=self.finalizar_cadastro_produto, font=("Helvetica", 12, "bold"), bg="#008CBA", padx=10, pady=5)
        self.botao_cadastrar_produto.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def finalizar_cadastro_produto(self):
        """Função para finalizar o cadastro do produto"""
        nome_produto = self.entry_nome_produto.get()
        preco_produto = self.entry_preco_produto.get()
        quantidade_produto = self.entry_quantidade_produto.get()
        tipo_produto = self.tipo_produto_var.get()  # Pega o tipo selecionado

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
            produto = Produto(nome_produto, codigo_produto, preco_produto, quantidade_produto, tipo_produto)
            estoque[produto.codigo] = produto  # Salva no estoque
            messagebox.showinfo("Concluído", "Produto cadastrado com sucesso!")
        
            # Fechar a janela após cadastro
            self.cadastro_produto_janela.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para preço e quantidade.")
    
    def remover_produto(self):
        # Janela para remover produto
        self.remover_window = Toplevel(self.root)
        self.remover_window.title("Remover Produto")
        self.remover_window.geometry("300x200")

        # Label e entrada para o código do medicamento
        self.codigo_label = tk.Label(self.remover_window, text="Código do medicamento:", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.codigo_label.pack(pady=10)

        self.codigo_entry = tk.Entry(self.remover_window,font=("Helvética", 12))
        self.codigo_entry.pack(pady=5)

            # Função para remover produto
        def remover():
            codigo = self.codigo_entry.get()
            if codigo in estoque:
                del estoque[codigo]
                messagebox.showinfo("Concluído", f"Medicamento {codigo} removido com sucesso!")
                self.remover_window.destroy()
            else:
                messagebox.showerror("Erro", f"Medicamento {codigo} não encontrado.")
                self.codigo_entry.delete(0, tk.END)

        # Botão para executar a remoção
        self.remover_button = tk.Button(self.remover_window, text="Remover", command=remover)
        self.remover_button.pack(pady=15)

        # Botão de fechar
        self.fechar_button = tk.Button(self.remover_window, text="Fechar", command=self.remover_window.destroy)
        self.fechar_button.pack()


    def atualizar_produto(self):
        # Janela para atualizar produto
        self.atualizar_window = Toplevel(self.root)
        self.atualizar_window.title("Atualizar Produto")
        self.atualizar_window.geometry("300x300")

        # Label e entrada para o código do medicamento
        self.codigo_label = tk.Label(self.atualizar_window, text="Código do medicamento:",bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.codigo_label.pack(pady=10)

        self.codigo_entry = tk.Entry(self.atualizar_window,font=("Helvética", 12))
        self.codigo_entry.pack(pady=5)

        # Função para atualizar produto
        def atualizar():
            codigo = self.codigo_entry.get()
            if codigo in estoque:
                novo_nome = simpledialog.askstring("Novo nome", "Digite o novo nome do medicamento:", parent=self.atualizar_window)
                novo_preco = simpledialog.askstring("Novo preço", "Digite o novo preço do medicamento:", parent=self.atualizar_window)
                novo_quantidade = simpledialog.askstring("Nova quantidade", "Digite a nova quantidade do medicamento:", parent=self.atualizar_window)
            
                # Validações de preço e quantidade
                try:
                    novo_preco = float(novo_preco)
                    novo_quantidade = int(novo_quantidade)
                
                    produto = estoque[codigo]
                
                    if novo_nome:
                        produto.nome = novo_nome
                    if novo_preco:
                        produto.preco = novo_preco
                    if novo_quantidade:
                       produto.quantidade = novo_quantidade

                    messagebox.showinfo("Concluído", f"Medicamento {codigo} atualizado com sucesso!")
                    self.atualizar_window.destroy()
                except ValueError:
                    messagebox.showerror("Erro", "Preço ou quantidade inválidos.")
            else:
                messagebox.showerror("Erro", f"Medicamento {codigo} não encontrado.")

        # Botão para executar a atualização
        self.atualizar_button = tk.Button(self.atualizar_window, text="Atualizar", command=atualizar)
        self.atualizar_button.pack(pady=15)

        # Botão de fechar
        self.fechar_button = tk.Button(self.atualizar_window, text="Fechar", command=self.atualizar_window.destroy)
        self.fechar_button.pack()

    def listar_produtos(self):
        if estoque:
            # Cria uma nova janela para exibir a lista de produtos
            self.lista_produtos_janela = tk.Toplevel(self.root)
            self.lista_produtos_janela.title("Lista de Produtos")
            self.lista_produtos_janela.geometry("600x400")
        
            # Configuração de layout
            self.lista_produtos_janela.grid_columnconfigure(0, weight=1)
            self.lista_produtos_janela.grid_columnconfigure(1, weight=2)
            self.lista_produtos_janela.grid_columnconfigure(2, weight=1)
            self.lista_produtos_janela.grid_columnconfigure(3, weight=1)
            self.lista_produtos_janela.grid_columnconfigure(4, weight=1)

            # Cabeçalhos
            cabecalho = tk.Label(self.lista_produtos_janela, text="Código | Nome | Preço | Quantidade | Tipo", font=("Helvetica", 12, "bold"), bg="#D3D3D3", padx=10, pady=10)
            cabecalho.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

            # Linha separadora
            linha_separadora = tk.Label(self.lista_produtos_janela, text="-"*60, font=("Helvetica", 8), bg="#D3D3D3")
            linha_separadora.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="ew")
        
            # Exibe os produtos cadastrados em linhas
            for idx, produto in enumerate(estoque.values(), start=2):
                tk.Label(self.lista_produtos_janela, text=produto.codigo, font=("Helvetica", 12), padx=10, pady=5).grid(row=idx, column=0, padx=5, pady=5)
                tk.Label(self.lista_produtos_janela, text=produto.nome, font=("Helvetica", 12), padx=10, pady=5).grid(row=idx, column=1, padx=5, pady=5)
                tk.Label(self.lista_produtos_janela, text=f"R${produto.preco:.2f}", font=("Helvetica", 12), padx=10, pady=5).grid(row=idx, column=2, padx=5, pady=5)
                tk.Label(self.lista_produtos_janela, text=produto.quantidade, font=("Helvetica", 12), padx=10, pady=5).grid(row=idx, column=3, padx=5, pady=5)
                tk.Label(self.lista_produtos_janela, text=produto.tipo, font=("Helvetica", 12), padx=10, pady=5).grid(row=idx, column=4, padx=5, pady=5)

            # Botão Fechar
            botao_fechar = tk.Button(   self.lista_produtos_janela, text="Fechar", width=20, height=2, command=self.lista_produtos_janela.destroy, bg="#f44336", fg="white", font=     ("Helvetica", 12, "bold"))
            botao_fechar.grid(row=idx+1, column=0, columnspan=5, padx=10, pady=20)
        
        else:
            messagebox.showinfo("Lista de Produtos", "Não há produtos cadastrados.")

    def ask_input(self, prompt, is_number=False):
        """Pede ao usuário uma entrada simples com uma caixa de diálogo."""
        resposta = simpledialog.askstring("Entrada", prompt, parent=self.root)
    
        # Se for número, verifica se a resposta é válida
        if is_number:
            try:
               resposta = float(resposta)
               return resposta
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
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

    def clear_window(self):
        """Limpa todos os widgets da janela"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = FarmaciaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


