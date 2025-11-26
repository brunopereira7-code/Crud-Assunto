import os 
os.system("cls ||clear") 

#CRUD usando lista 
#CREATE=criar / salvar
#Read=buscar/selecionar
#Update=atualizar/modificar
#Delete=excluir 

#criando uma lista 
lista_cliente=[] 

# menu={""
# "1- Create",
# "2-Read",
# "3-Update",
# "4-Delete"}

# print(f"-------{menu}-------------")
print("1- Create",
      "2-Read",
      "3-Update",
      "4-Delete")

try:
    pergunta=input("Qual oplao você gostaria?")
    match pergunta:
        case "1":
            nome=input("Digite seu nome")
            lista_cliente.append(nome ) 
            print(f"o nome:{nome} foi inserido com sucesso ") 

        case "2":
            print(lista_cliente) 

                #Update
                # print("\nUpdate-Atualizar / Alterar") 
        case"3":

            nome_pra_atualizar=nome
            if nome_pra_atualizar in lista_cliente:
                novo_nome=input("Digite o novo nome") 
            #funçao:index
                indice=lista_cliente.index(nome_pra_atualizar) 
                lista_cliente[indice]=novo_nome 
                print(f"o nome {nome_pra_atualizar} foi atualizado para {novo_nome}")
            else:
                print(f"o nome {nome_pra_atualizar} nao foi encontrado") 

                print(lista_cliente)

        case"4":
            nome_para_excluir=input("Digite qual nome deve ser excluido")
            if nome_para_excluir in lista_cliente:
                lista_cliente.remove(nome_para_excluir)
                print(f"{nome_para_excluir} foi excluido com sucesso")
            else:
                print(f"o nome {nome_para_excluir} nao foi encontrado") 

                print(lista_cliente)
except ValueError:
    print("erro Digite os valores certo ")