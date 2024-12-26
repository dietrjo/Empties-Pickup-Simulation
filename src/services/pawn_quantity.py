import numpy as np

def get_pawn_quanity(expectation_value=16, standard_deviation=10) -> int:
    """
    Gibt einen Zufallswert x zurück, basierend auf einer abgeschnittenen Normalverteilung,
    die nur Werte x >= 0 berücksichtigt
    
    Parameters:
        expectation_value: Erwartungswert µ der Normalverteilung
        standard_deviation: Standardabweichung σ der Normalverteilung

    Returns:
        int: Ein Zufallswert x, gerundet auf die nächste ganze Zahl, immer >= 0.
    """
    while True:
        # Generiere einen Wert basierend auf der Normalverteilung
        value = np.random.normal(expectation_value, standard_deviation)
        
        # Wenn der Wert >= 0 ist, gib ihn zurück
        if value >= 0:
            return round(value)



if __name__ == '__main__':
    sum = 0
    frequency = 30
    print("\n\nTesting", frequency, "times")
    
    for _ in range(frequency):
        random = get_pawn_quanity()
        sum += random
    
    print("sum", sum, "avg", round(sum/frequency, 2),"\n\n")