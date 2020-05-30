"""Sumpango Sacatepéquez 22/05/2020
Eddy Edson Armando Cubur Xicón Carné: 1990-19-16696
Módulo Compras-Proyecto Final"""

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        doc=open(filePath,"w", encoding="utf-8")

def nuevasunidades(filein, fileout, slinea, dagre, deli, auni):
    fin = open(filein, "r")
    fout = open(fileout, "w")
    total=int(dagre)+int(auni)
    for linea in fin:
        if slinea in linea:
            fout.write(slinea+": "+str(total)+"\n")
        else:
            fout.write(linea)
    fout.close()
    fin.close()
    fout=open(fileout,"r")
    contenido=fout.read()
    fout.close()
    fin=open(filein,"w")
    fin.write(contenido)
    fin.close()

x=0
unidades=-1
checkFileExistance("Inventario.txt")
checkFileExistance("ListaProductos.txt")
checkFileExistance("InventarioTotal.txt")

while x!=3:
    print("1. Ingreso de Productos")
    print("2. Añadir Stokc")
    print("3. Salir")
    x=int(input("Ingrese la Opción: "))

    if x==1:
        doc1=open("Inventario.txt","a")
        nombre=input("Ingrese el Nombre del Producto: ")
        while unidades<0:
            unidades=int(input("Ingrese las Unidades Compradas:"))
            if unidades<0:
                print("Valor NO Válido")
        #Listado de Productos
        doc2=open("ListaProductos.txt","r")
        lineas=doc2.readlines()
        doc2.close()
        doc2=open("ListaProductos.txt","a")
        doc2.write(str(len(lineas))+ "."+nombre+"\n")
        doc2.close()
        doc1.write(str(len(lineas))+ ". Nombre: "+ nombre + "\n")
        doc1.write(str(len(lineas))+ ". Unidades: "+ str(unidades) + "\n")  
        doc1.close()
        unidades=-1
        print("Datos Guardado con éxito!")
    else:
        if x==2:
            doc2=open("ListaProductos.txt","r")
            contenido=doc2.read()
            print(contenido)
            codigo=input("Ingrese el Código del Producto a Modificar:")
            agregar="Unidades"
            with open("Inventario.txt") as archivo:
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
                    mas=input("Ingrese las Nuevas Unidades: ")
                    if int(mas)<0:
                        print("Valor NO Válido!")
            nuevasunidades("Inventario.txt","InventarioTotal.txt",(codigo+". "+agregar),mas, codigo, unidades)