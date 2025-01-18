import numpy as np

def get_normal_distribution_quantity(expectation_value=16000, standard_deviation=10000, minimum=0, maximum=100000) -> int:
    """
    Gibt einen Zufallswert x zurück, basierend auf einer abgeschnittenen Normalverteilung,
    die nur Werte x >= minimum und x <= maximum berücksichtigt
    
    Parameters:
        expectation_value: Erwartungswert µ der Normalverteilung
        standard_deviation: Standardabweichung σ der Normalverteilung
        minimum: Minimalwert den x nicht unterschreiten kann
        maximum: Maximalwert den x nicht überschreiten kann

    Returns:
        int: Ein Zufallswert x, gerundet auf die nächste ganze Zahl, immer >= minimum und <= maximum.
    """
    while True:
        # Generiere einen Wert basierend auf der Normalverteilung
        value = np.random.normal(expectation_value, standard_deviation)
        
        if value <= maximum:
            return max(minimum, round(value))


def test():
    sum = 0
    frequency = 30
    print("\n\nTesting", frequency, "times")

    for _ in range(frequency):
        random = get_normal_distribution_quantity()
        sum += random

    print("sum", sum, "avg", round(sum / frequency, 2), "\n\n")


def generate_drink_demands():
    sum = 0
    frequency = 75

    for _ in range(frequency):
        random = get_normal_distribution_quantity()
        sum += random
        print(str(random) + ",")

    print("sum", sum, "avg", round(sum / frequency, 2), "\n\n")


def generate_other_demands():
    sum = 0
    frequency = 75

    for _ in range(frequency):
        random = get_normal_distribution_quantity(65000, 20000, 40000, 90000)
        sum += random
        print(str(random) + ",")

    print("sum", sum, "avg", round(sum / frequency, 2), "\n\n")


if __name__ == '__main__':
    test()
