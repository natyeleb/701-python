import statistics as es

historia_n1 = float(input("digite sua nota 1: "))
historia_n2 = float(input("digite sua nota 2: "))

listas = [historia_n1, historia_n2]
media = es.mean(listas)
print(media)

if media >= 7:
    print("aprovado")

elif media >= 5 and media < 7:
    print("recuperacao")

else:
    print("reprovado")    