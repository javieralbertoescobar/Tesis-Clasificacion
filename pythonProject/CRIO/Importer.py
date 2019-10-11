def listStringToFloat(list):
    l = list[:]
    for j in range(0, len(l)):
        l[j] = (float(l[j]))
    return l

#lee el archivo de muestras en formato zpl indicados en la ruta y retorna un lista de muestras en formato de tuplas.  
def readSamples(route, dimension):
    f = open(route,"r")
    lines = f.readlines()#f
    
    lines = list(map(lambda line: line[:-1], lines))
    lines = list(map(lambda line: line.split(","), lines))
    data = list(map(lambda line: listStringToFloat(line), lines))        
    print("data: " + str(data))
    clase = []
    sample = []

    for i in range(0, len(data) -1,dimension):
        
        for j in range(0, dimension):
            print("data actual: " + str(data[i]) +"\n")
            sample.append(data[i+j][2])
        clase.append(tuple(sample))
        sample = []

    f.close()
    return clase