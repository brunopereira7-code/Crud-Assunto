import os 
os.system("cls ||clear") 

#CRUD usando lista 
#CREATE=criar / salvar
#Read=buscar/selecionar
#Update=atualizar/modificar
#Delete=excluir 

#criando uma lista 
lista_cliente=[] 


#Create
print('create - adicionar ; /Inserir') 
nome="Marta" 
lista_cliente.append(nome ) 
print(f"o nome:{nome} foi inserido com sucesso ") 

#Read 
print("\nRead - Ler / Mostrar") 
print(lista_cliente) 

#Update
print("\nUpdate-Atualizar / Alterar") 
nome_pra_atualizar="marta" 
if nome_pra_atualizar in lista_cliente:
    novo_nome="Marta silva" 
    #funçao:index
    indice=lista_cliente.index(nome_pra_atualizar) 
    lista_cliente[indice]=novo_nome 
    print(f"o nome {nome_pra_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"o nome {nome_pra_atualizar} nao foi encontrado") 

print(lista_cliente)

#Delete
print("\nDelete- Excluir \ Remover")
nome_para_excluir="Marta" 
if nome_para_excluir in lista_cliente:
    lista_cliente.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluido com sucesso")
else:
    print(f"o nome {nome_para_excluir} nao foi encontrado") 

print(lista_cliente)
