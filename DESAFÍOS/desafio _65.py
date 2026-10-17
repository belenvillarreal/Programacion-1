# Desafío 65: Polimorfismo con figuras geométricas

import math


class Figura:
    """Clase base para representar una figura geométrica."""

    def area(self):
        """Método que será sobrescrito por las subclases."""
        raise NotImplementedError(
            "Las subclases deben implementar el método area()."
        )


class Circulo(Figura):
    """Representa un círculo mediante su radio."""

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        """Calcula y devuelve el área del círculo."""
        return math.pi * self.radio ** 2


class Cuadrado(Figura):
    """Representa un cuadrado mediante la longitud de su lado."""

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.lado ** 2


def main():
    """Demuestra el uso del polimorfismo."""

    print("Desafío 65: Polimorfismo con figuras geométricas")
    print()

    # Crear objetos de diferentes subclases
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)

    # Guardar objetos diferentes en una misma lista
    figuras = [
        ("Círculo", circulo),
        ("Cuadrado", cuadrado)
    ]

    # Aplicar el mismo método a todos los objetos
    # sin comprobar de qué tipo de figura se trata
    for nombre, figura in figuras:
        print("Figura:", nombre)
        print("Área:", round(figura.area(), 2))
        print()


if __name__ == "__main__":
    main()