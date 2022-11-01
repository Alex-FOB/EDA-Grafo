from nodo import Nodo

class Pila:
    __tope = None
    def __init__(self):
        self.__tope = None
    def vacia(self):
        return self.__tope == None
    def insertar(self, dato):
        aux = Nodo(dato)
        aux.setSiguiente(self.__tope)
        self.__tope = aux
    def suprimir(self):
        valor = -1
        if(not self.vacia()):
            valor = self.__tope.getDato()
            aux = self.__tope
            self.__tope = self.__tope.getSiguiente()
            del aux
        return valor