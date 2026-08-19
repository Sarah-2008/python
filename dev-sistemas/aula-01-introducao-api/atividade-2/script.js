const botao = document.getElementById("buscar");
const cidade = document.getElementById("cidade");
const resultado = document.getElementById("resultado");

botao.addEventListener("click", () => {
    const coordenadas = cidade.value.split(",");
    const lat = coordenadas[0];
    const lon = coordenadas[1];

    const nomeCidade = cidade.options[cidade.selectedIndex].text;

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    fetch(url)
        .then(resposta => resposta.json())
        .then(data => {
            const temperatura = data.current_weather.temperature;

            let icone;
            let fundo;

            if (temperatura < 20) {
                icone = "❄️";
                fundo = "linear-gradient(180deg, #2196f3, #64b5f6)";
            } else if (temperatura < 30) {
                icone = "⛅";
                fundo = "linear-gradient(180deg, #78909c, #b0bec5)";
            } else {
                icone = "☀️";
                fundo = "linear-gradient(180deg, #ff9800, #f44336)";
            }

            document.body.style.background = fundo;

            resultado.innerHTML = `
                <h2>${nomeCidade}</h2>
                <div style="font-size: 60px;">${icone}</div>
                <p><strong>Temperatura atual:</strong></p>
                <p style="font-size: 30px;">${temperatura} °C</p>
            `;
        })
        .catch(erro => {
            resultado.innerHTML = `
                <p>Não foi possível consultar os dados do clima.</p>
            `;
        });
});