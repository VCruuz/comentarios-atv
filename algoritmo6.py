def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio): #aqui comeca para calcular o custo de uma viagem

custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel  #calcula o combustivel total que é a distancia dividido pelo consumo

custo_pedagio_total = numero_pedagios * custo_pedagio #custo do pedagio uqe é o numero do pedagio vezes o custo

custo_total = custo_combustivel_total + custo_pedagio_total #aqui p-é o custo tatal que é a adição das outras coisas

return custo_total, custo_combustivel_total, custo_pedagio_total #retorna o custo den tudo
 
distancia = float(input("Digite a distância da viagem (em km): ")) #aqui esta escrito oque é para digitar
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): ")) #aqui esta escrito oque é para digitar
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): ")) #aqui esta escrito oque é para digitar
numero_pedagios = int(input("Digite o número de pedágios no percurso: ")) #aqui esta escrito oque é para digitar
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): ")) #aqui esta escrito oque é para digitar

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, #chama a funcao para calcular tudo
custo_combustivel,
consumo_veiculo, numero_pedagios, 

custo_pedagio)

print(f"Custo total da viagem: R${custo_total:.2f}") #aqui ta o custo da viagem
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}") #aqui o custo total do combustivel
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}") #e o custo dos pedagios