import numpy as np

def rebel_algorithm(initial_belief, actions, observations, iterations):
    """
    Prosty algorytm REBEL: rekurencyjne uczenie się przekonań na podstawie działań i obserwacji.

    Parameters:
        initial_belief (list): Początkowe przekonania (dystrybucja prawdopodobieństwa).
        actions (list): Lista możliwych działań.
        observations (list): Lista możliwych obserwacji.
        iterations (int): Liczba iteracji algorytmu.

    Returns:
        belief_history (list): Historia aktualizacji przekonań.
    """
    # Zainicjuj przekonania
    belief = np.array(initial_belief)
    belief_history = [belief.copy()]

    for i in range(iterations):
        print(f"Iteracja {i+1}")

        # Wybierz działanie na podstawie przekonań (np. eksploracyjnie lub eksploatacyjnie)
        action = np.random.choice(actions)
        print(f"  Wybrane działanie: {action}")

        # Symuluj obserwację na podstawie działania
        observation = np.random.choice(observations)
        print(f"  Otrzymana obserwacja: {observation}")

        # Zaktualizuj przekonania na podstawie akcji i obserwacji
        likelihood = np.random.uniform(0.1, 1, size=len(belief))  # Losowe prawdopodobieństwo
        belief = belief * likelihood
        belief /= belief.sum()  # Normalizacja przekonań

        # Zapisz historię przekonań
        belief_history.append(belief.copy())
        print(f"  Zaktualizowane przekonania: {belief}")

    return belief_history

# Przykład użycia
initial_belief = [0.5, 0.3, 0.2]  # Początkowe przekonania
actions = ["akcja1", "akcja2", "akcja3"]
observations = ["obserwacja1", "obserwacja2", "obserwacja3"]
iterations = 5

belief_history = rebel_algorithm(initial_belief, actions, observations, iterations)

# Wyświetl historię przekonań
print("\nHistoria przekonań:")
for i, belief in enumerate(belief_history):
    print(f"Iteracja {i}: {belief}")
