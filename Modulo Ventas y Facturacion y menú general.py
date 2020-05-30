"""San Martin Jilotepeque, Chimaltenango 15/05/2020
Anderson Emmanuel López Hernández 
Facturación, venta y menú general"""

#FUNCION GENERAL PARA COMPROBAR EXISTENCIA DE ARCHIVOS NECESARIOS PARA EL FUNCIONAMIENTO DEL PROGRAMA
def checkFileExistance(filePath):
    #Comprobar existencia del archivo
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        #si no existe, se crea el archivo en blanco
        doc=open(filePath,"w", encoding="utf-8")

#FUNCION PERTENECIENTE AL MODULO FACTURACION    
def mostrarfacturas(filePath):
    #Comprobar existencia del archivo
    try:
        with open(filePath, 'r') as f:
            #si el archivo existe imprime el nombre del archivo
            print(filePath)
    except FileNotFoundError as e:
        return False       


    #se abre el listado de productos existentes en modo lecutra
    fin = open(filein, "r")
    for linea in fin:
        if slinea in linea:
            print(linea)
    fin.close()
x=0
listad=[]
lista=[]
listap=[]
while x!=6:
    print("MENU DE OPCIONES")
    print("1. Revisar inventario")
    print("2. Ingresar nuevo cliente")
    print("3. Realizar compra")
    print("4. Realizar venta")
    print("5. Facturar")
    x=int(input("Ingrese el codigo de la opcion a utilizar: "))
    if x==1:
        print("Nada todavía")
 
    else:
        if x==2:
            print("Por ahora nada")
        else:
            if x==3:
                print("Por ahora nada")
            else:
                if x==4:                 
                    continuar=1
                    while continuar!=2:
                        venta1=1
                        while venta1!=2:
                            #segun los codigos del inventario revisamos si existe el producto
                            venta=int(input("Ingrese el codigo del producto a vender: "))
                            venta=str(venta)+"."
                            with open("tienda.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Nombre:" in linea[1]) and (venta in linea[0]):
                                            #si existe guardamos el nombre, y cuantas unidades venderemos
                                            lista.append(linea[2])
                                            uniV=int(input("¿Cuantas unidades vendera? "))
                                            #ingresamos las unidades a una lista para usarlos en la factura
                                            listap.append(uniV)
                                            venta1=2
                            #recuperamos el valor de las unidades que ya existen
                            with open("tienda.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Unidades" in linea[1]) and (venta in linea[0]):
                                            unidadF=int(linea[2])
                            #recuperamos el precio del producto y lo guardamos en una lista
                            with open("tienda.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Precio" in linea[1]) and (venta in linea[0]):
                                            listad.append(linea[2])
                            #restamos las unidades vendidas
                            unidadN=unidadF-uniV
                            if unidadN<0:
                                print("no se pudo realizar la venta porque no queda stock")
                            else:
                                #realizamos la actualizacion del inventario
                                fin=open("tienda.txt","r")
                                fout=open("tiendaT.txt","w")
                                for linea in fin:
                                    if (venta+" Unidades") in linea:
                                        fout.write(venta+" Unidades"+": "+str(unidadN)+"\n")
                                    else:
                                        fout.write(linea)
                                fout.close()
                                fin.close()
                                fout=open("tiendaT.txt","r")
                                contenido=fout.read()
                                fout.close()
                                fin=open("tienda.txt","w")
                                fin.write(contenido)
                                fin.close()

                                print("¿desea cotninuar? presione 2 para salir")
                                continuar=int(input("Ingrese aqui: "))
                    print(lista)
                    print(listad)
                    print(listap)                          
                else:
                    if x==5:
                        print("FACTURACION")
                        print("1. Crear factura")
                        print("2. Revisar facturas existentes")
                        y=int(input("Ingrese el numero de la opcion a utilizar: "))
                        if y==1:
                            #revisa que exista un archivo donde se almacenarán los codigos
                            checkFileExistance("codigos_facturacion.txt")
                            cod=open("codigos_facturacion.txt","r+")
                            codigo=cod.readlines()
                            #obtiene el número de lineas
                            num=len(codigo)
                            #escribe en el txt el codigo
                            cod.write(str(num)+"\n")
                            codcli=int(input("Ingrese el codigo del cliente: "))
                            #revisa la existencia de un documento con ese codigo
                            checkFileExistance("Factura"+str(num)+".txt")
                            #incresa los datos a la factura que contenga ese codigo
                            factura=open("Factura"+str(num)+".txt","a")
                            factura.write("LOCAL DE VENTAS \n")
                            factura.write("FACTURA NO. "+str(num)+" \n")
                            factura.write("Productos: \n")
                            t=0
                            for x in range(len(lista)):
                                #realizamos la multiplicacion para obtener el total a pagar
                                pt=float(listad[x])*float(listap[x])
                                t=t+pt
                                #eviamos a la factura todos los datos necesarios
                                factura.write(lista[x]+": "+str(pt)+"\n")    
                            factura.write("SUBTOTAL: \n")
                            factura.write(str(t)+"\n")
                            factura.write("TOTAL: \n")
                            factura.write(str(t)+"\n")
                            factura.close()
                            listad=[]
                            lista=[]
                            listap=[]
                        else:
                            if y==2:
                                #extra el numero de lineas en el txt de codigos
                                lector=open("codigos_facturacion.txt","r")
                                lin=lector.readlines()
                                num=len(lin)
                                if num==0:
                                    #si no hay lineas, no hay facturas
                                    print("No existen facturas")
                                else:
                                    #usamos un for con rango igual al numero de lineas +1 y llamamos a la funcion mostrarfacturas
                                    for x in range(num+1):
                                        mostrarfacturas("Factura"+str(x)+".txt")
                                    buscar=int(input("Ingrse el numero de la factura que desea ver: "))
                                    #mostramos el contenido de la factura que pida el usuario
                                    abrir=open("Factura"+str(buscar)+".txt","r")
                                    contenido=abrir.read()
                                    print(contenido)

