const input = document.getElementById("tituloInput");
const botaoCriar = document.getElementById("criarCard");
const container = document.getElementById("container");

botaoCriar.addEventListener("click", function () {

    // Pega o valor digitado
    const titulo = input.value.trim();

    // Verifica se o input está vazio
    if (titulo === "") {
        alert("Digite um título!");
        return;
    }

    // Cria o card
    const card = document.createElement("div");

    // Cria o h3
    const h3 = document.createElement("h3");
    h3.textContent = titulo;

    // Cria o botão Remover
    const botaoRemover = document.createElement("button");
    botaoRemover.textContent = "Remover";

    // Função para remover o card
    botaoRemover.addEventListener("click", function () {
        card.remove();
    });

    // Coloca o h3 e o botão dentro do card
    card.appendChild(h3);
    card.appendChild(botaoRemover);

    // Coloca o card dentro do container
    container.appendChild(card);

    // Limpa o input
    input.value = "";
});