import os 
from dataclasses import dataclass 
os.system("cls") 

@dataclass 
class Pessoa:
    nome:str
    email:str 
    telefone:int 
    endereco:str

    def mostrar_resultados_pessoa(self): 
        print(f"seu nome é {self.nome}")
        print(f"seu email é {self.email}") 
        print(f"telefone é {self.telefone}") 
        print(f"endereco é {self.endereco}")

@dataclass 
class Produto:
    produto:str 
    quantidade:int 
    lote:str 
    validade:str



    def mostrar_resultados_produto(self): 
        print(f"seu produto é {self.produto}")
        print(f"sua quantidade é {self.quantidade}")
        print(f"seu lote é: {self.lote}")
        print(f"validade{self.validade}")
        
#inicio do programa
print("--Cadastro inicial---") 
cliente=Pessoa(nome=input("Digite seu nome:"),
               email=input("Qual seu e-mail:"),
               telefone=int(input("Digite seu telefone")),
               endereco=input("Digite seu endereço")
               )




menu={
    1:'pedir pedido',
    2:'adiconar pedido',
    3:'encerrar pedido'
}

pedidos=[] 

while True:
    print("Sistemas de pedidos") 
    for chave,valor in menu.items():
        print(f"{chave}-{valor}")
    try:
        pergunta=int(input("Peça seu pedido a partir do menu:")) 

        match pergunta:
            case 1:
                print("-----Novo pedido-----") 
                print("""
                  1-Picanha 
                  2-Pao com ovo 
                  3-suco de uva
                  4-carne de sertão
                  """) 
                prato_pedido=input("Digite o nome do prato:")
                pedidos.append(prato_pedido)
                print(f"{prato_pedido} foi adicionado com sucesso")

            case 2: 
                print("Adicionar pedido") 
                mais_um=input("Gostaria de adicionar pedido s ou n:")
                if mais_um =='n':
                    break #continue
                
                if mais_um=='s': 
                    
                    print("""
                    1-Picanha 
                    2-Pao com ovo 
                    3-suco de uva
                    4-carne de sertão
                      """)
                    prato_pedido2=input("Qual prato gostaria de pedir")
                    #a lista vem primeiro depois vem a variavel

                    pedidos.append(prato_pedido2)
                    print(f"sucesso {prato_pedido2} foi adicionado com sucesso")

            case 3: 
                print("Saindo do programa....") 
                cliente.mostrar_resultados_pessoa()
                
                print("\n---Resumo do pedido")
                if not pedidos:
                    print("nenhum item pedido") 
                else:
                    print(f"total de itens {len(pedidos)}") 
                    print(f"pratos:{','.join(pedidos)}") 
                    

                break

            case _:
                print("opçao invalida") 

    
    except ValueError:
        print("Errado veja o que se pede")
            


#------------------------------------------------------------------------------------------------------------------------------------------------

#print(f"Logradouro: {self.endereco.logradouro}")
#print(f"Número: {self.endereco.numero}")
#print(f"Cidade: {self.endereco.cidade}")
#---------------------------------------------
# print(f"seu nome é {self.nome}")
# print(f"seu nome é {self.idade}")               
# print(f"seu curso é {self.curso}")
# print(f"seu endereço é {self.endereco}") 
# print(f"seu logradouro é {self.logradouro}")
# print(f"seu numero da cada é {self.numero}")  

#voce chamar o objeto cliente e nao a variavel
#pergunta.mostrar_resultado_produto()
                # print("\n--- ITENS PEDIDOS ---")
                # print(f"Total de itens: {len(pedidos)}")
                # print(f"Itens: {', '.join(pedidos)}")