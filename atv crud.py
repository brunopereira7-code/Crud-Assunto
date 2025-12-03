import os

# --- BANCO DE DADOS (Simulado com uma Lista) ---
lista_clientes = []

def limpar_tela():
    os.system("cls")

# --- MENU ---
menu_opcoes = {
    1: "Cadastrar Cliente",
    2: "Listar Clientes",
    3: "Atualizar Cliente",
    4: "Deletar Cliente",
    5: "Sair"
}

while True:
    print("\n--- SISTEMA DE CLIENTES (CRUD COM MATCH CASE) ---")
    for chave, valor in menu_opcoes.items():
        print(f"[{chave}] - {valor}")
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
        limpar_tela()

        
        match opcao:
            
            # CASO 1: CREATE
            case 1:
                print("--- NOVO CADASTRO ---")
                nome = input("Nome do cliente: ").strip()
                email = input("E-mail do cliente: ").strip()
                novo_cliente = {"nome": nome, "email": email}
                lista_clientes.append(novo_cliente)
                print("✅ Cliente cadastrado com sucesso!")

            # CASO 2: READ
            case 2:
                print("--- LISTA DE CLIENTES ---")
                if not lista_clientes:
                    print("Nenhum cliente cadastrado.")
                else:
                    for i, cliente in enumerate(lista_clientes):
                        print(f"ID {i} | Nome: {cliente['nome']} | Email: {cliente['email']}")

            # CASO 3: UPDATE
            case 3:
                print("--- ATUALIZAR DADOS ---")
                for i, cliente in enumerate(lista_clientes):
                    print(f"ID {i} - {cliente['nome']}")
                
                # Como temos inputs aqui dentro, é bom proteger contra erro de valor também
                try:
                    id_atualizar = int(input("Digite o ID do cliente que deseja atualizar: "))
                    if 0 <= id_atualizar < len(lista_clientes):
                        novo_nome = input(f"Novo nome (atual: {lista_clientes[id_atualizar]['nome']}): ")
                        novo_email = input(f"Novo email (atual: {lista_clientes[id_atualizar]['email']}): ")
                        lista_clientes[id_atualizar]['nome'] = novo_nome
                        lista_clientes[id_atualizar]['email'] = novo_email
                        print("✅ Dados atualizados!")
                    else:
                        print("❌ ID não encontrado.")
                except ValueError:
                    print("Erro: ID inválido.")

            # CASO 4: DELETE
            case 4:
                print("--- DELETAR CLIENTE ---")
                for i, cliente in enumerate(lista_clientes):
                    print(f"ID {i} - {cliente['nome']}")
                
                try:
                    id_deletar = int(input("Digite o ID do cliente para deletar: "))
                    if 0 <= id_deletar < len(lista_clientes):
                        removido = lista_clientes.pop(id_deletar)
                        print(f"🗑️ Cliente {removido['nome']} removido com sucesso!")
                    else:
                        print("❌ ID não encontrado.")
                except ValueError:
                    print("Erro: ID inválido.")

            # CASO 5: SAIR
            case 5:
                print("Saindo do sistema...")
                break

            # CASO PADRÃO (Equivalente ao 'else')
            # O underline (_) significa "qualquer outra coisa"
            case _:
                print("Opção inválida!")

    except ValueError:
        print("Erro: Digite apenas os números do menu.")