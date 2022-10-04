class Pet:
    def __init__(self, breed, color, species, name,):
        self.breed =breed
        self.color=color
        self.species=species
        self.name = name
def main():
    breed =input("what breed is your pet ")
    color =input('what color is your pet ')
    species = input('what is the species of your pet ')
    name =input('whagt is you pets name ')
    pet1=Pet(breed,color,species,name)
    print(f"{pet1.name} is a {pet1.species} and they are a {pet1.color} {pet1.breed}")
if __name__=="__main__":
    main()