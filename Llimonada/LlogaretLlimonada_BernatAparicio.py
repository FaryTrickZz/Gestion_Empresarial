import time

adminUsers = []
ingredientes = [["Llimona/u","Sucre/g","Agua/ml"],["20","1000","10000"]]
limonada = 0

def altaAdmin():
    usuario = input("Introdueix el nom d'usuari: ")
    passwd = input("Introdueix una contrasenya: ")
    adminUsers.append(usuario+"/"+passwd)
    print("L'usuari s'ha creat correctament")
    time.sleep(1)

def comandaStock():
    print("L'estock actual es: ")
    #Se muestra el stock actual de los ingredientes
    print(ingredientes[0][0]+": ",ingredientes[1][0],"\n"+ingredientes[0][1]+": ",ingredientes[1][1],"\n"+ingredientes[0][2]+": ",ingredientes[1][2])
    time.sleep(2)
    print("Introdueix la quantitat que vols augmentar dels seguents ingredients.")
    #Input de la cantidad a añadir de cada ingrediente
    ingredientes[1][0] = str(int(ingredientes[1][0]) + int(input("Quantitat de llimones en unitats: ")))
    ingredientes[1][1] = str(int(ingredientes[1][1]) + int(input("Quantitat de sucre en g: ")))
    ingredientes[1][2] = str(int(ingredientes[1][2]) + int(input("Quantitat d'aigua en ml: ")))

def produirLlimonada():
    #Depende de la cantidad de ingredientes que haya se muestra un mensaje para hacer una comanda de stock o no hacerla
    if (int(ingredientes[1][0])<12 or int(ingredientes[1][1])<240 or int(ingredientes[1][2])<2400):
        print("Els ingredients per produir llimonada s'setan acabant, conve fer una comanda")

    if (int(ingredientes[1][0])<4 or int(ingredientes[1][1])<80 or int(ingredientes[1][2])<800):
        print("No hi ha llimones suficients per produir llimonada")

    elif(int(ingredientes[1][1]) < 240):
        print("No hi ha sucre suficient per produir llimonada")

    elif(int(ingredientes[1][2])<2400):
        print("No hi ha aigua suficient per produir llimonada")

    else:
        ingredientes[1][0] = str(int(ingredientes[1][0]) - 4)
        ingredientes[1][1] = str(int(ingredientes[1][1]) - 80)
        ingredientes[1][2] = str(int(ingredientes[1][2]) - 800)
        print("S'ha produit 1l de llimonada casera")
        limonada = limonada + 1000

50*4+80+800






i = 1

while i == 1:
    print("\n1. Donar d'alta treballador.")
    print("2. Fer comanda d'ingredients.")
    print("3. Produir 1L de llimonada.")
    print("4. Vendre 250ml llimonada.")
    print("5. Veure el guany del lloc de llimonada.")
    print("6. Sortir.")

    x = int(input("\nEscoge una opcion: "))

    if x == 1:
        altaAdmin()
    if x == 2:
        comandaStock()
    if x == 3:
        produirLlimonada()

