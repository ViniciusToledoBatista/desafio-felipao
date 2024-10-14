nomeHeroi = str (input ("Insira o nome do Herói: "))
xpAtual = int (input ("Insira a XP atual: "))
nivelHeroi = ""

if (xpAtual >= 0 and xpAtual <= 1000):
    nivelHeroi = "Ferro"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 1001 and xpAtual <= 2000):
    nivelHeroi = "Bronze"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 2001 and xpAtual <= 5000):
    nivelHeroi = "Prata"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 5001 and xpAtual <= 7000):
    nivelHeroi = "Ouro"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 7001 and xpAtual <= 8000):
    nivelHeroi = "Platina"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 8001 and xpAtual <= 9000):
    nivelHeroi = "Ascendente"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual >= 9001 and xpAtual <= 10000):
    nivelHeroi = "Imortal"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
elif (xpAtual > 10000):
    nivelHeroi = "Radiante"
    print ("O Herói de nome " + nomeHeroi + " está no nível de " + nivelHeroi)
else:
    print ("A XP inserida é inválida")