"""Manuel Salvador Socop Francisco"""
"""Fecha 22 de mayo de 2020"""
"""Modulo de Clientes"""
"""Nuevos, actulizción, agregar, eliminación de datos de los clientes"""
def checkFileExistance(filePath):
    #Comprobar existencia del archivo
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        #si no existe, se crea el archivo en blanco
        doc=open(filePath,"w", encoding="utf-8")

def deleteline(filein, fileout, slinea, fileinP, fileoutP):
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
                #comprueba si el codigo del no producto esta en la primera columna y si no esta, copia la linea al doc Y normal
                if not (slinea in linea[0]):
                    fout.write(texto)
            #si el numero de columnas es 1 entonces la copia normal al doc Y (esto sería para evitar que se borren los separadores)
            if len(linea)==1:
                fout.write(texto)
    #realizamos la misma lectura de lineas en el documento X            
    for lineap in finp:
        #si el codigo del producto no esta en la linea, se copia normalmente al documento Y
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
    #realizamos la misma operacion con el documento X y Y de productos.
    foutp=open(fileoutP,"r")
    contenido=foutp.read()
    foutp.close()
    finp=open(fileinP,"w")
    finp.write(contenido)
    finp.close()
    
def modifline(filein, fileout, slinea, dagre, dmod, deli):
    #abrimos 2 documentos, uno en modo lectura (tiendaClientes) y 1 vacio
    fin = open(filein, "r")
    fout = open(fileout, "w")
    #En caso de querer modificar el nombre, también habría que modificarse el listado de productos
    if dmod=="Nombre":
        #abrimos el documento de productos
        finp=open("clientes.txt","r")
        foutp=open("clientesT.txt","w")
        #buscamos el codigo del producto que se va a cambiar
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
        #abrimos el documento original de productos ahora en modo vacio y agregamos el contenido anteriormente copiado
        finp=open("clientes.txt","w")
        finp.write(contenido)
        finp.close()
    #En caso de querer cambiar cualquier campo que no sea nombre
    #buscamos el codigo y campo del producto (Lo que se envia desde el programa principal es "Codigo.Campo:")
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
    #en el caso de que aquello que vayamos a cambiar sean las unidades, el Nombre o los telefonos, la ganancia se verá afectada y deberá editarse
    if dmod=="Nombre" or dmod=="telefono" or dmod=="Unidades":
        #abrimos de nuevo el documento X (tiendaClientes) y el documento Y vacio
        fin = open(filein, "r")
        fout = open(fileout, "w")
        #la nueva linea a buscar será aquella que contenga el codigo del producto y la palabra "Ganancias"
        slinea=deli+". Ganancia: "

        with open("tiendaClientes.txt") as archivo:
            for texto in archivo.readlines():
                linea=texto.split()
                if len(linea)>1:
                    #si el numero de columnas es mayor que 1 entonces confirmaremos si la primera columna contiene el codigo y la 2da el nombre "Nombre"
                    if ("Nombre" in linea[1]) and (deli in linea[0]):
                        #de ser así, copiaremos a una variable float el contenido de la 3ra columna (que sería el numero ingresado en el campo)
                        NombreT=float(linea[2])
        #realizamos el mismo proceso anteior ahora con el telefono
        with open("tiendaClientes.txt") as archivo:
            for texto in archivo.readlines():
                linea=texto.split()
                if len(linea)>1:
                    if ("telefono" in linea[1]) and (deli in linea[0]):
                        telefonoT=float(linea[2])
        #realizamos el mismo proceso anterior con las unidades
        with open("tiendaClientes.txt") as archivo:
            for texto in archivo.readlines():
                linea=texto.split()
                if len(linea)>1:
                    if ("Unidades" in linea[1]) and (deli in linea[0]):
                        unidadesT=int(linea[2])
        #en una nueva variable se realizará la operación de ganancia
        nganancia=(telefonoT-NombreT)*unidadesT
        #leeremos el documento X y buscaremos la linea que contenga el codigo del producto y el campo "Ganancia"
        for linea in fin:
            #enviaremos los datos del doc X al doc Y
            if slinea in linea:
                #al encontrar el campo "Ganancia" y el codigo, se enviará una linea diferente al doc Y
                fout.write(slinea+str(nganancia)+"\n")
            else:
                fout.write(linea)
        fout.close()
        fin.close()
        #abriremos el doc Y en modo lectura y recuperaremos su datos
        fout=open(fileout,"r")
        contenido=fout.read()
        fout.close()
        #abriremos el doc X vacio y copiaremos los datos del doc Y a este
        fin=open(filein,"w")
        fin.write(contenido)
        fin.close()
def agregarUnidades(filein, fileout, slinea, dagre, deli, auni):
    #igualaremos a 0 las variables a utilizar para evitar problemas
    telefonoT=0
    NombreT=0
    unidadesT=0
    #abriremos un doc X en modo lectura y uno Y vacio
    fin = open(filein, "r")
    fout = open(fileout, "w")
    #sumaremos el total de unidades que sería la suma de las unidades originales mas las nuevas a agregar
    total=int(dagre)+int(auni)
    #leeremos las lineas del doc X y las enviaremos al Y
    for linea in fin:
        #si encontramos en el doc X una linea que cumpla con el codigo del producto y el campo Unidades, se enviará la nueva linea
        if slinea in linea:
            fout.write(slinea+": "+str(total)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #abrimos el documento Y en modo lectura y recuperamos sus datos
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #abrimos el doc X vacio y enviamos los datos del doc Y
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()
    #ya que se editaron las unidades es necesario editar las ganancias
    #abrimos de nuevo el doc X y el doc Y
    fin = open(filein, "r")
    fout = open(fileout, "w")
    #la nueva linea a buscar será el codigo del producto junto con el campo "Ganancia"
    slinea=str(deli)+". Ganancia: "
    #separaremos los contenidos del doc X en columnas
    with open("tiendaClientes.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            #si el numero de columnas es mayor que 1 y la columna 1 tiene el codigo y la 2 tiene la palabra "Nombre", enviaremos a una variable el valor de la 3ra columna
            if len(linea)>1:
                if ("Nombre" in linea[1]) and (deli in linea[0]):
                    NombreT=float(linea[2])  
    #Se utiliza el mismo proceso anterior para obtener el telefono                
    with open("tiendaClientes.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            if len(linea)>1:
                if ("telefono" in linea[1]) and (deli in linea[0]):
                    telefonoT=float(linea[2])
    #se utiliza el mismo proceso anterior para obtener las unidades 
    with open("tiendaClientes.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            if len(linea)>1:
                if ("Unidades" in linea[1]) and (deli in linea[0]):
                    unidadesT=int(linea[2])
    #se realiza la operación de ganancias
    nganancia=(telefonoT-NombreT)*unidadesT
    #comenzaremos a enviar al doc Y los contenidos del doc X
    for linea in fin:
        #si una linea concuerda con el codigo del producto y la palabra "Ganancia", enviaremos una linea diferente
        if slinea in linea:
            fout.write(slinea+str(nganancia)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #abriremos el doc Y en modo lectura y copiaremos sus datos
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #abriremos el doc X vacio y copiaremos dentro de el los datos del doc Y
    fin=open(filein,"w")
    fin.write(contenido)
def getprod(filein, slinea):
    #abrimos el listado de productos existentes en modo lecutra
    fin = open(filein, "r")
    #mostraremos los contenidos de todo producto que concuerde con el codigo del producto para asi hacer un listado con cada campo del producto
    for linea in fin:
        if slinea in linea:
            print(linea)
    fin.close()
#CUERPO DEL PROGRAMA
#igualaremos a 0 la variable del while general
x=0
#igualaremos a -1 las variables de los campos para que las condicionales surtan efecto
telefono=0
#telefono=-1
#unidades=-1
#comprobamos la existencia de los archivos necesarios para el funcionamiento del programa
checkFileExistance("clientes.txt")
checkFileExistance("clientesF.txt")
checkFileExistance("tiendaClientes.txt")
checkFileExistance("clientesT.txt")
checkFileExistance("tiendaClientesT.txt")
#Creamos el menu principal
while x!=6:
    print("***INGRESO DE NUEVOS CLIENTES***")
    print("<--------------------------------->")
    print("1. Ingreso de Nuevos Productos") 
    print("2. Muestra de los clientes existentes")
    print("3. Modificacion de clientes")
    print("4. Elimninacion de clientes")
    print("5. Salir")
    print("<--------------------------------->")
    x=int(input("Ingrese la opcion que desea utilizar: "))
    if x==1:
        #comenzamos abriendo el documento de la tiendaClientes
        doc=open("tiendaClientes.txt","a")
        #coemnzamos a ingresar los datos
        nombre=input("Ingrese el nombre completo del cliente: ")
        fecha=input("Ingrese la Fecha de Nacimiento: ")
        dpi=input("Ingrese su CUI: ")
        direccion=input("Ingrese su telefono: ")
        telefono=input("Ingrese su número de telefono: ")
        nit=input("Ingrese su no. de NIT: ")
        #si el telefono ingresado es negativo se pedirá volver a ingresar los datos
        """while telefono>0:
            Nombre=float(input("Ingrese su número de teléfono: "))
            if telefono>0:
                print("valor no valido")
        #si el telefono es negativo o menor al Nombre se pedira volver a ingresar el dato
        while telefono<0 or telefono<Nombre:
            telefono=float(input("Ingrese el telefono de venta: "))
            if telefono<0 or telefono<Nombre:
                print("valor no valido")"""
        #si las unidades son negativas se pedira volver a ingresar el dato
        """while unidades<0:
            unidades=int(input("Ingrese las Unidades: "))
            if unidades<0:
                print("valor no valido") """
        """#realizamos la operacion para las ganancias
        ganancia=(telefono-Nombre)*unidades
        #enviamos al documento un separador"""
        doc.write("************************** \n")
        #abrimos el documento que contendrá el listado de productos y leemos sus lineas
        doc2=open("clientes.txt","r")
        lineas=doc2.readlines()
        doc2.close()
        #abrimos el doc que contendrá los codigos utilizados hasta ahora y leeremos sus lineas
        doc3=open("clientesF.txt","r")
        lineas=doc3.readlines()
        doc3.close()
        #abriremos el doc de codigos en modo escritura
        doc3=open("clientesF.txt","a")
        #enviaremos al doc de productos y al de codigos una linea conteniendo el nombre y un codigo equivalente al numero de lineas en el doc de codigos
        doc3.write(str(len(lineas))+". "+nombre+"\n")
        doc2.write(str(len(lineas))+". "+nombre+"\n")
        doc3.close()
        doc2.close()
        #enviaremos al doc que contendrá todos los datos los datos del producto junto con el codigo anterior obtenido
        doc.write(str(len(lineas))+". Datos del cliente: \n")
        doc.write(str(len(lineas))+ ". Nombre: "+ nombre + "\n")
        doc.write(str(len(lineas))+". Fecha: "+ fecha + "\n")
        doc.write(str(len(lineas))+". CUI: " + str(dpi) + "\n")
        doc.write(str(len(lineas))+". Dirección: " + direccion +"\n" )
        doc.write(str(len(lineas))+". Telefono: " + str(telefono) + "\n")
        doc.write(str(len(lineas))+". NIT: "+str(nit) + "\n")
        doc.close()
        #regresamos el valor de Nombre, telefono y unidades a -1 para evitar errores al volver a ingresar productos
        Nombre=0
        #telefono=-1
        #unidades=-1
        print("Datos guardados con éxito")
    else:
        if x==2:
            #abriremos el doc tiendaClientes, leeremos su contenido y lo mostraremos
            doc=open("tiendaClientes.txt","r")
            contenido=doc.read()
            print(contenido)
            doc.close()
        else:
            if x==6:
                #EDITOR DE UNIDADES
                #abriremos el documento que contiene todos los clientes existentes y mostramos su contenido
                doc2=open("clientes.txt","r")
                contenido=doc2.read()
                print(contenido)
                #ingresamos el codigo del cliente al que queremos agregar unidades
                eli=input("Ingrese el codigo del cliente que desea cambiar: ")
                #guardamos en una variable la palabra "unidades" para usarla después
                mod="Unidades"
                #abrimos el documento que contiene los datos de los productos y separamos su contenido en columnas
                with open("tiendaClientes.txt") as archivo:
                    for texto in archivo.readlines():
                        linea=texto.split()
                        #si el numero de columnas es mayor a 1 y la 1ra columna tiene el codigo del producto a cambiar
                        #y la segunda columna dice "Unidades", se guarda el valor de la 3ra columna (la cantidad de unidades)
                        if len(linea)>1:
                            if ("Unidades" in linea[1]) and (eli in linea[0]):
                                unidades=int(linea[2])
                        else:
                            #si no existen lineas entonces las unidades serán 0
                            if len(linea)<=0:
                                unidades=0
                #si nuestra varibale del campo que vamos a cambiar es "Unidades"entonces ingresaremos la cantidad de unidades a agregar
                if mod=="Unidades":
                    agre=-1
                    #usamos un while para confirmar que el dato ingresado no sea negativo
                    while int(agre)<0:
                        agre=input("Ingrese el dato que desea colocar: ")
                        if int(agre)<0:
                            print("Valor no valido")
                #enviamos los doumentos a utilizar, el codigo del producto junto con el campo "Unidades", y las unidades existentes a la funcion AgregarUnidades
                agregarUnidades("tiendaClientes.txt","tiendaClientesT.txt",(eli+". "+mod),agre, eli, unidades)

                    
            else:
                if x==3:
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
                    #ya que la ganancia no puede ser editada a menos que se edite el Nombre, telefono y unidades, usamos un while para evitar su modificacion
                    while mod=="Ganancia":
                        print("La ganancia no puede ser editada, cambie alguno de los demas valores")
                        mod=input("Ingrese el nombre del campo que desea editar (distingue entre mayusculas y minusculas, ej: Nombre, Nombre): ")
                    #abrimos el documento que contiene los datos de los productos y obtendremos los datos de Nombre del producto
                    #del mismo modo que se ha hecho anteriormente
                    with open("tiendaClientes.txt") as archivo:
                        for texto in archivo.readlines():
                            linea=texto.split()
                            if len(linea)>1:
                                if ("Nombre" in linea[1]) and (eli in linea[0]):
                                    NombreT=float(linea[2])
                    #recuperaremos también el valor del telefono del producto
                    with open("tiendaClientes.txt") as archivo:
                        for texto in archivo.readlines():
                            linea=texto.split()
                            if len(linea)>1:
                                if ("telefono" in linea[1]) and (eli in linea[0]):
                                    telefonoT=float(linea[2])
                    #dejamos la variable agre (agregacion) en -1 para que las condicionales funcionen correctamente
                    agre=-1
                    #si se va a editar el Nombre se confirma que el dato a ingresar no sea mayor al telefono de venta ni tampoco negativo
                    if mod=="Nombre":
                        while float(agre)>telefonoT or int(agre)<0:
                            agre=float(input("Ingrese el dato que desea colocar: "))
                            if float(agre)>telefonoT or int(agre)<0:
                                print("Valor no valido")
                    #si se va a editar el telefono se confirma que no sea menor al Nombre que ya existe y que tampoco sea negativo
                    if mod=="telefono":
                        while float(agre)<NombreT or int(agre)<0:
                            agre=input("Ingrese el dato que desea colocar: ")
                            if float(agre)<NombreT or int(agre)<0:
                                print("Valor no valido")
                    #si se va a editar las unidades existentes (editar todo el campo en lugar de sumar unidades) se confirma que el numero no sea negativo
                    if mod=="Unidades":
                        while int(agre)<0:
                            agre=input("Ingrese el dato que desea colocar: ")
                            if int(agre)<0:
                                print("Valor no valido")
                    #si lo que se va a editar es el nombre, simplemente se guarda lo que se escriba            
                    if mod=="Nombre":
                        agre=input("Ingrese el dato que desea colocar: ")
                    #enviamos los documentos que se van a editar 
                    #junto con el codigo y campo a editar juntos en una variable
                    #y tambiénel codigo y campo separados a la funcion modificar linea
                    modifline("tiendaClientes.txt","tiendaClientesT.txt",(eli+". "+mod),agre, mod, eli)

                else:
                    if x==4:
                        #leeremos el contenido de productos y lo mostraremos
                        doc2=open("clientes.txt","r")
                        contenido=doc2.read()
                        print(contenido)
                        eli=input("Ingrese el codigo del cliente que desea eliminar: ")
                        #enviaremos a la funcion eliminar los documentos que van a cambiar y el codigo del producto a eliminar
                        deleteline("tiendaClientes.txt","tiendaClientesT.txt",(eli+"."),"clientes.txt","clientesT.txt")
               

        



