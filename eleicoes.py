def ganhador(voto1,voto2):
  if voto1 == voto2:
     return 0
  elif voto1 > voto2:
     return 1
  else:
     return 2

politico = []
politico.append(input("Digite o nome do primeiro candidato:"))
politico.append(input("Digite o nome do segundo  candidato:"))
states_arq = input("Digite o nome do arquivo:")
std = open(states_arq,"r")
contagem = []
quant_voto = [0,0]
tab = 0

for linha in std:
  delegate = linha.strip().split("#")
  states = open(delegate[0])
  eleicao = {politico[0]:0, politico[1]:0}
  contagem.append([delegate[0],0,0])

  for vote in states:
    eleicao[vote.strip()]+=1

  champion = ganhador(eleicao[politico[0]],eleicao[politico[1]])
  
  if champion == 0:
     contagem[tab][1] = int(delegate[1])
     contagem[tab][2] = int(delegate[1])
  else:
     contagem[tab][champion] = int(delegate[1])
  quant_voto[0]+=eleicao[politico[0]]
  quant_voto[1]+=eleicao[politico[1]]
  tab+=1
  states.close()
std.close()

for i in range(len(politico)):
  print(politico[i]+" conquistou Delegado(s) no(s) Estado(s):")
  mont=0
  for j in range(len(contagem)):
    if contagem[j][i+1]:
      print("    "+contagem[j][0]+": "+str(contagem[j][i+1]))
      mont+=contagem[j][i+1]
  print("Total de Delegados para "+politico[i]+": "+str(mont))
  print("Total de Votos para "+politico[i]+": "+str(quant_voto[i]))
  print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")