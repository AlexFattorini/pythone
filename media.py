somma = 0
conteggio = 0


domanda = input("Vuoi inserire un numero? (sì/no): ")
while domanda == "sì":
    valore = float(input("Inserisci il numero: "))
    somma += valore
    conteggio += 1

    domanda = input("Vuoi inserire un altro numero? (sì/no): ")


if conteggio > 0:
   
    print("La media dei numeri inseriti è: ", somma/conteggio)
else:
    print("Non sono stati inseriti numeri.")
