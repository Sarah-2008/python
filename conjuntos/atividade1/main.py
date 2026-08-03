produtos = [
    (1001, "monitor", 24, 18),
    (1002, "Mouse", 12, 14),
    (1003, "placa mae", 36, 10),
    (1004, "Teclado", 12, 12),
    (1005, "Impressora", 24, 30)
]

em_garantia = 0
vencidos = 0

print(f"{'Código':<8} {'Nome':<12} {'Garantia':<12} {'Uso':<8} Situação")

for produto in produtos:
    # Desempacotamento 
    codigo, nome, garantia, uso = produto

    if uso <= garantia:
        restante = garantia - uso
        print(f"{codigo:<8} {nome:<12} {garantia} meses    {uso}m      Em garantia ({restante} meses restantes)")
        em_garantia += 1
    else:
        atraso = uso - garantia
        print(f"{codigo:<8} {nome:<12} {garantia} meses    {uso}m      Garantia vencida ({atraso} meses atrás)")
        vencidos += 1

print("\n=== Resumo ===")
print(f"Total: {len(produtos)} | Em garantia: {em_garantia} | Vencidos: {vencidos}")