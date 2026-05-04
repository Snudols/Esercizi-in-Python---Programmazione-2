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


# --- simulazione fila macellaio ---

fila = Queue()

# arrivano i clienti
fila.enqueue("Mario")
fila.enqueue("Giulia")
fila.enqueue("Tonino")
fila.enqueue("Rosa")

print("Servo:", fila.dequeue()) 

fila.enqueue("Enzo")

print("Persone in fila:", fila.size())

while not fila.isEmpty():
    print("Servo:", fila.dequeue())