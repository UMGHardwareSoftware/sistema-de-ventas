#Fecha 15 de mayo 2020
#Sumpango Sacatépequez
#Sergio Orlando Tajín Cubur Carnet: 1990-19-14892
#Modulo Inventario. Proyecto final. Programación I

def checkFileExistance(filePath):
    #se comprueba la existencia del archivo
    try: 
        with open(filePath, 'r') as f:
            return True
    #si el archivo no exite, se crea
    except FileNotFoundError as e:            
        doc=open(filePath,"w", encoding="utf-8")

def deleteline(filein, fileout, slinea, fileinP, fileoutP):
    #se abre un archivo de lectura 
    fin = open(filein, "r")
    finp=open(fileinP, "r")
    #se abre un archivo de escritura
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
            #si número de lines = 1, copia normal al archivo, evita que se eliminen los separadores
            if len(linea)==1:
                fout.write(texto)           
    for lineap in finp: 
        if not slinea in lineap:
            foutp.write(lineap)          
    fout.close()
    foutp.close()
    fin.close()
    finp.close()
    #se abre el archivo y se recupera el contenido
    fout=open(fileout,"r") 
    contenido=fout.read()
    fout.close()
    #se abre el archivo y se ingresa el contenido
    fin=open(filein,"w") 
    fin.write(contenido)
    fin.close()

    foutp=open(fileoutP,"r") 
    contenido=foutp.read()
    foutp.close()
    finp=open(fileinP,"w")
    finp.write(contenido)
    finp.close()
    
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
    #se abre un archivo en modo lectura y recuperaremos el contenido
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #se abre el archivo vacio y se ingresa el cotenido el archivo que se abrió.
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()
    #si se va a cambiar el precio o la cantidad de unidades
    if dmod=="Precio" or dmod=="Unidades":
        #se abre el archivo stock y el archivo vacío
        fin = open(filein, "r")
        fout = open(fileout, "w")
        #se abre el archivo stock para modificar el precio
        with open("stock.txt") as archivo:
            for texto in archivo.readlines():
                linea=texto.split()
                if len(linea)>1:
                    if ("Precio" in linea[1]) and (deli in linea[0]):
                        PrecioT=float(linea[2])
        #se abre el archivo stock para modificar las unidades
        with open("stock.txt") as archivo:
            for texto in archivo.readlines():
                linea=texto.split()
                if len(linea)>1:
                    if ("Unidades" in linea[1]) and (deli in linea[0]):
                        unidadesT=int(linea[2])
        fout.close()
        fin.close()
        #se abre el archivo en modo lectura y se recuperan los datos
        fout=open(fileout,"r")
        contenido=fout.read()
        fout.close()
        #abriremos el archivo vacío y se copian los datos
        fin=open(filein,"w")
        fin.write(contenido)
        fin.close()

def agregarUnidades(filein, fileout, slinea, dagre, deli, auni):
    #se igualan las variables a 0
    PrecioT=0
    unidadesT=0
    #se abre el archivo en modo lectura y se recuperan los datos
    fin = open(filein, "r")
    fout = open(fileout, "w")
    #se suman las unidades agregadas
    total=int(dagre)+int(auni)
    #se leen las líneas de un archivo y se envian al otro archivo.
    for linea in fin:
        if slinea in linea:
            fout.write(slinea+": "+str(total)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    #se abre archivo en modo lectura y recuperamos sus datos
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #se leen las líneas de un archivo y se envian al otro archivo
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()
    #se abre el archivo stock
    with open("stock.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()  
    #Se utiliza el mismo proceso anterior para obtener el precio                
    with open("stock.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            if len(linea)>1:
                if ("Precio" in linea[1]) and (deli in linea[0]):
                    PrecioT=float(linea[2])
    #se utiliza el mismo proceso anterior para obtener las unidades 
    with open("stock.txt") as archivo:
        for texto in archivo.readlines():
            linea=texto.split()
            if len(linea)>1:
                if ("Unidades" in linea[1]) and (deli in linea[0]):
                    unidadesT=int(linea[2])
    fout.close()
    fin.close()
    #se abre el archivo en modo lectura y se copian sus datos
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    #se abre el archivo vacío y se compian los datos del otro archivo
    fin=open(filein,"w")
    fin.write(contenido)
def getprod(filein, slinea):
    #se abre el listado de productos existentes en modo lecutra
    fin = open(filein, "r")
    for linea in fin:
        if slinea in linea:
            print(linea)
    fin.close()
#cuerpo del programa
#se iguala la variable a 0 del bucle while general
x=0
#se igualan a -1 las variables de los campos para que las condicionales surtan efecto
precio=-1
unidades=-1
#comprobamos la existencia de los archivos necesarios para el funcionamiento del programa
checkFileExistance("productos.txt")
checkFileExistance("registros.txt")
checkFileExistance("stock.txt")
checkFileExistance("op_stock.txt")
checkFileExistance("op_tienda.txt")
#se crea el menu principal para el inventario
while x!=6:
    print("Inventario")
    print("1. Ingreso de nuevos productos")
    print("2. Ver stock de productos")
    print("3. Agregar unidades")
    print("4. Editar producto")
    print("5. Elimninar producto")
    print("6. Salir")
    x=int(input("Ingrese la opcion que desea utilizar: "))
    if x==1:
        #ingreso de nuevos productos
        #se abre el archivo stock
        doc=open("stock.txt","a")
        #pide ingresar el nombre del producto nuevo
        nombre=input("Ingrese el nombre del producto: ")
        while precio<0:
            precio=float(input("Ingrese el precio de venta: "))
            if precio<0:
                print("Valor no valido")
        #mientras unidades sean negativas el programa no continuará
        while unidades<0:
            unidades=int(input("Ingrese las Unidades: "))
            if unidades<0:
                print("Valor no valido") 
        doc.write("++++++++++++++++++++++++++++++++++++ \n")
        #se abre el archivo que tendrá la información de los productos
        doc2=open("productos.txt","r")
        lineas=doc2.readlines()
        doc2.close()
        doc2=open("productos.txt","a")
        #se abre el archivo que tendrá los registros
        doc3=open("registros.txt","r")
        lineas=doc3.readlines()
        doc3.close()
        #se abre archivo en modo escritura
        doc3=open("registros.txt","a")
        #se envía al archivo de productos y registros la información con los códigos basado en el número de lína del producto
        doc3.write(str(len(lineas))+". "+nombre+"\n")
        doc2.write(str(len(lineas))+". "+nombre+"\n")
        doc3.close()
        doc2.close()
        #se envía al archivo la información del producto
        doc.write(str(len(lineas))+". Información del producto: \n")
        doc.write(str(len(lineas))+ ". Nombre: "+ nombre + "\n")
        doc.write(str(len(lineas))+ ". Precio: "+ str(precio) + "\n")
        doc.write(str(len(lineas))+ ". Unidades: "+ str(unidades) + "\n")
        doc.close()
        precio=-1
        unidades=-1
        print("¡Producto agregado correctamente!")
        print("++++++++++++++++++++++++++++++++++++ \n")
    else:
        if x==2:
            #ver stock de productos
            #se abre el archivo stock leeremos su contenido y lo mostraremos
            doc=open("stock.txt","r")
            contenido=doc.read()
            print(contenido)
            doc.close()
        else:
            if x==3:
                #agregar unidades
                #se abre el archivo que contiene todos los productos existentes y mostramos su contenido
                doc2=open("productos.txt","r")
                contenido=doc2.read()
                print(contenido)
                #se solicita el código del producto al que se le van a agregar unidades
                eli=input("Ingrese el codigo del producto que desea editar: ")
                mod="Unidades"
                #se abre el archivo stock que contiene los datos de los productos y separamos su contenido en columnas
                with open("stock.txt") as archivo:
                    for texto in archivo.readlines():
                        linea=texto.split()
                        if len(linea)>1:
                            if ("Unidades" in linea[1]) and (eli in linea[0]):
                                unidades=int(linea[2])
                        else:
                            #si no existen lineas entonces las unidades serán 0
                            if len(linea)<=0:
                                unidades=0
                #si la variable es igual a unidades, se permite ingresar las unidades
                if mod=="Unidades":
                    agre=-1
                    #bucle para no ingresar números negativos
                    while int(agre)<0:
                        agre=input("Digite las unidades que va agregar: ")
                        if int(agre)<0:
                            print("Valor no valido")
                #se envía la información al archivo stock
                agregarUnidades("stock.txt","op_tienda.txt",(eli+". "+mod),agre, eli, unidades)
      
            else:
                if x==4:
                    #editar producto
                    #se abre el archivo con el listado de productos y mostraremos su contenido
                    doc2=open("productos.txt","r")
                    contenido=doc2.read()
                    print(contenido)
                    #el prodrama solicita el código del producto que se va editar
                    eli=input("Ingrese el codigo del producto que desea editar: ")
                    #se muestran los campos a editar
                    getprod("stock.txt",(eli+"."))
                    #el programa solicita el nombre del campo que se va editar
                    mod=input("Escriba el nombre del campo que va a editar, el programa distingue mayúsculas y minúsculas: ")
                    #se abre el archivo stock
                    with open("stock.txt") as archivo:
                        for texto in archivo.readlines():
                            linea=texto.split()
                            if len(linea)>1:
                                if ("Precio" in linea[1]) and (eli in linea[0]):
                                    PrecioT=float(linea[2])
                    #se deja la variable en -1 para que funcione
                    agre=-1
                    #si se edita el precio 
                    if mod=="Precio":
                        while float(agre)<0 or int(agre)<0:
                            agre=input("Ingrese el nuevo dato que va a mostrar: ")
                            if float(agre)<0 or int(agre)<0:
                                print("Valor no valido")
                    #si se editan las unidades, no se permiten números negativos
                    if mod=="Unidades":
                        while int(agre)<0:
                            agre=input("Ingrese el nuevo dato que va a mostrar: ")
                            if int(agre)<0:
                                print("Valor no valido")
                    #si se edita el nombre, el programa guarda todo lo que se escriba          
                    if mod=="Nombre":
                        agre=input("Ingrese el nuevo dato que va a mostrar: ")
                    modifline("stock.txt","op_tienda.txt",(eli+". "+mod),agre, mod, eli)

                else:
                    if x==5:
                        #eliminar producto
                        #se lee el contenido del archivo productos y lo mostraremos
                        doc2=open("productos.txt","r")
                        contenido=doc2.read()
                        print(contenido)
                        eli=input("Ingrese el codigo del producto que desea eliminar: ")
                        #elimina el producto
                        deleteline("stock.txt","op_tienda.txt",(eli+"."),"productos.txt","op_stock.txt")