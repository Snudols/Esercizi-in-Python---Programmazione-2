class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuovo = Node(data)

        if self.head is None:
            self.head = nuovo
            nuovo.next = nuovo
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = nuovo
        nuovo.next = self.head

    def insertAfter(self, target, data):
        current = self.head

        while True:
            if current.data == target:
                nuovo = Node(data)
                nuovo.next = current.next
                current.next = nuovo
                return

            current = current.next

            if current == self.head:
                break

    def remove(self, target):
        if self.head is None:
            return

        if self.head.data == target:

            if self.head.next == self.head:
                self.head = None
                return

            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == target:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

    def traverse(self, n):
        if self.head is None:
            return

        current = self.head

        for _ in range(n):
            print(current.data)
            current = current.next

    def size(self):
        if self.head is None:
            return 0

        count = 1
        current = self.head.next

        while current != self.head:
            count += 1
            current = current.next

        return count

    def __str__(self):
        if self.head is None:
            return "[]"

        elementi = []
        current = self.head

        while True:
            elementi.append(current.data)
            current = current.next

            if current == self.head:
                break

        return " -> ".join(elementi)


team = CircularLinkedList()

team.append("alice")
team.append("bob")
team.append("carlo")

print(team)

print("\nPrimi 6 turni:")
team.traverse(6)

team.insertAfter("bob", "diana")

print("\nLista aggiornata:")
print(team)

print("\nAltri 8 turni:")
team.traverse(8)

team.remove("bob")

print("\nDopo la rimozione di bob:")
print(team)

print("\nUltimi 6 turni:")
team.traverse(6)

print("\nNumero analisti:", team.size())