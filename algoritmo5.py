def calcular_imc(peso, altura): #comeca para calcular o seu imc

imc = peso / (altura ** 2) #indica oq é imc, é seu peso dividido por sua altura ao quadrado
return imc #retorna o seu imc

def classificar_imc(imc): #define os imcs que podem dar

if imc < 18.5:
return "Abaixo do peso" #se menor que 18.5 é abaixo do peso
elif 18.5 <= imc < 24.9: #se entre 18.5 e 24.8 é normal
return "Peso normal" 
elif 25 <= imc < 29.9: #se for entre 25 e 29.8 é sobrepeso
return "Sobrepeso"
elif 30 <= imc < 34.9:
return "Obesidade grau 1" #se entre 30 e 34.8 é obesidade grau 1
elif 35 <= imc < 39.9:
return "Obesidade grau 2" #se entre 35 e 39.8 é obesidade grau 2
else:
return "Obesidade grau 3" #senao é obesidade grau 3

def sugestao_atividade_fisica(classificacao_imc): #aqui traz sugestoes de atividades fisicas

if classificacao_imc == "Abaixo do peso":
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em  #se for abaixo do peso sugere essas atividades entre "
proteínas e calorias."    
elif classificacao_imc == "Peso normal":
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado." #se for normal do peso sugere essas atividades entre "
elif classificacao_imc == "Sobrepeso":
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além ##se for sobrepeso do peso sugere essas atividades entre "
de exercícios de resistência."
elif classificacao_imc == "Obesidade grau 1": 
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um  ##se for obesidade 1 do peso sugere essas atividades entre "
programa de reeducação alimentar."
elif classificacao_imc == "Obesidade grau 2":
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional." #se for obesidade 2