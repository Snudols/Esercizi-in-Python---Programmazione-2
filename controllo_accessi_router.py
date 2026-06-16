import random
import ipaddress
import time
from collections import deque

def ipToInt(ip):
    return int(ipaddress.ip_address(ip))

def intToIp(n):
    return str(ipaddress.ip_address(n))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)

blacklist_ip = [
    str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))
    for _ in range(1000)
]

blacklist_int = [ipToInt(ip) for ip in blacklist_ip]

bst = BST()

for ip in blacklist_int:
    bst.insert(ip)

pacchetti = []

for ip in random.sample(blacklist_ip, 10):
    pacchetti.append({
        "ip_sorgente": ip,
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": random.randint(64, 1500)
    })

nuovi_ip = []

while len(nuovi_ip) < 10:
    ip = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

    if ip not in blacklist_ip:
        nuovi_ip.append(ip)

for ip in nuovi_ip:
    pacchetti.append({
        "ip_sorgente": ip,
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": random.randint(64, 1500)
    })

random.shuffle(pacchetti)

queue = deque(pacchetti)

bloccati = 0
permessi = 0

while queue:
    pacchetto = queue.popleft()

    ip = pacchetto["ip_sorgente"]
    ip_int = ipToInt(ip)

    if bst.search(ip_int):
        print(f"{ip} -> BLOCCATO")
        bloccati += 1
    else:
        print(f"{ip} -> PERMESSO")
        permessi += 1

print("\nRIEPILOGO")
print("Bloccati:", bloccati)
print("Permessi:", permessi)

test_ip = random.choice(blacklist_ip)
test_int = ipToInt(test_ip)

ripetizioni = 10000

start = time.perf_counter()

for _ in range(ripetizioni):
    bst.search(test_int)

tempo_bst = time.perf_counter() - start

start = time.perf_counter()

for _ in range(ripetizioni):
    test_int in blacklist_int

tempo_lista = time.perf_counter() - start

print("\nCONFRONTO TEMPI")

print(f"BST: {tempo_bst:.8f} s")
print(f"Lista: {tempo_lista:.8f} s")

if tempo_bst < tempo_lista:
    print(f"BST più veloce di {tempo_lista / tempo_bst:.2f} volte")
else:
    print(f"Lista più veloce di {tempo_bst / tempo_lista:.2f} volte")