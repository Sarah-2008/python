cor = input("Digite a cor do semáforo (em letras minúsculas): ")

tipo = input("Você é pedestre ou motorista? ")

if cor == "verde":
    print("Pode avançar com atenção.")

elif cor == "amarelo":
    print("Atenção! Prepare-se para parar.")

elif cor == "vermelho":
    if tipo == "pedestre":
        print("Você pode atravessar com atenção.")
    else:
        print("Pare! Aguarde o sinal verde.")

else:
    print("Cor inválida. Digite verde, amarelo ou vermelho.")