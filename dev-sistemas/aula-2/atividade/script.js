// Informações do jogador
const nomeJogador = "Carlos";
let idade = 20;
let online = true;

// Jogo favorito
const jogoFavorito = {
    nome: "Minecraft",
    anoLancamento: 2011
};

// Últimas 3 pontuações
const pontuacoes = [850, 920, 780];

// Mostrando os valores e seus tipos
console.log("Nome:", nomeJogador);
console.log("Tipo:", typeof nomeJogador);

console.log("Idade:", idade);
console.log("Tipo:", typeof idade);

console.log("Online:", online);
console.log("Tipo:", typeof online);

console.log("Jogo favorito:", jogoFavorito);
console.log("Tipo:", typeof jogoFavorito);

console.log("Pontuações:", pontuacoes);
console.log("Tipo:", typeof pontuacoes);

// Alterando a idade e o status online
idade = 21;
online = false;

console.log("Nova idade:", idade);
console.log("Novo status online:", online);

// Tentativa de alterar o nome
// nomeJogador = "João";
// Isso causaria um erro porque nomeJogador foi declarado com const.

// Calculando a média das pontuações
const media = (pontuacoes[0] + pontuacoes[1] + pontuacoes[2]) / 3;

console.log(`A média de pontos do jogador ${nomeJogador} foi: ${media}`);