def calcular_area_comodos(): #comeca uma variavel para calcular a area dos comodos
total_area = 0

while True: #enquanto nao quiser parar vai continuando, criando meio que um loop

largura = float(input("Digite a largura do cômodo (em metros): ")) #pede para colocar em metros a largura de um comodo
comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) #pede para colocar em metros o comprimento do comodo

area_comodo = largura * comprimento #Aqui faz que o valor da area seja igual a largura que foi colocada vezes o comprimento tambem colocado
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #aqui mostra o quanto vale a area do comodo

total_area += area_comodo #aqui junta a area total com a area docomodo

mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() #aqui pergunta se quer adicionar mais algum comodo
if mais_comodos != 's': #aqui se a resposta for s ele continua, se não for ele para 
break

return total_area #aqui ele retorna o valor da area total

area_total = calcular_area_comodos() #aqui ele traz a funcao para calculat a area total com um ou mais comodos
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")#aqui mostra como ficou a area total 