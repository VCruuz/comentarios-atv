def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
#calcula o juros diario em relação com o valor e com a taxa anual    

taxa_juros_diaria = taxa_juros_anual / 365 / 100
#divide a a taxa anual por 365 para ter a taxa de cada dia e depois divide por 100 para tirar a porcentagem

juros = valor_principal * taxa_juros_diaria * dias_atraso
#calcula o valor do juros  em relação com o valor principal e com os dias de atraso

valor_total = valor_principal + juros #calcula o valor total junto com o juros
return valor_total, juros #retorna o valor total e o valor do juros

valor_principal = 1000.00 #esse é o quanto é o valor principal
taxa_juros_anual = 5.0 #esse é o quanto é o valor do juros
dias_atraso = 30 #esse é o quanto são os dias de atraso

valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
#aqui ele tem a uma funçao para para calcular o valor total que deve ser pago junto com o juros

print(f"Valor total a ser pago: R${valor_total:.2f}") #aqui responde o quanto a pessoa teria que pagar, o valor total
print(f"Valor dos juros: R${juros:.2f}") #esse responde o valor dos juros