class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuovo = Node(data)

        if self.head is None:
            self.head = nuovo
            return

        corrente = self.head

        while corrente.next is not None:
            corrente = corrente.next

        corrente.next = nuovo

    def insertAfter(self, target, data):
        corrente = self.head

        while corrente is not None:
            if corrente.data == target:
                nuovo = Node(data)
                nuovo.next = corrente.next
                corrente.next = nuovo
                return

            corrente = corrente.next

    def insertBefore(self, target, data):
        nuovo = Node(data)

        if self.head is None:
            return

        if self.head.data == target:
            nuovo.next = self.head
            self.head = nuovo
            return

        precedente = None
        corrente = self.head

        while corrente is not None:
            if corrente.data == target:
                precedente.next = nuovo
                nuovo.next = corrente
                return

            precedente = corrente
            corrente = corrente.next

    def removeFirst(self):
        if self.head is not None:
            self.head = self.head.next

    def removeLast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        corrente = self.head

        while corrente.next.next is not None:
            corrente = corrente.next

        corrente.next = None

    def size(self):
        count = 0
        corrente = self.head

        while corrente is not None:
            count += 1
            corrente = corrente.next

        return count

    def peekLast(self):
        if self.head is None:
            return None

        corrente = self.head

        while corrente.next is not None:
            corrente = corrente.next

        return corrente.data

    def __str__(self):
        elementi = []

        corrente = self.head

        while corrente is not None:
            elementi.append(corrente.data)
            corrente = corrente.next

        return " -> ".join(elementi)


cronologia = LinkedList()

cronologia.append("admin")
cronologia.append("mario")
cronologia.append("sara")

print(cronologia)

cronologia.insertAfter("mario", "guest")

print(cronologia)

cronologia.insertBefore("admin", "root")

print(cronologia)

cronologia.insertBefore("sara", "luca")

print(cronologia)

cronologia.removeFirst()

print(cronologia)

cronologia.removeLast()

print(cronologia)

print("Numero modifiche:", cronologia.size())

print("Ultima modifica:", cronologia.peekLast())