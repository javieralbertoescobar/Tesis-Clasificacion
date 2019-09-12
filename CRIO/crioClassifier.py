from clusteringV2 import ClusterContainer 
from pyscipopt import Model
from grouper import GroupContainer
from fileManager import writeClusters,writeParameters, readSamples
import hiperplaneDefiner as Hiperplane


#TO DO: parametrizar estos parametros
routeClase0 = "model/class0.dat"
routeClase1 = "model/class1.dat"
routeCluster0 = "model/cluster0.dat"
routeCluster1 = "model/cluster1.dat"
routeParameters = "model/globalParameters"
dimenssion = 2
k = 2
M = 1000000

def trainClasificator():
    
    print("Leyendo muestras...")
    class0 = readSamples(routeClase0, dimenssion)
    class1 = readSamples(routeClase1, dimenssion)

    print("Creando clusters...")
    clusterContainer0 = ClusterContainer(class0,class1)
    clusterContainer1 = ClusterContainer(class1,class0)    

    print("Escribiendo clusters...")
    writeClusters(clusterContainer0, class0,routeCluster0)
    writeClusters(clusterContainer1, class1, routeCluster1)

    print("escribiendo parametros...")
    parameters = [(len(class0 + class1)), dimenssion, len(class0), len(class1), k, clusterContainer0.getCantClusters(), clusterContainer1.getCantClusters(),M]
    writeParameters(parameters, routeParameters)


    print("Asignando clusters a grupos...")
    groups = GroupContainer(clusterContainer1, k)
    
    print("clase 0: " + str(class0))
    print("clase 1: " + str(class1))
    print("cluster 0: " + str(clusterContainer0.getClusters()))
    print("cluster 1: " + str(clusterContainer1.getClusters()))
    print ("grupos: " + str(groups.getGroups()))

    print("Definiendo hiperplanos...")
    regiones = Hiperplane.defineHiperplanes(groups, clusterContainer0)

    print("-----------------------------------------------------------------------------------------------------------\n")
    for key, value in regiones.items():
        print("Region: " + str(key) + " \n Hiperplanos:\n ")
        print("cantidad: " + str(len(key)))
        for hiperplano in value:
                print(str(hiperplano) + "\n")
        print("-----------------------------------------------------------------------------------------------------------\n")

    

def main():
    trainClasificator()

main()
    