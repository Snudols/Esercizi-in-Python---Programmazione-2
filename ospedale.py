class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni"


class Paziente(Persona):
    def __init__(self, nome, cognome, eta, codice_id,
                 gruppo_sanguigno, patologie, allergie):

        super().__init__(nome, cognome, eta)

        self.codice_id = codice_id
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = patologie
        self.allergie = allergie

    def __str__(self):
        return (f"Paziente: {self.nome} {self.cognome} "
                f"(ID: {self.codice_id})")


class Dottore(Persona):
    def __init__(self, nome, cognome, eta,
                 specializzazione, matricola, reparto):

        super().__init__(nome, cognome, eta)

        self.specializzazione = specializzazione
        self.matricola = matricola
        self.reparto = reparto
        self.pazienti = []

    def aggiungi_paziente(self, paziente):
        self.pazienti.append(paziente)

    def mostra_pazienti(self):
        print(f"Pazienti del dottor {self.cognome}:")

        for paziente in self.pazienti:
            print("-", paziente)

    def __str__(self):
        return (f"Dottore: {self.nome} {self.cognome} "
                f"({self.specializzazione})")


p1 = Paziente(
    "Mario",
    "Rossi",
    45,
    "P001",
    "A+",
    ["Diabete"],
    ["Penicillina"]
)

p2 = Paziente(
    "Anna",
    "Verdi",
    30,
    "P002",
    "0-",
    ["Asma"],
    []
)

d1 = Dottore(
    "Luigi",
    "Bianchi",
    50,
    "Cardiologia",
    "D101",
    "Cardiologia"
)

d1.aggiungi_paziente(p1)
d1.aggiungi_paziente(p2)

print(d1)
d1.mostra_pazienti()