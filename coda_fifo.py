from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        return self.__data[0]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue({list(self.__data)})"


coda = Queue()

coda.enqueue("Mario")
coda.enqueue("Luigi")
coda.enqueue("Anna")

print("Coda:", coda)
print("Primo elemento:", coda.peek())
print("Dimensione:", coda.size())

print("Servito:", coda.dequeue())

print("Coda aggiornata:", coda)
print("Dimensione:", coda.size())
print("Coda vuota?", coda.isEmpty())