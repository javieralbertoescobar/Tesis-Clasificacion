import GraficadorMuestral as graficador
import GeneradorMuestral as generador
import ExportadorArchivo as exportador
import ClasificadorSVM as clasificador
import ConsultorClase as consultor
import numpy as np

gen = generador.GeneradorMuestral()
graf = graficador.GraficadorMuestral()
exp = exportador.ExportadorArchivo()
clas = clasificador.ClasificadorSVM('rbf')

muestraClase1 = gen.generarMuestra(0,1,2,100,1)
muestraClase2 = gen.generarMuestra(3,1,2,100,0)


consul = consultor.ConsultorClase(gen.getMuestraC1(), gen.getMuestraC2())

print("Clase a la que pertenece: "+str(consul.consultarClase((-0.4995,0.6731))))

#esp = [5,5]
#cov = [[1,0],[0,1]]
#np.random.seed(45)  
#x,y = np.random.multivariate_normal(esp, cov, 2000).T
#x,y = gen.generarMuestraDN(0,100,2,100)
#graf.graficarBidimensional(x, y)
exp.exportarArchivoCSV(muestraClase1+muestraClase2, "input/input.csv")

clas.clasificarMuestra('input/input.csv')




