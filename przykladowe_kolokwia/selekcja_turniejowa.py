import numpy as np

def selekcja_turniejowa(fitness, N, k):
    M = fitness.shape[0]
    turnieje_indeksy = np.random.randint(0, M, size=(N,k))
    turnieje_fitness = fitness[turnieje_indeksy]
    # print(f"Turnieje_fitness: {turnieje_fitness.shape}")

    najlepsi_lokalnie = np.argmax(turnieje_fitness, axis=1)

    # print(f"Fitness shape: {fitness.shape}")
    print(f"Turnieje_indeksy: {turnieje_indeksy}")
    print(f"Najlepsi_lokalnie: {najlepsi_lokalnie}")

    odpowiedz = turnieje_indeksy[np.arange(N), najlepsi_lokalnie]
    print(f"Finalna odpowiedź: {odpowiedz}")

    return odpowiedz

if __name__ == "__main__":
    fitness = np.array([10, 40, 20, 50, 80, 30])
    N = 6
    k = 2

    selekcja_turniejowa(fitness, N, k)