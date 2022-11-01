from nodo import Nodo

class Cola:
    __primer = None
    __ultimo = None
    def __init__(self):
        self.__primer = None
        self.__ultimo = None
    def vacia(self):
        return self.__primer == None
    def insertar(self, dato):
        aux = Nodo(dato)
        aux.setSiguiente(None)
        if(self.__ultimo == None):
            self.__primer = aux
            self.__ultimo = aux
        else:
            self.__ultimo.setSiguiente(aux)
            self.__ultimo = aux
        #return self.__ultimo.getDato()
    def suprimir(self):
        if(self.vacia()):
            print('Cola vacia')
            return -1
        else:
            aux = self.__primer
            x = self.__primer.getDato()
            self.__primer = self.__primer.getSiguiente()
            if(self.__primer == None):
                self.__ultimo = None
            del(aux)
            return x