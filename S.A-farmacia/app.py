from modelos import Produto
from database import criar_tabela
import controle

# Cria a tabela no banco de dados
criar_tabela()

# Adiciona um medicamento

medicamentos = []

def menu_farmacia():
     while True:
        print("""
 _________|=========================|__________
|         |  MENU SISTEMA FÁRMACIA  |          |
|         |=========================|          |
|                                              |
| [ 1 ] Adicionar medicamento                  |
| [ 2 ] Remover medicamento                    |
| [ 3 ] Atualizar medicamento                  |
| [ 4 ] Mostrar medicamento                    |
| [ 5 ] Sair do programa                       |
|                                              |
================================================""")
        decisao = int(input("Escolha a ação: "))
        if decisao == 1:
         med = Produto()
         controle.adicionar_medicamento(med.nome, med.preco, med.quantidade)
         medicamentos.append (med)
        elif decisao == 2:
         med    
        elif decisao == 3:
         pass  
        elif decisao == 4:
           pass
        elif decisao == 5:
         break
        else:
            print("Ação inválida.")
