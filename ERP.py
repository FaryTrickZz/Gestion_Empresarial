
def mostrarUsuarios():
    f = open("Clientes", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

def insertarUsuario(Cliente):
    f = open("Clientes", "a")
    contraseña = input("Introduce una contraseña: ")
    f.write("\n"+Cliente+"-"+contraseña)
    f.close()

def eliminarUsuario(Cliente):
    f = open("Clientes", "r")
    lines = f.readlines()
    f.close()

    f = open("Clientes", "w")
    lin = 0
    aux = False
    while aux == False:
        usuario = input("\nIntroduce el usuario admin para continuar: ")
        contraseña = input("Introduce la contraseña: ")
        if usuario == "administrador" and contraseña == "1234":
            while lin < len(lines):
                if lines[lin] == Cliente + "\n":
                    print("Se ha encontrado un elemento a eliminar")
                    lin = lin+1
                elif lines[lin] != Cliente + "\n":
                    f.write(lines[lin])
                    lin = lin+1
                aux = True
                print("Se ha eliminado con exito el usuario.")
    f.close()

def comprobarStock():
    f = open("Productos", "r")
    lines = f.readlines()

    for line in lines:
        print(line.rstrip("1,2,3,4,"))
    f.close()


def añadirStock(idProducto):
    f = open("Productos", "r")
    productos = f.readlines()
    f.close()
    f = open("Stock", "r")
    stockProductos = f.readlines()
    i = 0
    for producto in productos:
            if producto.startswith(str(idProducto)):
                print(producto)
                stockaanadir  = input("Cuanto stock quieres añadir: ")
                stockActualProducto = stockProductos[idProducto-1]
                stockfinal = int(stockActualProducto) + int(stockaanadir)
                stockProductos[idProducto - 1] = str(stockfinal) + "\n"
                f = open("Stock", "w")
                for stockProducto in stockProductos:
                    f.write(str(stockProducto))
    f.close()

def eliminarStock(idProducto, cantidad):
    f = open("Productos", "r")
    productos = f.readlines()
    f.close()
    f = open("Stock", "r")
    stockProductos = f.readlines()
    i = 0
    for producto in productos:
        if producto.startswith(str(idProducto)):
            stockaeliminar = cantidad
            stockActualProducto = stockProductos[idProducto - 1]
            stockfinal = int(stockActualProducto) - int(stockaeliminar)
            stockProductos[idProducto - 1] = str(stockfinal) + "\n"
            stockProductos
            f = open("Stock", "w")
            for stockProducto in stockProductos:
                f.write(str(stockProducto))
    f.close()

def verPrecioStock(idProducto):
    fr = open("Stock", "r")
    f = open("Productos", "r")
    lines = fr.readlines()
    lines2 = f.readlines()
    Producto = ([idProducto - 1].rstrip("\n,0,1,2,3,4,5,6,7,8,9"))
    Stock = (lines[idProducto-1])
    PrecioStock = (lines2[idProducto - 1].lstrip("\n,0,1,2,3,4,5,6,7,8,9,Monitor, Cam, k"))
    PrecioStock2 = PrecioStock.lstrip("-")
    PrecioTotal = int(Stock)*int(PrecioStock2)
    print(Producto + "\nStock: "+ Stock +"Precio unitario: "+PrecioStock2+"Precio Total: "+str(PrecioTotal))
    f.close()
    fr.close()

def verIngresos():
    f = open("balance", "r")
    lines = f.readLines
    for line in lines:
        print(line)

def venderProducto(idProducto):
    # PIDE UN USUARIO Y CONTRASEÑA PARA VENDER UN PRODUCTO Y COMPRUEBA QUE SEA CORRECTO
    boolean = False
    while boolean != True:
        usuario = input("Para vender un producto indica un usuario: ")
        contraseña = input("                               contraseña: ")
        usuarioContraseña = usuario+"-"+contraseña+"\n"
        f4 = open("Clientes", "r")
        clientes = f4.readlines()
        for cliente in clientes:
            if usuarioContraseña == cliente:
                boolean = True

    cantidad = input("Introduce la cantidad que quieres vender: ")

    # ABRE Y LEE LOS ARCHIVOS DE PRODUCTOS Y BALANCE
    f2 = open("Productos", "r")
    f3 = open("balance", "r")
    balance = f3.readlines()
    lines2 = f2.readlines()

    # CON LA FUNCION LSTRIP COGE EL PRECIO DEL PRODUCTO
    PrecioProducto = (lines2[idProducto - 1].lstrip("\n,0,1,2,3,4,5,6,7,8,9,Monitor, Cam, k"))
    PrecioProducto2 = PrecioProducto.lstrip("-")

    Beneficio = int(PrecioProducto2) * int(cantidad)
    Total = int(balance[0])+int(Beneficio)
    f3 = open("balance", "w")
    f5r = open("Historial", "r")
    historial = f5r.readlines()

    # Si el archivo historial esta vacio lo rellenara con el primer cliente
    if historial == []:
        f5w = open("Historial", "w")
        f5w.write(usuario+": "+Beneficio)
        f5w.close()
    # En el caso que ya haya algun cliente registrado leera todos los clientes buscando el que hemos escrito
    else:
        x = 0
        for cliente in historial:
            # Si el cliente ya esta en el histrial se sobreescribe su registro
            if cliente.strip(": 0123456789") == usuario:
                f5w = open("Historial", "w")
                historialCliente = cliente.strip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
                total = int(historialCliente)+Beneficio
                historial[x] = usuario+": "+str(total)
                for cliente in historial:
                    f5w.write(cliente)
                f5w.close()
            # Si no existe en el registro lo añade con su primera compra
            else:
                f5w = open("Historial", "a")
                f5w.write("\n"+usuario+ ": " +str(Beneficio))
                f5w.close()
            x = x+1


    f3.write(str(Total))
    f3.close()
    f2.close()
    eliminarStock(idProducto, cantidad)

def historialClientes():
    f = open("Historial", "r")
    lines = f.readlines()
    for line in lines:
        print(line)

def mayorComprador():
    f = open("Historial", "r")
    lines = f.readlines()
    mayorComprador = 0
    clienteGanador = ""
    for line in lines:
        dineroGastado = line.lstrip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
        if int(dineroGastado) > int(mayorComprador):
            mayorComprador = dineroGastado
            clienteGanador = line.rstrip(": 0123456789")
    print("\nEl cliente que mas ha gastado ha sido: "+clienteGanador+" con: "+mayorComprador+"€")

def fidelizarCliente():
    f = open("Historial", "r")
    lines = f.readlines()

    for line in lines:
        dineroGastado = line.lstrip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
        if int(dineroGastado) > 2000:
            print(line.strip(": 0123456789"))




i = 1

while i == 1:
    print("\n1. Mostrar la lista de usuarios.")
    print("2. Insertar nuevo usuario.")
    print("3. Eliminar usuario con un nombre en concreto.")
    print("4. Consultar stock.")
    print("5. Aumentar stock.")
    print("6. Ver precio del stock.")
    print("7. Ver Ingresos.")
    print("8. Vender producto.")
    print("9. Mostrar historial de clientes.")
    print("10. Mostrar cliente que mas ha gastado.")
    print("11. Fidelizar cliente.")
    print("12. Salir.")
    x = int(input("\nEscoge una opcion: "))


    if x == 1:
        mostrarUsuarios()
    if x == 2:
        usuario = input("\nEscribe el nombre del nuevo cliente: ")
        insertarUsuario(usuario)
    if x == 3:
        usuario = input("\nEscribe el cliente a eliminar: ")
        eliminarUsuario(usuario)
    if x == 4:
        print(comprobarStock())
    if x == 5:
        idProducto = int(input("\nEscribe el ID del producto que quieres aumentar el stock: "))
        añadirStock(idProducto)
    if x == 6:
        idProducto = int(input("\nEscribe el ID del producto que quieres ver su stock: "))
        verPrecioStock(idProducto)
        print()

    if x == 7:
        verIngresos()

    if x == 8:
        idProducto = int(input("\nId del producto a vender: "))
        venderProducto(idProducto)

    if x == 9:
        historialClientes()

    if x == 10:
        mayorComprador()

    if x == 11:
        fidelizarCliente()

    if x == 12:
        i = 2