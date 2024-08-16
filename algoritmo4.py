def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #comeca uma variavel para calcular a media e ver quem esta aprovado
total_notas = 0 
num_alunos = len(notas) #pega a informação de quantos alunos tem
aprovados = [] #lista para ter os alunos aprovados
reprovados = [] #lista para ter os alunos reprovados

for aluno, nota in notas.items(): #cria meio que um looppara ver as notas
total_notas += nota 
if nota >= nota_minima_aprovacao: #adiciona a nova nota ao total de notas ja colocadas
aprovados.append(aluno)
else:  #verifica se a nota do aluno é maio do que o minimo que precisa, se sim o aluno é aprovado
reprovados.append(aluno) #senao o aluno é reprovado

media_turma = total_notas / num_alunos #aqui faz a media de todas as notas

return media_turma, aprovados, reprovados #retorna a media de todas as notas, os aprovados e os reprovados

notas = {  #traz as notas das pessoas
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70 #declara a nota minima

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

print(f"Média da turma: {media_turma:.2f}") #mostra a media das notas
print(f"Alunos aprovados: {', '.join(aprovados)}") #os alunos aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}") #e os alunos reporvados