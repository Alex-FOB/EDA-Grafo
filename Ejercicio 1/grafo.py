import numpy as np

from cola import Cola

from pila import Pila

class Grafo:
    __matriz = None
    __etiquetas = None #arreglo de nodos
    def __init__(self, cant = 0):
        self.__matriz = np.zeros((cant, cant))
        self.__etiquetas = []
    def adyacentes(self, u):
        lista = []
        pos = self.buscar(u)
        if(pos != -1):
            for i in range(len(self.__etiquetas)):
                if(self.__matriz[pos][i] == 1):
                    lista.append(self.__etiquetas[i])
        else:
            raise IndexError('ERROR.ADYACENTES: nodo invalido')
        return lista
    def camino(self, u, v): #devuelve si hay o no camino entre u y v
        camino = self.rea(u)
        band = False
        i = 0
        while not band and i < len(camino): #se busca si el nodo v esta en la lista de los nodos conectados a u
            if(camino[i] == v):
                band = True
            i += 1
        return band
    def caminoMin(self, u, v): #devuelve el camino minimo entre u y v
        lista = []
        if(self.camino(u, v)):
            long = 9999999
            ady = self.adyacentes(u)
            for nodo in ady:
                verf = list(ady)
                verf.append(u)
                min = [u]

                band = False
                pila = Pila()
                pila.insertar(nodo)
                while not band and not pila.vacia():
                    x = pila.suprimir()
                    if(x == v):
                        min.append(x)
                        band = True
                    else:
                        min.append(x)
                        ady2 = self.adyacentes(x)
                        #-----------------------------REVISAR
                        for nodo2 in ady2:
                            if(nodo2 not in verf):
                                pila.insertar(nodo2)
                                if(nodo2 == v):
                                    min.append(nodo2)
                                    band = True
                        #-----------------------------
                        verf.append(x)
                if(len(min) < long and band == True):
                    lista = min
                    long = len(min)
                print(min)
        return lista
    def conexo(self):
        pass
    def aciclico(self):
        pass
    def recubrimiento(self): #devuelve el arbol de recubrimiento (minimo)
        pass 
    def rea(self, u): #procesa el grafo en anchura
        recorrido = []
        pos = self.buscar(u)
        if(pos != -1):
            lista = []
            for i in range(len(self.__etiquetas)):
                lista.append(-1) #todos los nodos no estan marcados
            lista[pos] = 0 #marcar el origen

            cola = Cola()
            cola.insertar(u)
            while not cola.vacia():
                v = cola.suprimir()
                recorrido.append(v)
                ady = self.adyacentes(v) #se obtienen los nodos adyacentes
                for nodo in ady:
                    pos = self.buscar(nodo)
                    if(pos != -1 and lista[pos] == -1):
                        lista[pos] = 1
                        cola.insertar(nodo)
            return recorrido
        else:
            raise IndexError('ERROR.REA: nodo invalido')
    def rep(self, u): #procesa el grafo en profundidad
        recorrido = []
        pos = self.buscar(u)
        if(pos != -1):
            lista = []
            for i in range(len(self.__etiquetas)):
                lista.append(-1)
            lista[pos] = 0
            pila = Pila()
            pila.insertar(u)
            while not pila.vacia():
                v = pila.suprimir()
                recorrido.append(v)
                ady = self.adyacentes(v)
                for nodo in ady:
                    pos = self.buscar(nodo)
                    if(pos != -1 and lista[pos] == -1):
                        lista[pos] = 1
                        pila.insertar(nodo)
            return recorrido
        else:
            raise IndexError('ERROR.REP: nodo invalido')
    
    #ADICIONAL
    def aristas(self, u, v):
        pos1 = self.buscar(u)
        pos2 = self.buscar(v)
        if(pos1 != -1 and pos2 != -1):
            self.__matriz[pos1][pos2] = 1
            self.__matriz[pos2][pos1] = 1
        else:
            raise IndexError('ERROR.ARISTAS: etiqueta invalida')
    def etiquetar(self, etiqueta):
        self.__etiquetas.append(etiqueta)
    def buscar(self, etiqueta):
        pos = -1
        band = False
        i = 0
        while not band and i < len(self.__etiquetas):
            if(self.__etiquetas[i] == etiqueta):
                pos = i
                band = True
            i += 1
        return pos