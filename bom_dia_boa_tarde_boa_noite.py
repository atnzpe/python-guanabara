"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
 exiba a saudação apropriada. Ex.
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
try:
    hour = input("Que horas são? ")

    hour_int = int(hour)

    bom_dia = hour >= 0 and hour <= 11
    boa_tarde = hour >= 12 and hour <= 17
    boa_noite = hour >= 18 and hour <= 23

    if bom_dia:
        print("bom dia!")
    elif boa_tarde:
        print("Boa tarde!")
    elif boa_noite:
        print("Boa Noite!")

except:
    print("Voce não digitou um número!")
