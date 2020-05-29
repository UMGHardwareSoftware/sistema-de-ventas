"""San Martin Jilotepeque, Chimaltenango 27/05/2020
Equipo de Trabajo
Proyecto final"""

#GENERALIDADES DE USO 1:
#PARA REALIZAR VENTAS PRIMERO SE DEBE ENTRAR A LA OPCION VENTAS Y AL TERMINAR ELEGIR LA OPCION FACTURACION PARA
#REALIZAR LA FACTURA. SI EL PROGRAMA SE CIERRA ANTES DE REALIZAR LA FACTURA, SE PERDERÁ LA COMPRA 
#GENERALIDADES DE USO 2:
#CUALQUIER DATO INGRESADO DEBERÁ USAR GUIONES BAJOS (_) O NORMALES (-) PARA SEPARAR PALABRAS.
#GENERALIDADES DE USO 3:
#LOS CÓDIGOS DE LOS PRODUCTOS SE CREARAN DE MANERA AUTOMATICA. POR FAVOR APUNTAR DICHOS CODIGOS EN EL PRODUCTO
#REAL PARA LLEVAR UN MEJOR CONTROL A LA HORA DE VENDER

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

#FUNCION PERTENECIENTE AL MODULO COMPRAS
def nuevasunidadesCompra(filein, fileout, slinea, dagre, deli, auni):
    #abrimos el doc de productos en modo lectura
    fin = open(filein, "r")
    #abrimos un segundo doc en blanco
    fout = open(fileout, "w")
    #calculamos el total de las nuevas unidades
    total=int(dagre)+int(auni)
    #copiamos el doc de productos al doc en blanco y cambiamos la linea de unidades por la nueva linea con las nuevas unidades
    for linea in fin:
        if slinea in linea:
            fout.write(slinea+": "+str(total)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #regresamos el contenido que quedó en el doc en blanco al doc productos
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()

#FUNCION PERTENECIENTE AL MODULO INVENTARIO
def deleteline(filein, fileout, slinea, fileinP, fileoutP):
    #se abre el archivo de productos y el listado de prodcutos en modo lectura
    fin = open(filein, "r")
    finp=open(fileinP, "r")
    #se abren dos archivos en blanco
    fout = open(fileout, "w")
    foutp=open(fileoutP,"w")
    #se abre el archivo stock
    with open("stock.txt") as archivo: 
        for texto in archivo.readlines():
            linea=texto.split()
            if len(linea)>1:
                #si el codigo del producto no esta en la linea, se copia normalmente al archivo 
                if not (slinea in linea[0]):
                    fout.write(texto)
            #si número de columnas = 1, copia normal al archivo, evita que se eliminen los separadores
            if len(linea)==1:
                fout.write(texto)
    #hacemos lo mismo con el listado de productos           
    for lineap in finp: 
        if not slinea in lineap:
            foutp.write(lineap)          
    fout.close()
    foutp.close()
    fin.close()
    finp.close()
    #Regresamos el contenido que quedó en los docs en blanco al doc de productos y al listado de productos
    fout = open(fileout,"r") 
    contenido=fout.read()
    fout.close()
    fin=open(filein,"w") 
    fin.write(contenido)
    fin.close()
    foutp=open(fileoutP,"r") 
    contenido=foutp.read()
    foutp.close()
    finp=open(fileinP,"w")
    finp.write(contenido)
    finp.close()

#FUNCION PERTENECIENTE AL MODULO INVENTARIO
def modifline(filein, fileout, slinea, dagre, dmod, deli):
    fin = open(filein, "r") #se abren dos archivos, modo lectura para stock y otro vacío
    fout = open(fileout, "w")
    #si se modifica el nombre, también se modifica el listado de productos 
    if dmod=="Nombre":
        #se abre el archivo de productos
        finp=open("productos.txt","r")
        foutp=open("op_stock.txt","w")
        #se busca el código del producto que se va a modificar
        for lineap in finp:
            #se pasaran los datos del archivo leído al archivo vacío
            if deli in lineap:
                #si encuentra el codigo en el archivo leído, la línea se cambia por una que tenga el nuevo nombre
                foutp.write(deli+". "+str(dagre)+"\n")
            else:
                foutp.write(lineap)
        foutp.close()
        finp.close()
        #se abre archivo nuevo y se recupera el contenido
        foutp=open("op_stock.txt","r") 
        contenido=foutp.read()
        foutp.close()
        #se abre el archivo original en modo vacío y se agrega el contenido
        finp=open("productos.txt","w")
        finp.write(contenido)
        finp.close()
    #si se cambia otro campo que no sea nombre, se busca el código y el campo del producto
    for linea in fin: 
        #se envian datos de un archivo a otro
        if slinea in linea:
            fout.write(slinea+": "+str(dagre)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #se abre el archivo en blanco que usamos al principio en modo lectura y recuperaremos el contenido
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #se abre el archivo de productos original vacio y se ingresa el cotenido.
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()

#FUNCION PERTENECIENTE AL MODULO INVENTARIO Y CLIENTES
def getprod(filein, slinea):
    #se abre el listado de productos existentes en modo lectura
    fin = open(filein, "r")
    #mostramos aquello que contenga la variable slinea
    for linea in fin:
        if slinea in linea:
            print(linea)
    fin.close()

#FUNCION PERTENECIENTE AL MODULO CLIENTES
def deletelineC(filein, fileout, slinea, fileinP, fileoutP):
    #abrimos un archivo x en modo lectura, y uno Y vacio
    fin = open(filein, "r")
    finp=open(fileinP, "r")
    fout = open(fileout, "w")
    foutp=open(fileoutP,"w")
    #abrimos el documento X y separamos sus elementos en columna
    with open("tiendaClientes.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            #si la linea leida tiene más de 1 columna
            if len(linea)>1:
                #comprueba si el codigo del cliente esta en la primera columna y si no esta, copia la linea al doc Y normal
                if not (slinea in linea[0]):
                    fout.write(texto)
            #si el numero de columnas es 1 entonces la copia normal al doc Y (esto sería para evitar que se borren los separadores)
            if len(linea)==1:
                fout.write(texto)
    #realizamos la misma lectura de lineas en el documento de listado de clientes          
    for lineap in finp:
        #si el codigo del cliente no esta en la linea, se copia normalmente al documento Y
        if not slinea in lineap:
            foutp.write(lineap)          
    fout.close()
    foutp.close()
    fin.close()
    finp.close()
    #abrimos el documento Y y recuperamos su contenido
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #abrimos el documento X vacio e ingresamos el contenido del documento Y
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()
    #realizamos la misma operacion con el documento X y Y del listado de clientes.
    foutp=open(fileoutP,"r")
    contenido=foutp.read()
    foutp.close()
    finp=open(fileinP,"w")
    finp.write(contenido)
    finp.close()

#FUNCION PERTENECIENTE AL MODULO CLIENTES
def modiflineC(filein, fileout, slinea, dagre, dmod, deli):
    #abrimos 2 documentos, uno en modo lectura (tiendaClientes) y 1 vacio
    fin = open(filein, "r")
    fout = open(fileout, "w")
    #En caso de querer modificar el nombre, también habría que modificarse el listado de clientes
    if dmod=="Nombre":
        #abrimos el documento de clientes
        finp=open("clientes.txt","r")
        foutp=open("clientesT.txt","w")
        #buscamos el codigo del cliente que se va a cambiar
        for lineap in finp:
            #se iran pasando los datos del documento leido al documento vacio
            if deli in lineap:
                #si se encuentra el codigo en el documento leido, esta linea se cambia por una que contenga el nuevo nombre
                foutp.write(deli+". "+str(dagre)+"\n")
            else:
                foutp.write(lineap)
        foutp.close()
        finp.close()
        #abrimos el documento nuevo en modo lectura y recuperamos su contenido
        foutp=open("clientesT.txt","r")
        contenido=foutp.read()
        foutp.close()
        #abrimos el documento original de clientes ahora en modo vacio y agregamos el contenido anteriormente copiado
        finp=open("clientes.txt","w")
        finp.write(contenido)
        finp.close()
    #En caso de querer cambiar cualquier campo que no sea nombre
    #buscamos el codigo y campo del producto (Lo que se envia desde el programa principal es "Codigo. Campo:")
    for linea in fin:
        #empezaremos a enviar los datos de de un documento X a uno Y
        if slinea in linea:
            #si encontramos el codigo y el campo, el documento Y recibirá una linea distinta al documento X
            fout.write(slinea+": "+str(dagre)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #abriremos el documento Y en modo lectura y recuperaremos el contenido
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #abriremos el documento X vacio e ingresaremos los contenidos del documento Y
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()
x=0
#DICCIONARIO PARA EVITAR QUE LOS USUARIOS INGRESEN LETRAS EN LAS OPCIONES
dic=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".",",","ñ","/","*","-","+"]
#LISTAS USADAS PARA REALIZAR LAS VENTAS
listad=[]
lista=[]
listap=[]
#MENU GENERAL
while x!=6:
    print("***MENU DE OPCIONES***")
    print("<--------------------------------->")
    print("1. Revisar inventario")
    print("2. Ingresar nuevo cliente")
    print("3. Realizar compra")
    print("4. Realizar venta")
    print("5. Facturar")
    print("6. Salir")
    print("<--------------------------------->")
    a=input("Ingrese el codigo de la opcion a utilizar: ")
    #USAMOS UN CONTADOR PARA SABER SI SE INGRESARON LETRAS EN VEZ DE NUMEROS
    contador=-1    
    while contador!=0:
        #REVISAREMOS SI ALGUNA LETRA DEL DICCIONARIO SE ENCUENTRA EN LO QUE EL USUARIO INGRESÓ
        for g in range(len(dic)):
            if dic[g] in a:
                #SI SE ENCUENTRA UNA DE LAS LETRAS, EL CONTADOR AUMENTA
                contador=contador+1
        if contador!=0:
            #SI EL CONTADOR NO ES 0 (ES DECIR, SI HAY LETRAS O SIGNOS) EL USUARIO INGRESA DE NUEVO UN VALOR
            a=input("Ingrese el codigo de la opcion a utilizar: ")
            #SI EL VALOR QUE INGRESA EL USUARIO ES UN NUMERO EQUIVALENTE A UNA OPCION, EL CONTADOR SE VUELVE 0
            if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6":
                contador=0
    #CON EL CONTADOR EN 0, EL VALOR INGRESADO POR EL USUARIO SE CONVIERTE EN INT PARA USARLO
    x=int(a)
    if x==1:
        """----------------------------------MODULO INVENTARIO---------------------------------"""
        codinventario=0
        #USAMOS LA FUNCION CHECKFILEEXISTENCE PARA CREAR LOS DOCUMENTOS NECESARIOS SI ES QUE NO EXISTEN Y ASI EVITAR ERRORES
        checkFileExistance("stock.txt")
        checkFileExistance("productos.txt")
        checkFileExistance("op_tienda.txt")
        checkFileExistance("op_productos.txt")
        checkFileExistance("tienda.txt")
        #MENU GENERAL DEL INVENTARIO
        while codinventario!=5:
            print("***CONTROL DE INVENTARIO***")
            print("<--------------------------------->")
            print("1. Ver stock de productos")
            print("2. Editar producto")
            print("3. Elimninar producto")
            print("4. Buscar")
            print("5. Regresar")
            print("<--------------------------------->")
            strcodinventario=input("Ingrese la opcion que desea utilizar: ")
            contador=-1
            #SE REALIZA EL MISMO PROCESO QUE EN EL MENU GENERAL PARA QUE EL USUARIO NO INGRESE LETRAS    
            while contador!=0:
                for g in range(len(dic)):
                    if dic[g] in strcodinventario:
                        contador=contador+1
                if contador!=0:
                    strcodinventario=input("Ingrese la opcion que desea utilizar: ")
                if strcodinventario=="1" or strcodinventario=="2" or strcodinventario=="3" or strcodinventario=="4" or strcodinventario=="5":
                    contador=0
            codinventario=int(strcodinventario)
            if codinventario==1:
                #MOSTRAMOS LOS PRODUCTOS GUARDADOS EN EL DOCUMENTO STOCK
                doc=open("stock.txt","r")
                contenido=doc.read()
                print(contenido)
                doc.close()
            else:
                if codinventario==2:
                    #EDITAR PRODUCTOS
                    #Se abre el archivo con el listado de productos y mostramos su contenido
                    doc2=open("productos.txt","r")
                    contenido=doc2.read()
                    print(contenido)
                    #el programa solicita el código del producto que se va editar
                    eli=input("Ingrese el codigo del producto que desea editar: ")
                    #se muestran los campos posibles para editar
                    getprod("stock.txt",(eli+"."))
                    #el programa solicita el nombre del campo que se va editar
                    mod=input("Escriba el nombre del campo que va a editar, el programa distingue mayúsculas y minúsculas: ")
                    #se deja la variable en -1 para que funcione
                    agre=-1
                    #si se edita el precio 
                    if mod=="Precio":
                        #se comprueba que el valor ingresado no sea negativo
                        while float(agre)<0 or int(agre)<0:
                            agre=input("Ingrese el nuevo dato que va a mostrar: ")
                            if float(agre)<0 or int(agre)<0:
                                print("Valor no valido")
                    #si se editan las unidades, no se permiten números negativos tampoco
                    if mod=="Unidades":
                        while int(agre)<0:
                            agre=input("Ingrese el nuevo dato que va a mostrar: ")
                            if int(agre)<0:
                                print("Valor no valido")
                    #si se edita cualquier otra cosa, el programa acepta cualquier cosa          
                    else:
                        agre=input("Ingrese el nuevo dato que va a mostrar: ")
                    #enviamos los datos obtenidos a la funcion modificar linea    
                    modifline("stock.txt","op_tienda.txt",(eli+". "+mod),agre, mod, eli)
                else:
                    if codinventario==3:
                        #eliminar producto
                        #se lee el contenido del archivo productos y lo mostraremos
                        doc2=open("productos.txt","r")
                        contenido=doc2.read()
                        print(contenido)
                        eli=input("Ingrese el codigo del producto que desea eliminar: ")
                        #enviamos los datos necesarios a la funcion eliminar linea
                        deleteline("stock.txt","op_tienda.txt",(eli+"."),"productos.txt","op_stock.txt")
                    else:
                        if codinventario==4:
                            #buscar productos
                            codbusqueda=0
                            while codbusqueda!=3:
                                #menu de busqueda
                                print("<--------------------------------->")
                                print("***MENU DE BUSQUEDAS***")
                                print("1. Busqueda por nombre")
                                print("2. Busqueda por fabricante")
                                print("3. Salir")
                                print("<--------------------------------->")
                                strcodbusqueda=input("Ingrese la opcion que desea usar: ")
                                #de la misma forma que en menus anteriores, evitamos que el usuario ingrese letras
                                contador=-1    
                                while contador!=0:
                                    for g in range(len(dic)):
                                        if dic[g] in strcodbusqueda:
                                            contador=contador+1
                                    if contador!=0:
                                        strcodbusqueda=input("Ingrese la opcion que desea usar: ")
                                    if strcodbusqueda=="1" or strcodbusqueda=="2" or strcodbusqueda=="3":
                                        contador=0
                                codbusqueda=int(strcodbusqueda)
                                if codbusqueda==1:
                                    nombrebuscar=input("Ingrese una palabra clave para buscar: ")
                                    #se abre el txt de productos y se muestran aquellos que contengan la palabra
                                    #ingresada por el usuario
                                    buscador=open("productos.txt","r")
                                    print("Se encontraron los siguientes productos: ")
                                    for linea in buscador.readlines():
                                        if nombrebuscar in linea:
                                            print(linea)
                                    buscador.close()
                                else:
                                    if codbusqueda==2:
                                        #busqueda por fabricante
                                        #dentro de una lista se guardaran los codigos de los productos que 
                                        #cumplan con lo ingresado por el usuario 
                                        listafabricante=[]
                                        fabricantebuscar=input("Ingrese el nombre del fabricante: ")
                                        buscador=open("stock.txt","r")
                                        print("Se encontraron los siguientes productos: ")
                                        #dentro del archivo stock buscaremos todos los codigos de productos cuyo
                                        #fabricante sea el ingresado por el usuario
                                        for linea in buscador.readlines():
                                            texto=linea.split()
                                            if len(texto)>1:
                                                if ("Fabricante" in texto[1] and fabricantebuscar in texto[2]):
                                                    #si encuentra al fabricante, agreamos el codigo a la lista
                                                    listafabricante.append(texto[0])
                                        buscador.close()
                                        #revisamos la lista, y buscamos dentro del archivo stock los codigos
                                        for h in range(len(listafabricante)):
                                            buscador=open("stock.txt","r")
                                            for fabricantes in buscador.readlines():
                                                texto=fabricantes.split()
                                                if len(texto)>1:
                                                    #al encontrar el codigo, muestra los datos del producto encontrado
                                                    if str(listafabricante[h]) in texto[0]:
                                                        print(fabricantes)
                                            print("*********************")

                        """----------------------------------FINAL MODULO INVENTARIO-----------------------------------"""
    else:
        if x==2:
            """----------------------------------MODULO CLIENTES-----------------------------------"""          
            #igualaremos a 0 la variable del while general
            codclientes=0
            #igualaremos a -1 las variables de los campos para que las condicionales surtan efecto
            telefono=-1
            #comprobamos la existencia de los archivos necesarios para el funcionamiento del programa
            checkFileExistance("clientes.txt")
            checkFileExistance("clientesF.txt")
            checkFileExistance("tiendaClientes.txt")
            checkFileExistance("clientesT.txt")
            checkFileExistance("tiendaClientesT.txt")
            #Creamos el menu principal
            while codclientes!=5:
                print("***CONTROL DE CLIENTES***")
                print("<--------------------------------->")
                print("1. Ingreso de Nuevos Clientes") 
                print("2. Muestra de los clientes existentes")
                print("3. Modificacion de clientes")
                print("4. Elimninacion de clientes")
                print("5. Salir")
                print("<--------------------------------->")
                strcodclientes=input("Ingrese la opcion que desea utilizar: ")
                #de la misma forma que antes comprobamos que el usuario no ingrese letras
                contador=-1    
                while contador!=0:
                    for g in range(len(dic)):
                        if dic[g] in strcodclientes:
                            contador=contador+1
                    if contador!=0:
                        strcodclientes=input("Ingrese la opcion que desea utilizar: ")
                    if strcodclientes=="1" or strcodclientes=="2" or strcodclientes=="3" or strcodclientes=="4" or strcodclientes=="5":
                        contador=0
                codclientes=int(strcodclientes)
                if codclientes==1:
                    #comenzamos abriendo el documento de la tiendaClientes
                    doc=open("tiendaClientes.txt","a")
                    #comenzamosa ingresar los datos
                    nombre=input("Ingrese el nombre completo del cliente: ")
                    fecha=input("Ingrese la Fecha de Nacimiento: ")
                    dpi=input("Ingrese su CUI: ")
                    direccion=input("Ingrese su direccion: ")
                    while telefono<0:
                        telefono=int(input("Ingrese su número de telefono: "))
                        if telefono<0:
                            print("Valor NO Valido")
                    nit=input("Ingrese su no. de NIT: ")
                    #enviamos un separador al documento de texto
                    doc.write("************************** \n")
                    #abrimos el documento que contendrá el listado de clientes y leemos sus lineas
                    doc2=open("clientes.txt","r")
                    lineas=doc2.readlines()
                    doc2.close()
                    #abrimos el doc que contendrá los codigos utilizados hasta ahora y leeremos sus lineas
                    doc3=open("clientesF.txt","r")
                    lineas=doc3.readlines()
                    doc3.close()
                    #abriremos el doc de codigos y el listado de clientes en modo escritura
                    doc3=open("clientesF.txt","a")
                    doc2=open("clientes.txt","a")
                    #enviaremos al doc de clientes y al de codigos una linea conteniendo el nombre y un codigo equivalente al numero de lineas en el doc de codigos
                    doc3.write(str(len(lineas))+". "+nombre+"\n")
                    doc2.write(str(len(lineas))+". "+nombre+"\n")
                    doc3.close()
                    doc2.close()
                    #enviaremos al doc que contendrá todos los datos los datos de los clientes junto con el codigo anterior obtenido
                    doc.write(str(len(lineas))+". Datos del cliente: \n")
                    doc.write(str(len(lineas))+ ". Nombre: "+ nombre + "\n")
                    doc.write(str(len(lineas))+". Fecha: "+ fecha + "\n")
                    doc.write(str(len(lineas))+". CUI: " + str(dpi) + "\n")
                    doc.write(str(len(lineas))+". Dirección: " + direccion +"\n" )
                    doc.write(str(len(lineas))+". Telefono: " + str(telefono) + "\n")
                    doc.write(str(len(lineas))+". NIT: "+str(nit) + "\n")
                    doc.close()
                    #regresamos el valor de del telefono a -1 para evitar errores al volver a ingresar productos
                    telefono=-1
                    print("Datos guardados con éxito")
                else:
                    if codclientes==2:
                        #abriremos el doc tiendaClientes, leeremos su contenido y lo mostraremos
                        doc=open("tiendaClientes.txt","r")
                        contenido=doc.read()
                        print(contenido)
                        doc.close()
                    else:
                        if codclientes==3:
                            #EDITAR DATOS
                            #Abriremos el doc con el listado de productos y mostraremos su contenido
                            doc2=open("clientes.txt","r")
                            contenido=doc2.read()
                            print(contenido)
                            #ingresaremos el codigo del cliente que se va a cambiar
                            eli=input("Ingrese el codigo del cliente que desea cambiar")
                            #mostraremos los campos existentes del cliente usando la funcion getprod
                            getprod("tiendaClientes.txt",(eli+"."))
                            #ingresaremos a la varibale mod (modificacion) el nombre del campo que se va a editar
                            mod=input("Ingrese el nombre del campo que desea editar (distingue entre minusculas y mayusculas, ej: Nombre): ")
                            agre=input("Ingrese el dato que desea colocar: ")
                            #enviamos los documentos que se van a editar 
                            #junto con el codigo y campo a editar juntos en una variable
                            #y tambiénel codigo y campo separados a la funcion modificar linea
                            modiflineC("tiendaClientes.txt","tiendaClientesT.txt",(eli+". "+mod),agre, mod, eli)
                        else:
                            if codclientes==4:
                                #leeremos el contenido de clientes y lo mostraremos
                                doc2=open("clientes.txt","r")
                                contenido=doc2.read()
                                print(contenido) 
                                eli=input("Ingrese el codigo del cliente que desea eliminar: ")
                                #enviaremos a la funcion eliminar los documentos que van a cambiar y el codigo del cliente a eliminar
                                deletelineC("tiendaClientes.txt","tiendaClientesT.txt",(eli+"."),"clientes.txt","clientesT.txt") 
                                """----------------------------------FINAL MODULO CLIENTES-----------------------------------"""
        else:
            if x==3:
                """----------------------------------MODULO COMPRAS-----------------------------------"""
                #dejamos en 0 el codigo del menu
                codcompra=0
                #y en -1 las variables de los campos
                unidades=-1
                precio=-1
                #comprobamos la existencia de los documentos necesarios
                checkFileExistance("stock.txt")
                checkFileExistance("productos.txt")
                checkFileExistance("op_productos.txt")
                checkFileExistance("tienda.txt")
                while codcompra!=3:
                    print("***MENU DE COMPRAS***")
                    print("<--------------------------------->")
                    print("1. Ingreso de Productos")
                    print("2. Añadir Stock")
                    print("3. Salir")
                    print("<--------------------------------->")
                    strcodcompra=input("Ingrese la opcion que desea usar: ")
                    #de la misma forma que en menus pasados, se evita que el usuario ingrese letras
                    contador=-1    
                    while contador!=0:
                        for g in range(len(dic)):
                            if dic[g] in strcodcompra:
                                contador=contador+1
                        if contador!=0:
                            strcodcompra=input("Ingrese la opcion que desea usar: ")
                        if strcodcompra=="1" or strcodcompra=="2" or strcodcompra=="3":
                            contador=0
                    codcompra=int(strcodcompra)

                    if codcompra==1:
                        doc1=open("stock.txt","a")
                        #ingresamos los datos del producto
                        nombre=input("Ingrese el Nombre del Producto: ")
                        while unidades<0:
                            print("Ingrese la cantidad de unidades")
                            unidades=input("Si ingresa numeros negativos o letras, deberá volver a ingresar el dato: ")
                            #Se comprueba que lo ingresado no sea letras o numeros negativos      
                            try:
                                #si es posible convertir el valor en INT, comprueba que no sea negativo
                                with int(unidades) as f:
                                    if unidades<0:
                                        print("Valor NO Válido")
                            #si no es posible convertirlo, vuelvea pedir el valor
                            except ValueError as e:
                                print("Valor NO Valido")
                                unidades=-1
                            #si se ingresó un numero desde el principio, lo guarda
                            except AttributeError as f:
                                unidades=int(unidades)

                        while precio<0:
                            print("Ingrese el precio")
                            precio=input("Evite ingresar numeros negativos o letras o deberá ingresar de nuevo un valor: ")
                            #realiza el mismo procedimiento que en las unidades para que el usuario no ingrese letras
                            #ni numeros negativos
                            try:
                                with float(precio) as f:
                                    if float<0:
                                        print("Valor NO Válido")
                            except ValueError as e:
                                print("Valor NO Valido")
                                precio=-1
                            except AttributeError as f:
                                precio=float(precio)
                        fabricante=input("Ingrese el nombre del fabricante: ")
                        print("Ingrese especificaciones que crea convenientes")
                        especif=input("Separe cada palabra con un _ por favor: ")
                        #Hacemos lo mismo que con los clientes y hacemos un txt con el codigo que se va a utilizar
                        doc3=open("tienda.txt","r")
                        lineas=doc3.readlines()
                        doc3.close()
                        doc2=open("productos.txt","a")
                        doc3=open("tienda.txt","a")
                        doc2.write(str(len(lineas))+ "."+nombre+"\n")
                        doc3.write(str(len(lineas))+ "."+nombre+"\n")
                        doc3.close()
                        doc2.close()
                        #enviamos los campos
                        doc1.write("++++++++++++++++++++++++++++++++++++++++++++ \n")
                        doc1.write(str(len(lineas))+ ". Nombre: "+ nombre + "\n")
                        doc1.write(str(len(lineas))+ ". Unidades: "+ str(unidades) + "\n")
                        doc1.write(str(len(lineas))+ ". Precio: "+ str(precio) + "\n") 
                        doc1.write(str(len(lineas))+ ". Especificaciones: "+ str(especif) + "\n")   
                        doc1.write(str(len(lineas))+ ". Fabricante: "+str(fabricante)+ "\n")
                        doc1.close()
                        unidades=-1
                        precio=-1
                        print("Datos Guardado con éxito!")
                    else:
                        if codcompra==2:
                            #sumar unidades
                            doc2=open("productos.txt","r")
                            contenido=doc2.read()
                            print(contenido)
                            codigo=input("Ingrese el Código del Producto a Modificar:")
                            agregar="Unidades"
                            #leyendo el documento con los productos, sacamos el numero de unidades que hay
                            with open("stock.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Unidades" in linea[1]) and (codigo in linea[0]):
                                            unidades=int(linea[2])
                                    else:
                                        if len(linea)<=0:
                                            unidades=0
                            if agregar=="Unidades":
                                mas=-1
                                while int(mas)<0:
                                    #pedimos la nueva cantidad de unidades
                                    print("Ingrese la cantidad de nuevas unidades")
                                    mas=input("Evite ingresar numeros negativos o deberá volver a ingresar el dato: ")
                                    #comprobamos si lo ingresado es un numero o no
                                    try:
                                        #si es posible convertir el dato a INT, comprueba que no sea negativo
                                        with int(mas) as f:
                                            if mas<0:
                                                print("Valor NO Válido")
                                    #si no es posible convertirlo, vuelve a pedir que lo ingresen
                                    except ValueError as e:
                                        print("Valor NO Valido")
                                        mas=-1
                                    #si lo ingresado desde un principio es un numero, se guarda
                                    except AttributeError as f:
                                        mas=int(mas)
                            #enviamos a la funcion del modulo compras los datos obtenidos   
                            nuevasunidadesCompra("stock.txt","op_productos.txt",(codigo+". "+agregar),mas, codigo, unidades)               
                            """--------------------------------------FINAL MODULO COMPRAS------------------------------------------"""
            else:
                if x==4:
                    """----------------------------------MODULO VENTAS-----------------------------------"""                    
                    continuar=1
                    while continuar!=2:
                        venta1=1
                        while venta1!=2:
                            #segun los codigos del inventario revisamos si existe el producto
                            Verproductos=open("productos.txt","r")
                            contenidoproductos=Verproductos.read()
                            print(contenidoproductos)
                            venta=int(input("Ingrese el codigo del producto a vender: "))
                            venta=str(venta)+"."
                            with open("stock.txt") as archivo:
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
                            with open("stock.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Unidades" in linea[1]) and (venta in linea[0]):
                                            unidadF=int(linea[2])
                            #recuperamos el precio del producto y lo guardamos en una lista
                            with open("stock.txt") as archivo:
                                for texto in archivo.readlines():
                                    linea=texto.split()
                                    if len(linea)>1:
                                        if ("Precio" in linea[1]) and (venta in linea[0]):
                                            listad.append(linea[2])
                            #restamos las unidades vendidas
                            unidadN=unidadF-uniV
                            if unidadN<0:
                                print("no se pudo realizar la venta porque no queda stock")
                                lista=[]
                                listad=[]
                                listap=[]
                            else:
                                #realizamos la actualizacion del inventario
                                fin=open("stock.txt","r")
                                fout=open("op_tienda.txt","w")
                                for linea in fin:
                                    if (venta+" Unidades") in linea:
                                        fout.write(venta+" Unidades"+": "+str(unidadN)+"\n")
                                    else:
                                        fout.write(linea)
                                fout.close()
                                fin.close()
                                fout=open("op_tienda.txt","r")
                                contenido=fout.read()
                                fout.close()
                                fin=open("stock.txt","w")
                                fin.write(contenido)
                                fin.close()

                                print("¿desea cotninuar? ingrese 2 para salir, ingrese cualquier numero para continuar")
                                continuar=int(input("Ingrese aqui: "))
                    print(lista)
                    print(listad)
                    print(listap)
                    """--------------------------------------FINAL MODULO VENTAS------------------------------------------"""                            
                else:
                    if x==5:
                        """--------------------------------------MODULO FACTURACIÓN-----------------------------------------"""
                        y=0
                        while y!=3:
                            print("***FACTURACION***")
                            print("<--------------------------------->")
                            print("1. Crear factura")
                            print("2. Revisar facturas existentes")
                            print("3. Regresar")
                            print("<--------------------------------->")
                            stry=input("Ingrese el codigo de la opcion a utilizar: ")
                            #del mismo modo que antes, evitamos que el usuario ingrese letras
                            contador=-1    
                            while contador!=0:
                                for g in range(len(dic)):
                                    if dic[g] in stry:
                                        contador=contador+1
                                if contador!=0:
                                    stry=input("Ingrese el codigo de la opcion a utilizar: ")
                                if stry=="1" or stry=="2" or stry=="3":
                                    contador=0
                            y=int(stry)
                            if y==1:
                                if len(lista)==0:
                                    #si no se ha vendido nada, no se podrá realizar la factura
                                    print("No se ha realizado ninguna venta")
                                else:
                                    #revisa que exista un archivo donde se almacenarán los codigos
                                    checkFileExistance("codigos_facturacion.txt")
                                    cod=open("codigos_facturacion.txt","r+")
                                    codigo=cod.readlines()
                                    #obtiene el número de lineas
                                    num=len(codigo)
                                    #escribe en el txt el codigo
                                    cod.write(str(num)+"\n")
                                    cod.close()
                                    #abrimos el doc de clientes y lo mostramos
                                    clientesL=open("clientes.txt","r")
                                    contenido=clientesL.read()
                                    print(contenido)
                                    nombreCliente="Nada"
                                    #pediremos al usuario que ingrese el codigo de un cliente
                                    print("Ingrese el codigo del cliente")
                                    print("Si no ingresa un cliente, la factura se tomará automaticamente como consumidor final")
                                    codcli=input("Si desea que la factura sea a consumidor final ingrese -1: ")
                                    #buscamos el nombre del cliente segun el codigo
                                    if codcli!="-1":
                                        with open("tiendaClientes.txt") as archivo:
                                            for texto in archivo.readlines():
                                                linea=texto.split()
                                                if len(linea)>1:
                                                    if ((str(codcli)+".") in linea[0]) and ("Nombre:" in linea[1]):
                                                        nombreCliente=linea[2]
                                        #si al final no se encuentra el nombre, quedará como consumidor final
                                        if nombreCliente=="Nada":
                                            nombreCliente="Consumidor Final"
                                    else:
                                        nombreCliente="Consumidor Final"
                                    #revisa la existencia de un documento con ese codigo
                                    checkFileExistance("Factura"+str(num)+".txt")
                                    #incresa los datos a la factura que contenga ese codigo
                                    factura=open("Factura"+str(num)+".txt","a")
                                    factura.write("LOCAL DE VENTAS \n")
                                    factura.write("FACTURA NO. "+str(num)+" \n")
                                    factura.write("Cliente: "+nombreCliente+" \n")
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
                                    #si agregamos un cliente a la factura, se le realizará un descuento 
                                    if nombreCliente!="Consumidor Final":
                                        total=t-(t*0.05)
                                    else:
                                        #si es consumidor final, pagará el precio total
                                        total=t
                                    factura.write(str(total)+"\n")
                                    factura.close()
                                    listad=[]
                                    lista=[]
                                    listap=[]
                            else:
                                if y==2:
                                    #extrae el numero de lineas en el txt de codigos
                                    lector=open("codigos_facturacion.txt","r")
                                    lin=lector.readlines()
                                    num=len(lin)
                                    if num==0:
                                        #si no hay lineas, no hay facturas
                                        print("No existen facturas")
                                    else:
                                        #usamos un for con rango igual al numero de lineas +1 y llamamos a la funcion mostrarfacturas
                                        for z in range(num+1):
                                            mostrarfacturas("Factura"+str(z)+".txt")
                                        buscar=input("Ingrse el numero de la factura que desea ver: ")
                                        #comprobamos si al abrir el archivo nos mostrará un error o no
                                        try:
                                            #si no muestra error, mostramos el contenido del archivo
                                            with open("Factura"+str(buscar)+".txt", 'r') as f:
                                                abrir=open("Factura"+str(buscar)+".txt","r")
                                                contenido=abrir.read()
                                                print(contenido)
                                                abrir.close()
                                        #si nos lanza un error de archivo no encontrado, indicamos al usuario        
                                        except FileNotFoundError as e:
                                        #si no existe, se crea el archivo en blanco
                                            print("No existe la factura requerida")


