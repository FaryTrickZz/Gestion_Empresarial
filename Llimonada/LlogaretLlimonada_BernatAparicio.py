import time

#Variables y arrays para tratar el programa
adminUsers = []
ingredientes = [["Llimona/u","Sucre/g","Agua/ml"],["20","1000","10000"]]
limonada = 0
dinero = 0

#Pide un usuario y contraseña y lo inserta en el array de usuarios
def altaAdmin():
    usuario = input("Introdueix el nom d'usuari: ")
    passwd = input("Introdueix una contrasenya: ")
    adminUsers.append(usuario+"/"+passwd)
    print("L'usuari s'ha creat correctament")
    time.sleep(1)

#Muestra el stock actual y mediante un input insertas la cantidad de cada producto deseado
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

#Segun la cantidad de ingredientes te avisa de que se estan acabando los ingredientes, si no hay algun ingrediente suficiente no te permite
#producir limonada.
def produirLlimonada(limonada):
    #Depende de la cantidad de ingredientes que haya se muestra un mensaje para hacer una comanda de stock o no hacerla
    if (int(ingredientes[1][0])<12 or int(ingredientes[1][1])<240 or int(ingredientes[1][2])<2400):
        print("Els ingredients per produir llimonada s'setan acabant, conve fer una comanda")

    if (int(ingredientes[1][0])<4):
        print("No hi ha llimones suficients per produir llimonada")

    elif(int(ingredientes[1][1]) < 240):
        print("No hi ha sucre suficient per produir llimonada")

    elif(int(ingredientes[1][2])<2400):
        print("No hi ha aigua suficient per produir llimonada")

    else:
        # Formula de la limonada 50*4+80+800
        ingredientes[1][0] = str(int(ingredientes[1][0]) - 4)
        ingredientes[1][1] = str(int(ingredientes[1][1]) - 80)
        ingredientes[1][2] = str(int(ingredientes[1][2]) - 800)
        print("S'ha produit 1l de llimonada casera")
        limonada = limonada + 1000
        return limonada

#Vende limonada, resta 250ml a la cantidad total de limonada
def vendrellimonada(limonada):
    limonada = limonada - 250
    return limonada

#Cuando vendes limonada se suma 1€ a la cantidad total de ganancias
def augmentarDiners(dinero):
    dinero = dinero + 1
    return dinero

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
        if adminUsers:
            comandaStock()
    if x == 3:
        if adminUsers:
            limonada = produirLlimonada(limonada)
    if x == 4:
        if adminUsers:
            limonada = vendrellimonada(limonada)
            dinero = augmentarDiners(dinero)
    if x == 5:
        if adminUsers:
            print("Els ingresos son: "+dinero)



