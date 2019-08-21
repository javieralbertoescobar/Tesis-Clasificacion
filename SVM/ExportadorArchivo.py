
def exportarArchivoSVM(muestra, ubicacion):
    generarEncabezado(muestra, ubicacion, "w")        
    f = open(ubicacion, "a")
    for dato in muestra:
        for k in dato:
            for j in range(len(k)):
                f.write(str(k[j]))
                if(j!=len(k)-1):
                    f.write(",")
            f.write("\n")
    f.close()

def generarEncabezado(muestra, ubicacion, target):
    f = open(ubicacion, target)
    for i in range(len(muestra[0][0])-1):
        f.write("Feature"+str(i+1)+",")
    f.write('Class\n')
    f.close()

def exportarArchivoZPL(muestra, ubicacion):
    f = open(ubicacion, "w")
    for dato in muestra:
        for j in range(len(dato)):
            f.write(str(dato[j]))
            if(j!=len(dato)-1):
                f.write(",")
        f.write("\n")
    f.close()

