from Clustering import ClusterContainer 
from CRIO import Grouper as Grouper
from Exporter import writeClusters,writeParameters, writeSolution
from Importer import readSamples
from CRIO import HiperplaneDefiner as Hiperplane
from astroid.__pkginfo__ import classifiers
from __builtin__ import False
import functools

#TO DO: parametrizar estos parametros
#routeClase0 = "model/class0.dat"
#routeClase1 = "model/class1.dat"
routeCluster0 = "model/cluster0.dat"
routeCluster1 = "model/cluster1.dat"
routeParameters = "model/globalParameters"
#dimenssion = 2
#k = 2
M = 1000000


class Classifier():
    def __init__(self, route0,route1,k,d, t0, t1):
        self.routeClase0 = route0
        self.routeClase1 = route1
        self.numGroups = k
        self.dimenssion = d
        self.regions = self.trainClasificator()
        self.tag0 = t0
        self.tag1 = t1
        

    

    def trainClasificator(self):
        
        class0 = readSamples(self.routeClase0, self.dimenssion)
        class1 = readSamples(self.routeClase1, self.dimenssion)        
        
        clusterContainer0 = ClusterContainer(class0,class1)
        clusterContainer1 = ClusterContainer(class1,class0)        
        
        writeClusters(clusterContainer0, class0,routeCluster0)
        writeClusters(clusterContainer1, class1, routeCluster1)
    
        parameters = [(len(class0 + class1)), self.dimenssion, len(class0), len(class1), self.numGroups, clusterContainer0.getCantClusters(), clusterContainer1.getCantClusters(),M]
        writeParameters(parameters, routeParameters)
    
        groupContainer = Grouper.GroupContainer(class1, clusterContainer1, self.numGroups)
        Grouper.deleteOutliers(class0, clusterContainer0, groupContainer.model.e0Vals)
        
        regions = Hiperplane.defineHiperplanes(groupContainer, clusterContainer0)
        return regions
    
   
    def classify(self, sample):
        ret = self.tag0
        for value in self.regions.values():
            results = list(map(lambda hiperplane: hiperplane[0]*sample[0] + hiperplane[1]*sample[1] <= hiperplane[2], value))
            print("resultados: " + str(results) + "\n")
            if reduce(lambda a,b: a and b, results):
                ret = self.tag1
                break
        return ret
        
        
        
    def printRegions(self):
        print("-----------------------------------------------------------------------------------------------------------\n")
        for key, value in self.regions.items():
            print("Region: " + str(key) + " \n Hiperplanos:\n ")
            print("cantidad: " + str(len(key)))
            for hiperplano in value:
                    print(str(hiperplano) + "\n")
            print("-----------------------------------------------------------------------------------------------------------\n")

        
        
        


    