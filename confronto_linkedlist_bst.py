import random
import time

numeri = [random.randint(1, 10000) for _ in range(1000)]


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next = None


class LinkedList:

    def __init__(self):
        self.__head = None

    def append(self, valore):

        nuovo = Nodo(valore)

        if self.__head is None:
            self.__head = nuovo
            return

        corrente = self.__head

        while corrente.next is not None:
            corrente = corrente.next

        corrente.next = nuovo

    def search(self, valore):

        corrente = self.__head

        while corrente is not None:

            if corrente.valore == valore:
                return True

            corrente = corrente.next

        return False


class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.__radice = None

    def insert(self, valore):

        if self.__radice is None:
            self.__radice = NodoBST(valore)

        else:
            self.__insertRicorsivo(self.__radice, valore)

    def __insertRicorsivo(self, nodo, valore):

        if valore < nodo.valore:

            if nodo.left is None:
                nodo.left = NodoBST(valore)

            else:
                self.__insertRicorsivo(nodo.left, valore)

        else:

            if nodo.right is None:
                nodo.right = NodoBST(valore)

            else:
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):

        if nodo is None:
            return False

        if nodo.valore == valore:
            return True

        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.left, valore)

        else:
            return self.__searchRicorsivo(nodo.right, valore)


lista = LinkedList()
albero = BST()

for numero in numeri:
    lista.append(numero)
    albero.insert(numero)

target = numeri[499]

print("Numero da cercare:", target)

inizio_lista = time.perf_counter()
lista.search(target)
fine_lista = time.perf_counter()
tempo_lista = fine_lista - inizio_lista
inizio_bst = time.perf_counter()
albero.search(target)
fine_bst = time.perf_counter()
tempo_bst = fine_bst - inizio_bst

print(f"Tempo LinkedList: {tempo_lista:.10f} secondi")
print(f"Tempo BST: {tempo_bst:.10f} secondi")

rapporto = tempo_lista / tempo_bst

print(f"Il BST è stato circa {rapporto:.2f} volte più veloce")