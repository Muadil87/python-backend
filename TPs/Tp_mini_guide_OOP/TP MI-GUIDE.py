from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def afficher_commande(self):
        print(f"  - {self.description()} : {self.cout():.2f}€")


class Cafe(Boisson):
    def cout(self):
        return 2.0

    def description(self):
        return "Cafe simple"


class The(Boisson):
    def cout(self):
        return 1.5

    def description(self):
        return "Black The"


class ChocolatChaud(Boisson):
    def cout(self):
        return 2.5

    def description(self):
        return "Chocolat Chaud"


class Decorator(Boisson):
    def __init__(self, boisson):
        self.boisson = boisson


class Lait(Decorator):
    def cout(self):
        return self.boisson.cout() + 0.5

    def description(self):
        return self.boisson.description() + ", Lait"


class Sucre(Decorator):
    def cout(self):
        return self.boisson.cout() + 0.2

    def description(self):
        return self.boisson.description() + ", Sucre"


class Caramel(Decorator):
    def cout(self):
        return self.boisson.cout() + 0.7

    def description(self):
        return self.boisson.description() + ", Caramel"


class CombinedBoisson(Boisson):
    def __init__(self, boisson1, boisson2):
        self.boisson1 = boisson1
        self.boisson2 = boisson2

    def cout(self):
        return self.boisson1.cout() + self.boisson2.cout()

    def description(self):
        return self.boisson1.description() + " + " + self.boisson2.description()

    def afficher_commande(self):
        print(f"  - {self.description()} : {self.cout():.2f}€")

    def __add__(self, other):
        if isinstance(other, Boisson):
            return CombinedBoisson(self, other)


def _boisson_add(self, other):
    if isinstance(other, Boisson):
        return CombinedBoisson(self, other)

Boisson.__add__ = _boisson_add


@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0


class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        print(f"=== Commande de {self.client.nom} ===")
        for b in self.boissons:
            print(f"  - {b.description()} : {b.cout():.2f}€")
        print(f"  TOTAL : {self.prix_total():.2f}€")


class CommandeSurPlace(Commande):
    def afficher(self):
        print("[ Sur place ]")
        super().afficher()


class CommandeEmporter(Commande):
    TAXE_EMBALLAGE = 0.10

    def prix_total(self):
        return super().prix_total() + len(self.boissons) * self.TAXE_EMBALLAGE

    def afficher(self):
        print("[ À emporter ]")
        super().afficher()
        print(f"  (taxe emballage : {len(self.boissons) * self.TAXE_EMBALLAGE:.2f}€ incluse)")


class Fidelite:
    def ajouter_points(self, client, montant):
        points_gagnes = int(montant)
        client.points_fidelite += points_gagnes
        print(f"  +{points_gagnes} points de fidélité -> Total : {client.points_fidelite} pts")


class CommandeFidele(Commande, Fidelite):
    def valider(self):
        total = self.prix_total()
        self.afficher()
        print("\n--- Validation de la commande ---")
        self.ajouter_points(self.client, total)


if __name__ == "__main__":

    boisson = Cafe()
    boisson = Lait(boisson)
    boisson = Sucre(boisson)
    boisson.afficher_commande()

    print()

    cafe_caramel = Caramel(Cafe())
    cafe_caramel.afficher_commande()

    print()

    menu = Cafe() + The()
    menu.afficher_commande()

    print()

    adil = Client(nom="Adil", numero=1)
    print(f"Client : {adil}\n")

    cmd_sur_place = CommandeSurPlace(adil)
    cmd_sur_place.ajouter_boisson(Lait(Cafe()))
    cmd_sur_place.ajouter_boisson(The())
    cmd_sur_place.afficher()

    print()

    cmd_emporter = CommandeEmporter(adil)
    cmd_emporter.ajouter_boisson(Caramel(Cafe()))
    cmd_emporter.afficher()

    print()

    souhaib = Client(nom="Souhaib", numero=2)
    cmd_fidele = CommandeFidele(souhaib)
    cmd_fidele.ajouter_boisson(Lait(Sucre(Cafe())))
    cmd_fidele.ajouter_boisson(ChocolatChaud())
    cmd_fidele.valider()
    print(f"\nClient après commande : {souhaib}")