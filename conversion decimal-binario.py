numero = int(input("Ingresa un número decimal de dos cifras: "))

if numero < 0 or numero > 99:
    print("El número debe estar entre 0 y 99.")
else:
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    while len(binario) < 8:
        binario = "0" + binario

    print("Su número binario es:", binario)
