from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def bfs(grafo, start):
    print("===== BFS =====")

    coda = deque([start])
    visitati = set()
    result = []

    passo = 0

    while coda:
        print(f"\nPasso {passo}")
        print("Coda:", list(coda))
        print("Visitati:", visitati)
        print("Result:", result)

        nodo = coda.popleft()

        if nodo not in visitati:
            visitati.add(nodo)
            result.append(nodo)

            for vicino in grafo[nodo]:
                if vicino not in visitati:
                    coda.append(vicino)

        passo += 1

    print("\nRisultato finale BFS:", result)


def dfs(grafo, start):
    print("\n===== DFS =====")

    pila = [start]
    visitati = set()
    result = []

    passo = 0

    while pila:
        print(f"\nPasso {passo}")
        print("Pila:", pila)
        print("Visitati:", visitati)
        print("Result:", result)

        nodo = pila.pop()

        if nodo not in visitati:
            visitati.add(nodo)
            result.append(nodo)

            for vicino in reversed(grafo[nodo]):
                if vicino not in visitati:
                    pila.append(vicino)

        passo += 1

    print("\nRisultato finale DFS:", result)


bfs(grafo, 'A')
dfs(grafo, 'A')