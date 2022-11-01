from grafo import Grafo

def nodos(cant):
    grafo = Grafo(cant)
    for i in range(cant):
        etiqueta = input('Etiqueta: ')
        grafo.etiquetar(etiqueta)
    return grafo
def conectar(grafo):
    nodoU = input('Nodo 1 (-1 para salir): ')
    nodoV = input('Nodo 2 (-1 para salir): ')
    while nodoU != '-1' and nodoV != '-1':
        try:
            grafo.aristas(nodoU, nodoV)
        except IndexError as error:
            print(error)

        nodoU = input('\nNodo 1 (-1 para salir): ')
        nodoV = input('Nodo 2 (-1 para salir): ')
if __name__ == '__main__':
    try:
        cant = int(input('Ingrese cantidad de nodos: '))
        grafo = nodos(cant)
        conectar(grafo)
        nodo = input('Ingrese nodo: ')
        print('Adyacentes:', grafo.adyacentes(nodo))
        print('Recorrido por anchura:', grafo.rea(nodo))
        print('Recorrido por profundidad:', grafo.rep(nodo))
        nodo1 = input('Ingrese nodo 1: ')
        nodo2 = input('Ingrese nodo 2: ')
        print('Camino entre nodo 1 y 2:', grafo.camino(nodo1, nodo2))
        print('Camino minimo entre nodo 1 y 2:', grafo.caminoMin(nodo1, nodo2))
    except ValueError:
        print('ERROR: cantidad invalido')
    except IndexError as error:
        print(error)