#limpando o terminal

import os
os.system ("clear || cls")

#atividade pontuada

total = 0

while True:
    #mostrando a tabela
    codigo = int(input(""" 
 CÓDIGO  |       PRATO        |   VALOR        
   1     |      PICANHA       |  R$25,00                                      
   2     |      LASANHA       |  R$20,00
   3     |     STROGONOFF     |  R$18,00 
   4     |   BIFE ACEBOLADO   |  R$15,00         
   5     |    PÃO COM OVO     |  R$5,00  
   6     |  MOQUECA DE PEIXE  |  R$21,00
   7     |     FEIJOADA       |  R$22,00  

Digite o código do seu pedido:
"""))
    #pedindo o prato       
    match codigo:
        case 1:
            valor = 25
        case 2:
            valor = 20
        case 3:
            valor = 18
        case 4:
            valor = 15
        case 5:
            valor = 5
        case 6:
            valor = 21
        case 7:
            valor = 22
        case _:
            print("Opção inválida")
     #Armazendando os valores   
    total += valor
    #Pedindo outros pratos 
    outro_pedido = input("Deseja pedir algo mais? (digite 0 caso não queira): ")    
    #Terminando o pedido
    if outro_pedido == "0":
        print(f"Total: {valor_pagar}")
        break
    #escolhendo a forma de pagamento    
    forma_pagamento = int(input("""
    Forma de pagamento:
    CÓDIGO |      FORMA
       1   |      Á vista 
       2   |  Cartão de crédito
        
        Informe o código da forma de pagamento: """))
    match forma_pagamento:
        #calculando desconto
        case 1:
            desconto = total * 0.10
            valor_pagar = total - desconto
        #calculando o acréscimo
        case 2:
            desconto = total * 0.10 
            valor_pagar = total + desconto
#exibindo resultados
print (f"")
print (f"Subtotal: {total}")
print (f"Forma de pagamento escolhida: {forma_pagamento}")
print (f"Total do desconto ou acréscimo: {desconto}")
print (f"Valor final: {valor_pagar}")