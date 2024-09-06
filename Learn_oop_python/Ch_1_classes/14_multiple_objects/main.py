def main():
    aragorn_brawler = Brawler(4,4,'Aragorn')
    gimli_brawler = Brawler(2,7,"Gimli")
    legolas_brawler = Brawler(7,7,'Legolas')
    frodo_brawler = Brawler(3,2,"Frodo")
    fight(aragorn_brawler,gimli_brawler)
    fight(legolas_brawler,frodo_brawler)




class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()

