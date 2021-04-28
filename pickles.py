import pickle

class Animal:

    def __init__(self,especie, origen,alimentacion):
        self.especie = especie
        self.origen = origen
        self.alimentacion = alimentacion

    def __repr__(self):
        return f"{self.especie} {self.alimentacion}"

animales = []
# for i in range(50):
#     a = Animal("Perro","Todo el mundo",str(i))
#     animales.append(a)
#
# with open("animales.txt", "wb") as file:
#     pickle.dump(animales,file)

with open("animales.txt", 'rb') as file:
    b = pickle.load(file)
    print(b)