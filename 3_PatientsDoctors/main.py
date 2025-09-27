from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_details(self) -> str:
        ...

class Patient(Person):
    def __init__(self, name: str, age: int, medical_history: str) -> None:
        super().__init__(name, age)
        self.medical_history = medical_history

    def get_details(self) -> str:
        return f"Patient Name: {self.name}, Age: {self.age}, Medical History: {self.medical_history}"

class Doctor(Person):
    def __init__(self, name: str, age: int, specialty: str) -> None:
        super().__init__(name, age)
        self.specialty = specialty

    def get_details(self) -> str:
        return f"Doctor Name: {self.name}, Age: {self.age}, Specialty: {self.specialty}"

def display_person_details(person: Person) -> None:
    print(person.get_details())

if __name__ == "__main__":
    patient = Patient(name="Omar", age=30, medical_history="Hypertension")
    doctor = Doctor(name="Dr. Hesham", age=45, specialty="Cardiology")

    display_person_details(patient)
    display_person_details(doctor)
