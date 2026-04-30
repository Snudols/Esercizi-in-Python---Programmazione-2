class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.__data[-1]

    def bottom(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.__data[0]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def clear(self):
        self.__data.clear()

    def insert(self, index, item):
        self.__data.insert(index, item)

    def contains(self, item):
        return item in self.__data

    def count(self, item):
        return self.__data.count(item)

    def to_list(self):
        return self.__data.copy()

    def print_top_down(self):
        for item in reversed(self.__data):
            print(item)

    def __repr__(self):
        return f"Stack({self.__data})"


history = Stack()

history.push("google.com")
history.push("wikipedia.org")
history.push("python.org")

print("Pila attuale:", history)

print("Cima:", history.peek())
print("Fondo:", history.bottom())
print("Dimensione:", history.size())

history.insert(1, "proton.me")
print("Pila dopo insert:", history)

print("Contiene google.com?", history.contains("google.com"))
print("Quante volte compare google.com?", history.count("google.com"))

print("Stampa dalla cima al fondo:")
history.print_top_down()

lista_copia = history.to_list()
print("Copia della pila come lista:", lista_copia)

removed = history.pop()
print("Tolto:", removed)

print("Pila dopo pop:", history)

history.clear()
print("Pila dopo clear:", history)