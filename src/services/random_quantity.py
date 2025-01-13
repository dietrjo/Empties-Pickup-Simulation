import numpy as np

def get_normal_distribution_quantity(expectation_value=16000, standard_deviation=10000, maximum=100000) -> int:
    """
    Gibt einen Zufallswert x zurück, basierend auf einer abgeschnittenen Normalverteilung,
    die nur Werte x >= 0 und x <= maximum berücksichtigt
    
    Parameters:
        expectation_value: Erwartungswert µ der Normalverteilung
        standard_deviation: Standardabweichung σ der Normalverteilung
        maximum: Maximalwert den x nicht überschreiten kann

    Returns:
        int: Ein Zufallswert x, gerundet auf die nächste ganze Zahl, immer >= 0 und <= maximum.
    """
    while True:
        # Generiere einen Wert basierend auf der Normalverteilung
        value = np.random.normal(expectation_value, standard_deviation)
        
        if value <= maximum:
            return max(0, round(value))


if __name__ == '__main__':
    sum = 0
    frequency = 30
    print("\n\nTesting", frequency, "times")
    
    for _ in range(frequency):
        random = get_normal_distribution_quantity()
        sum += random
    
    print("sum", sum, "avg", round(sum/frequency, 2),"\n\n")