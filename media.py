somma = 0
conteggio = 0

while True:
    domanda = input("Vuoi inserire un numero? (sì/no): ")

    if domanda == "no":
        break

    if domanda == "sì":

        valore = float(input("Inserisci il numero: "))
        somma += valore
        conteggio += 1


if conteggio > 0:
    media = somma / conteggio
    print(f"La media dei numeri inseriti è: {media}")
else:
    print("Non sono stati inseriti numeri.")
