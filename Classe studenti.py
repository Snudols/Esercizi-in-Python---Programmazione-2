class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valore):
        if valore == "":
            print("Nome non valido")
            self._nome = "Sconosciuto"
        else:
            self._nome = valore

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, valore):
        if valore < 0:
            print("Età non valida")
            self._eta = 0
        else:
            self._eta = valore

    def saluto(self):
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni")


# --- CLASSE FIGLIA ---

class StudenteITS(Studente):
    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)
        self.corso = corso

    def saluto(self):
        super().saluto() 
        print(f"Sto studiando nel corso di: {self.corso}")


s = StudenteITS("Giulia", 28, "Cyber Security")
s.saluto()