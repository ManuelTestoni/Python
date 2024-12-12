import pickle

# Definizione della classe con __repr__
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __repr__(self):
        return f"Persona(nome='{self.nome}', eta={self.eta})"

# Creazione di un oggetto della classe
persona = Persona("Alice", 30)

# Salvataggio dell'oggetto su file
with open("persona.pkl", "wb") as file:
    pickle.dump(persona, file)

print("Oggetto salvato su file.")

# Caricamento dell'oggetto dal file
with open("persona.pkl", "rb") as file:
    persona_caricata = pickle.load(file)

print("Oggetto caricato dal file:")
print(persona_caricata)  # Mostrerà la rappresentazione leggibile grazie a __repr__
