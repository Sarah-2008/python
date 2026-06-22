lado_a = float(input("Informe o lado A: "))
lado_b = float(input("Informe o lado B: "))
lado_c = float(input("Informe o lado C: "))


if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:

    print("Os lados formam um triângulo válido.")

    if lado_a == lado_b and lado_b == lado_c:
        print("Classificação: Equilátero")

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Classificação: Isósceles")

    else:
        print("Classificação: Escaleno")

else:
    print("Os valores informados não formam um triângulo válido.")