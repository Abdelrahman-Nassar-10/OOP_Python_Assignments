from abc import ABC, abstractmethod
from typing import List

class VacationPackage(ABC):
    def __init__(self, destination: str, price: float) -> None:
        self.destination = destination
        self.price = price

    @abstractmethod
    def display_details(self) -> None:
        ...

class AdventurePackage(VacationPackage):
    def __init__(self, destination: str, price: float, activities: List[str]) -> None:
        super().__init__(destination, price)
        self.activities = activities

    def display_details(self) -> None:
        print(f"Destination: {self.destination}")
        print(f"Price: ${self.price:.0f}")
        print("Activities: " + ", ".join(self.activities))

class RelaxationPackage(VacationPackage):
    def __init__(self, destination: str, price: float, spa_services: List[str]) -> None:
        super().__init__(destination, price)
        self.spa_services = spa_services

    def display_details(self) -> None:
        print(f"Destination: {self.destination}")
        print(f"Price: ${self.price:.0f}")
        print("Spa Services: " + ", ".join(self.spa_services))

if __name__ == "__main__":
    adventure = AdventurePackage("Turkey", 2500, ["Hiking", "Rafting"])
    relaxation = RelaxationPackage("Hurghada", 3000, ["Massage", "Yoga"])

    adventure.display_details()
    print("---")
    relaxation.display_details()
