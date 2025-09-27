from abc import ABC, abstractmethod

class TravelPackage(ABC):
    @abstractmethod
    def calculate_total_cost(self) -> float:
        ...

    @abstractmethod
    def display_package_cost(self) -> None:
        ...

class HotelPackage(TravelPackage):
    def __init__(self, nights: int, cost_per_night: int) -> None:
        self.nights = nights
        self.cost_per_night = cost_per_night

    def calculate_total_cost(self) -> float:
        return float(self.nights * self.cost_per_night)

    def display_package_cost(self) -> None:
        total = self.calculate_total_cost()
        print(f"Total Cost for Hotel package: ${total:.2f}")

class TourPackage(TravelPackage):
    def __init__(self, days: int, cost_per_day: int, discount: float = 0.10) -> None:
        self.days = days
        self.cost_per_day = cost_per_day
        self.discount = discount

    def calculate_total_cost(self) -> float:
        return float(self.days * self.cost_per_day)

    def display_package_cost(self) -> None:
        base = self.calculate_total_cost()
        final = base * (1 - self.discount)
        # Note the space before ':' to match the screenshot exactly
        print(f"Total Cost for Tour package After {int(self.discount*100)}% discount : ${final:.2f}")

if __name__ == "__main__":
    hotel_package = HotelPackage(nights=5, cost_per_night=200)
    tour_package = TourPackage(days=7, cost_per_day=100)

    hotel_package.display_package_cost()
    tour_package.display_package_cost()
