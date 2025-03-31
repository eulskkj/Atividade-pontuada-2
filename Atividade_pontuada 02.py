#limpando o terminal

import os
os.system ("clear || cls")

#atividade pontuada

total = 0
junta_prato = ""
pratos_escolhidos = []




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
            nome = "Picanha"
            valor = 25
        case 2:
            nome = "Lasanha"
            valor = 20
        case 3:
            nome = "Strogonoff"
            valor = 18
        case 4:
            nome = "Bife acebolado"
            valor = 15
        case 5:
            nome = "Pão com ovo"
            valor = 5
        case 6:
            nome = "Moqueca de peixe"
            valor = 21
        case 7:
            nome = "Feijoada"
            valor = 22
        case _:
            print("Opção inválida")
            continue
         
     #Armazendando os valores   
    total += valor
    pratos_escolhidos.append(f"{codigo} - {nome}")
    #Pedindo outros pratos 
    outro_pedido = input("Deseja pedir algo mais? (digite 0 caso não queira e 1 para continuar.): ")  

    #Terminando o pedido
    if outro_pedido == "0":
        break
    

    #escolhendo a forma de pagamento    
forma_pagamento = int(input("""
Forma de pagamento:
CÓDIGO |      FORMA
   1   |      Á vista 
   2   |  Cartão de crédito
    
Informe o código da forma de pagamento:  """))

#calculando desconto
if forma_pagamento == 1:
    desconto = total * 0.10
    valor_pagar = total - desconto
#calculando o acréscimo
elif forma_pagamento == 2:
    desconto = total * 0.10 
    valor_pagar = total + desconto
else: 
    print("Escolha 1 para pagamento á vista ou 2 para pagamento de cartão de credito.")
    

#exibindo resultados
print("\n=== RESUMO DO PEDIDO ===")
print("Pratos escolhidos:")
for prato in pratos_escolhidos:
    print(prato)
print (f"Pratos escolhidos: {junta_prato}")
print (f"Forma de pagamento escolhida: {forma_pagamento}")
print (f"Subtotal: R${total:.2f}")
print (f"Total do desconto ou acréscimo: R${desconto:.2f}")
print (f"Valor final: R${valor_pagar:.2f}")
print(f"Obrigado pela preferência e um bom apetite.")