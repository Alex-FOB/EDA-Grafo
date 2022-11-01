class Nodo:
    __dato = None
    __siguiente = None
    def __init__(self, dato = None, siguiente = None):
        self.__dato = dato
        self.__siguiente = siguiente
    def setDato(self, dato = None):
        self.__dato = dato
    def setSiguiente(self, siguiente = None):
        self.__siguiente = siguiente
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__siguiente