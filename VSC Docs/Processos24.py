class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("AU!,AU!")
class Gato(Animal):
    def fazer_som(self):
        print ("MIAU! ")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.fazer_som()