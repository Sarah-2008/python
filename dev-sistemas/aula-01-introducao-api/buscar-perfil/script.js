const botaoBuscar = document.getElementById("buscar");

botaoBuscar.addEventListener("click", () => {
    const nome = document.getElementById("usuario").value.trim();
    const perfil = document.getElementById("perfil");

    if (nome === "") {
        perfil.innerHTML = "<p>Digite um usuário!</p>";
        return;
    }

    fetch(`https://api.github.com/users/${nome}`)
        .then(resp => {
            if (!resp.ok) {
                throw new Error("Usuário não encontrado!");
            }

            return resp.json();
        })
        .then(dados => {
            perfil.innerHTML = `
                <img src="${dados.avatar_url}" alt="Foto de ${dados.name || nome}" width="150">
                <h3>${dados.name || "Nome não informado"}</h3>
                <p>${dados.bio || "Biografia não informada."}</p>
            `;
        })
        .catch(erro => {
            perfil.innerHTML = `<p>${erro.message}</p>`;
        });
});