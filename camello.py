import random
hecho = False
millas = 0
sed = 0
cansancio = 0
nativos = -20
cantimplora = 20
print("Bienvenido al Camello!")
print("Has robado un camello para atravesar el gran desierto del Mobi.")
print("Los nativos quieren que les devuelvas su camello y salen en persecución tuya!")
print("Tendrás que sobrevivir al desierto y correr más que los nativos.")
print()
while not hecho:

    print("A. Beber de la cantimplora.")
    print("B. Velocidad moderada hacia adelante.")
    print("C. A toda velocidad hacia adelante.")
    print("D. Para y descansa.")
    print("E. Comprueba tu estado.")
    print("Q. Salir.")
    a = input("¿Qué eliges?: ")
    if(a.upper() == "A"):
        print("Has consumido de la cantimplora.")
        cantimplora = cantimplora-5
        sed=sed-5
        nativos = random.randint(1,30)
        print("Nativos estan a ",nativos,"millas")
        if(sed == -1):
            sed = 0
            print("Tu sed es de ",sed,"%")
            print("Has perdido de la cantimplora ",cantimplora,"% ","has recorrido ",millas," millas.")
            print("Venga tu puedes...")
            print()
        if cansancio == 20:
            print("Has muerto por cansancio , has perdido.")
            hecho = True
        if millas == 30:
            print("Has recorrido todo el desierto, has ganado.")
            print("Enhorabuena")
            hecho = True
        if sed == 20:
            print("Te has muerto de sed, has perdido.")
            hecho = True
        if nativos == 30:
            print("Los nativos te han pillado , has perdido.")
            hecho = True
    if(a.upper() == "B"):
        print("Has consumido energia.")
        cansancio=cansancio+5
        sed=sed+5
        millas=millas+10
        nativos = random.randint(1,30)
        nativos = nativos - 5
        print("Nativos estan a ",nativos,"millas")
        print("Tu cansancio es de ",cansancio,"% ","has recorrido ",millas," millas.")
        print("Venga tu puedes...")
        print()
        print("Tu sed ha aumentado revisa tu estado.")
        if cansancio == 20:
            print("Has muerto por cansancio , has perdido.")
            hecho = True
        if millas == 30:
            print("Has recorrido todo el desierto, has ganado.")
            print("Enhorabuena")
            hecho = True
        if sed == 30:
            print("Te mueres de sed, has perdido.")
            hecho = True
        if nativos == 30:
            print("Los nativos te han pillado , has perdido.")
            hecho = True
    if(a.upper() == "C"):
        cansancio=cansancio+10
        millas=millas+10
        sed=sed+5
        nativos = random.randint(1,30)
        nativos = nativos -10
        print("Nativos estan a ",nativos,"millas")
        print("Tu cansancio es de ",cansancio,"%")
        print("Venga tu puedes...")
        print()
        if cansancio == 20:
            print("Has muerto por cansancio , has perdido.")
            hecho = True
        if millas == 30:
            print("Has recorrido todo el desierto, has ganado.")
            print("Enhorabuena")
            hecho = True
        if sed == 30:
            print("Te has muerto de sed, has perdido.")
            hecho = True
        if nativos == 30:
            print("Los nativos te han pillado , has perdido.")
            hecho = True
    if(a.upper() == "D"):
        cansancio=2
        print("Tu energía comienza a subir un ",cansancio,"%","pero los nativos se acercan.")
        nativos = random.randint(1,30)
        print("Nativos estan a ",nativos,"millas")
        if cansancio == 5:
            print("Has muerto por cansancio , has perdido.")
            hecho = True
        if millas == 30:
            print("Has recorrido todo el desierto, has ganado.")
            print("Enhorabuena")
            hecho = True
        if sed == 20:
            print("Te has muerto de sed, has perdido.")
            hecho = True
        if nativos == 30:
            print("Los nativos te han pillado , has perdido.")
            hecho = True
    elif(a.upper() == "E"):
        print("Mi estado:")
        print("Cansancio: ",cansancio,"%")
        print("Sed: ",sed,"%")
        print("Nativos: ",nativos,"millas")
        print("Cantimplora: ",cantimplora,"%")
    if(a.upper() == "Q"):
        hecho = True
