history = ["google.com", "wikipedia.org", "python.org"]
forward = []

current = history.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")

forward.append(current)
current = history.pop()

print(f"\nPagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")

forward.append(current)
current = history.pop()

print(f"\nPagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")

history.insert(1, "yahoo.com")

history[0]
history[1]

history.remove("google.com")
history.pop(0)

history.sort()
history.reverse()