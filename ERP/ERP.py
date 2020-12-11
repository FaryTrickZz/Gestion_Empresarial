import time

def mostrarUsuarios():
    f = open("Clientes", "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\nQWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm0123456789")
        line = line.rstrip("-")
        print(line)
    f.close()
    time.sleep(3)


def insertarUsuario(Cliente):
    f = open("Clientes", "a")
    contrasena = input("Introduce una contraseña: ")
    f.write("\n" + Cliente + "-" + contrasena)
    f.close()


def eliminarUsuario():
    f = open("Clientes", "r")
    lines = f.readlines()
    f.close()

    f = open("Clientes", "w")
    lin = 0
    aux = False
    while aux == False:
        admin = input("\nIntroduce el usuario admin para continuar: ")
        contrasena = input("Introduce la contraseña: ")
        mostrarUsuarios()
        time.sleep(1)
        usuario = input("\nEscribe el cliente a eliminar: ")
        if admin == "administrador" and contrasena == "1234":
            while lin < len(lines):
                line = lines[lin].rstrip("\nQWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm0123456789")
                line = line.rstrip("-")
                if line == usuario.rstrip("\n"):
                    print("Se ha eliminado el usuario: "+ usuario)
                    lin = lin + 1
                elif lines[lin] != usuario.rstrip("\n"):
                    f.write(lines[lin])
                    lin = lin + 1
                aux = True
    f.close()
    time.sleep(1)


def comprobarStock():
    f = open("ERP/Productos", "r")
    productos = f.readlines()
    f2 = open("ERP/Stock", "r")
    stock = f2.readlines()
    x = 0
    while x < len(productos):
        producto = productos[x].rstrip("0123456789\n")
        producto = producto.rstrip("-")
        producto = producto.lstrip("0123456789")
        print(producto+ ": "+stock[x])
        x= x+1



def añadirStock(idProducto):
    f = open("ERP/Productos", "r")
    productos = f.readlines()
    f.close()
    f = open("ERP/Stock", "r")
    stockProductos = f.readlines()
    for producto in productos:
        if producto.startswith(str(idProducto)):
            producto = producto.rstrip("0123456789\n")
            producto = producto.rstrip("-")
            producto = producto.lstrip("0123456789")
            print(producto)
            stockaanadir = input("Cuanto stock quieres añadir: ")
            stockActualProducto = stockProductos[idProducto - 1]
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
            f = open("Stock", "w")
            for stockProducto in stockProductos:
                f.write(str(stockProducto))
    f.close()


def verPrecioStock():
    f = open("Productos", "r")
    productos = f.readlines()
    f.close()
    f = open("Stock")
    stock = f.readlines()
    x = 0
    while x < len(productos):
        producto = productos[x].rstrip("0123456789\n")
        producto = producto.rstrip("-")
        producto = producto.lstrip("0123456789")
        precioProducto = productos[x].lstrip("QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm0123456789\n")
        precioProducto = precioProducto.lstrip("-")
        stockProducto = stock[x]
        precioStock = int(precioProducto)*int(stockProducto)
        print(producto + ": " + precioProducto + " --> Stock: " + stockProducto + " --> Precio del stock: " + str(precioStock) + "\n")
        time.sleep(1)
        x = x+1
    f.close()



def verIngresos():
    f = open("balance", "r")
    lines = f.readlines()
    print("Los ingresos actuales son: " + lines[0])
    time.sleep(2)



def venderProducto():
    # PIDE UN USUARIO Y CONTRASEÑA PARA VENDER UN PRODUCTO Y COMPRUEBA QUE SEA CORRECTO
    boolean = False
    while boolean != True:
        usuario = input("Para vender un producto indica un usuario: ")
        contrasena = input("                               contraseña: ")
        usuarioContrasena = usuario + "-" + contrasena
        f4 = open("Clientes", "r")
        clientes = f4.readlines()
        for cliente in clientes:
            if usuarioContrasena == cliente.rstrip("\n"):
                boolean = True

    idProducto = int(input("\nId del producto a vender: "))

    # ABRE Y LEE LOS ARCHIVOS DE PRODUCTOS, BALANCE Y CLIENTES FIDELIZADOS
    f2 = open("Productos", "r")
    f3 = open("balance", "r")
    f4 = open("ClientesFidelizados", "r")
    clientesFidelizados = f4.readlines()
    balance = f3.readlines()
    lines2 = f2.readlines()

    # CON LA FUNCION LSTRIP COGE EL PRECIO DEL PRODUCTO
    PrecioProducto = (lines2[idProducto - 1].lstrip("\n,0,1,2,3,4,5,6,7,8,9,Monitor, Cam, k"))
    PrecioProducto2 = PrecioProducto.lstrip("-")
    cantidad = input("Introduce la cantidad que quieres vender: ")
    PrecioFinal = int(PrecioProducto2) * int(cantidad)

    f3 = open("balance", "w")
    #  COMPRUEBA SI EL CLIENTES ESTA FIDELIZADO PARA HACER O NO EL DESCUENTO
    for clienteFidelizado in clientesFidelizados:

        if clienteFidelizado.rstrip("0123456789") == usuario:

            if clienteFidelizado.strip("QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm") == str(20):
                print("Bernat es un cliente fidelizado, recibirá un 20% de descuento")
                PrecioFinal = int(int(PrecioFinal)*80/100)
                Total = int(balance[0]) + int(PrecioFinal)

            else:
                print("Bernat es un cliente fidelizado, recibirá un 10% de descuento")
                PrecioFinal = int(int(PrecioFinal) * 80 / 100)
                Total = int(balance[0]) + int(PrecioFinal)


        else:
            Total = int(balance[0]) + int(PrecioFinal)

        f3.write(str(Total))
        f3.close()
        time.sleep(1)


    f5r = open("Historial", "r")
    historial = f5r.readlines()

    # Si el archivo historial esta vacio lo rellenara con el primer cliente
    if historial == []:
        f5w = open("Historial", "w")
        f5w.write(usuario + ": " + PrecioFinal)
        f5w.close()
    # En el caso que ya haya algun cliente registrado leera todos los clientes buscando el que hemos escrito
    else:
        x = 0
        for cliente in historial:
            # Si el cliente ya esta en el historial se sobreescribe su registro
            if cliente.strip(": 0123456789") == usuario:
                f5w = open("Historial", "w")
                historialCliente = cliente.strip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
                total = int(historialCliente) + PrecioFinal
                historial[x] = usuario + ": " + str(total)
                for cliente in historial:
                    f5w.write(cliente)
                f5w.close()
            # Si no existe en el registro lo añade con su primera compra
            else:
                f5w = open("Historial", "a")
                f5w.write("\n" + usuario + ": " + str(PrecioFinal))
                f5w.close()
            x = x + 1


    f2.close()
    eliminarStock(idProducto, cantidad)


def historialClientes():
    f = open("Historial", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
        time.sleep(1)


def mayorComprador():
    f = open("Historial", "r")
    lines = f.readlines()
    mayorComprador = 0
    clienteGanador = ""
    for line in lines:
        dineroGastado = line.lstrip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
        if int(dineroGastado) > int(mayorComprador):
            mayorComprador = dineroGastado
            clienteGanador = line.rstrip("\n: 0123456789")
    print("\nEl cliente que mas ha gastado ha sido: " + clienteGanador + " con: " + mayorComprador + "€")
    time.sleep(1)


def fidelizarCliente():

    f = open("Historial", "r")
    lines = f.readlines()
    print("Los clientes que se pueden fidelizar son:")
    dineroGastado = 0
    for line in lines:
        dineroGastado = line.lstrip(": QWERTYUIOPÑLKJHGFDSAZXCVBNMqwertyuiopñlkjhgfdsazxcvbnm")
        if int(dineroGastado) > 2000:
            print(line.rstrip("\n: 0123456789"))

    clienteFidelizado = input("\nIntroduce el cliente a fidelizar: ")
    f2 = open("ClientesFidelizados", "r")
    ClientesFidelizados = f2.readlines()
    # Si el fichero esta vacio fideliza al primer cliente
    if ClientesFidelizados == []:
        f2 = open("ClientesFidelizados", "w")
        if 1000 < int(dineroGastado) < 2000:
            f2.write(clienteFidelizado + "10")
        else:
            f2.write(clienteFidelizado + "20")
        f2.close()
    else:
        x = 0
        for cliente in ClientesFidelizados:
            # Si el cliente ya esta fidelizado no lo apunta
            if cliente.strip(": 0123456789") == clienteFidelizado:
                print("El cliente ya esta fidelizado")
            # Si el cliente no esta fidelizado lo apunta
            else:
                f2 = open("ClientesFidelizados", "a")
                if 10000 < int(dineroGastado) < 20000:
                    f2.write(clienteFidelizado + "10")
                else:
                    f2.write(clienteFidelizado + "20")
                f2.close()
            x = x + 1


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

        eliminarUsuario()
    if x == 4:
        print(comprobarStock())
    if x == 5:
        idProducto = int(input("\nEscribe el ID del producto que quieres aumentar el stock: "))
        añadirStock(idProducto)
    if x == 6:
        verPrecioStock()
    if x == 7:
        verIngresos()
    if x == 8:
        venderProducto()
    if x == 9:
        historialClientes()
    if x == 10:
        mayorComprador()
    if x == 11:
        fidelizarCliente()
    if x == 12:
        i = 2
