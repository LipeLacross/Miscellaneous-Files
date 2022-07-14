while True:
    dia = int(input("Dia: "))
    dia_valido = dia > 0 and dia <=31
    if (dia_valido):
        break
    print("Dia informado é inválido")
