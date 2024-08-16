def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #calcula se uma pessoa tem diabets ou nao

if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: #verifica se uma pessoa esta com uma glicemia em jejum maior ou igual que 126, ou uma glicemia pos prandial maior ou igual que 200
return "Diabetes" #se sim, em uma das duas, retorna que essa pessoa tem diabetes
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:#agora se a glicemia em jejum estiver entre 100 até 125, ou se a glicemia pos prandial estiver menor que 200
return "Pré-diabetes" #retorna que a pessoa é pre-diabetica
else: 
return "Normal" #senão retorna que essa pessoa é normal

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #pede para a pessoa colocar quanto ta a glicemia dela em jejum 
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) #pede para colocar quanto ta a glicemia pos prandial

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #aqui traz a funçao para trazer o resultado
print(f"O diagnóstico é: {resultado}") #tras o resultado se a pessoa é diabetica ou pre diabetica ou nao é diabetica