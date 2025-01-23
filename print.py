aliquota1 = 0.23
aliquota2 = 0.35
aliquota3 = 0.43
reddito = float(input("Inserisci il tuo reddito: "))

if reddito <= 28000:
    print("La tua aliquota è del", int(aliquota1 * 100), "%")
    print("L'imposta da pagare è:", reddito * aliquota1, "euro")
elif reddito <= 50000:
    print("La tua aliquota è del", int(aliquota2 * 100), "%")
    print("L'imposta da pagare è:", reddito * aliquota2, "euro")
else:
    print("La tua aliquota è del", int(aliquota3 * 100), "%")
    print("L'imposta da pagare è:", reddito * aliquota3, "euro")
