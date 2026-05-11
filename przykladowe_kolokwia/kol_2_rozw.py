from typing import List
import numpy as np

def selekcja_ruletkowa(fitness: List, N: int) -> np.ndarray:
    if N > len(fitness):
        N = len(fitness)

    fitness = np.array(fitness)
    probs = fitness / np.sum(fitness, axis=0)

    dystrybuanta = np.cumsum(probs)
   

    wylosowane_liczby = np.random.rand(N)
    indeksy = np.searchsorted(dystrybuanta, wylosowane_liczby)

    return indeksy


if __name__ == '__main__':
    fitness = [10, 30, 20, 5, 35]
    N = 3
    print(selekcja_ruletkowa(fitness, N))