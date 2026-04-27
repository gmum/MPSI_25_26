import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ==========================================
# 1. BAZOWE FUNKCJE ALGORYTMU
# ==========================================
def objective_function(x):
    e = np.e
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * x**2)) - \
           np.exp(0.5 * np.cos(2 * np.pi * x)) + e + 20.0

def initialize_population(pop_size, bounds):
    return np.random.uniform(bounds[0], bounds[1], pop_size)

def tournament_selection(population, fitnesses, k=3):
    indices = np.random.choice(len(population), size=k, replace=False)
    best_idx = indices[np.argmin(fitnesses[indices])]
    return population[best_idx]

def crossover(parent1, parent2):
    return 0.5 * parent1 + 0.5 * parent2

def mutate(individual, mutation_rate, sigma, bounds):
    if np.random.rand() < mutation_rate:
        individual += np.random.normal(0, sigma)
        individual = np.clip(individual, bounds[0], bounds[1])
    return individual

# ==========================================
# 2. KONFIGURACJA EKSPERYMENTU
# ==========================================
BOUNDS = (-32.768, 32.768)
POP_SIZE = 10
MUTATION_RATE = 0.5
SIGMA = 5.0
GENERATIONS = 100

# Inicjalizacja pierwszej populacji
population = initialize_population(POP_SIZE, BOUNDS)

# ==========================================
# 3. PRZYGOTOWANIE WYKRESU DO ANIMACJI
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))
x_vals = np.linspace(BOUNDS[0], BOUNDS[1], 1000) 
y_vals = objective_function(x_vals)

ax.plot(x_vals, y_vals, label="Funkcja celu f(x)", color='blue', alpha=0.5)

scat = ax.scatter([], [], color='red', zorder=5, label="Populacja (Rozwiązania)")
best_pt, = ax.plot([], [], 'y*', markersize=15, markeredgecolor='black', zorder=6, label="Najlepszy (Elita)")

ax.set_xlim(BOUNDS[0], BOUNDS[1])
ax.set_ylim(-1, 22)


ax.legend(loc="upper right", shadow=True, fancybox=True)
ax.grid(True, linestyle='--', alpha=0.6)

# ==========================================
# 4. LOGIKA POJEDYNCZEJ KLATKI
# ==========================================
def update(frame):
    global population
    
    # 1. Ocena populacji
    fitnesses = objective_function(population)
    
    # Znalezienie lidera
    best_idx = np.argmin(fitnesses)
    best_x = population[best_idx]
    best_y = fitnesses[best_idx]
    
    offsets = np.column_stack((population, fitnesses))
    scat.set_offsets(offsets)
    best_pt.set_data([best_x], [best_y])
    
    ax.set_title(f"Pokolenie: {frame} | Best x: {best_x:.4f} | Best f(x): {best_y:.4f}")
    
    # 2. Budowa nowego pokolenia
    if frame < GENERATIONS - 1:
        new_population = [best_x] # Elitaryzm
        
        while len(new_population) < POP_SIZE:
            # Selekcja
            p1 = tournament_selection(population, fitnesses, k=3)
            p2 = tournament_selection(population, fitnesses, k=3)
            
            # Krzyżowanie
            child = crossover(p1, p2)
            
            # Mutacja
            child = mutate(child, MUTATION_RATE, SIGMA, BOUNDS)
            
            new_population.append(child)
            
        population = np.array(new_population)
        
    return scat, best_pt

# ==========================================
# 5. URUCHOMIENIE ANIMACJI
# ==========================================
print("Uruchamiam animację w nowym oknie...")

ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=GENERATIONS, 
    interval=150,
    blit=False,
    repeat=False
)

plt.show()