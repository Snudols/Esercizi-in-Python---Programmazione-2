class Notifiche:
    def __init__(self):
        self.pila = []

    def arriva(self, messaggio):
        self.pila.append(messaggio)

    def leggi(self):
        if len(self.pila) == 0:
            print("Nessuna notifica.")
        else:
            print("Letta:", self.pila.pop())

    def prossima(self):
        if len(self.pila) == 0:
            print("Nessuna notifica.")
        else:
            print("In cima:", self.pila[-1])


notifiche = Notifiche()

notifiche.arriva("WhatsApp: Ciao!")
notifiche.arriva("Gmail: Hai un nuovo messaggio")
notifiche.arriva("Instagram: Ti hanno taggato")

notifiche.prossima()

notifiche.leggi()
notifiche.leggi()
notifiche.leggi()
notifiche.leggi()