let nomeHeroi = "Shaka de Virgem"
let xpAtual = 13000
let nivelHeroi = 9000

if (xpAtual >=0 && xpAtual <= 1000){
    nivelHeroi = "Ferro"
} else if (xpAtual >= 1001 && xpAtual <= 2000){
    nivelHeroi = "Bronze"
} else if (xpAtual >= 2001 && xpAtual <= 5000){
    nivelHeroi = "Prata"
} else if (xpAtual >= 5001 && xpAtual <= 7000){
    nivelHeroi = "Ouro"
} else if (xpAtual >= 7001 && xpAtual <= 8000){
    nivelHeroi = "Platina"
} else if (xpAtual >= 8001 && xpAtual <= 9000){
    nivelHeroi = "Ascendente"
} else if (xpAtual >= 9001 && xpAtual <= 10000){
    nivelHeroi = "Imortal"
} else{
    nivelHeroi = "Radiante" 
}

console.log ("O Herói de nome " + nomeHeroi + " está no nível de: " + nivelHeroi)