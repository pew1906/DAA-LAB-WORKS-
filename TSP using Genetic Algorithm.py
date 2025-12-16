# Assignment 06: Solving Traveling Salesman Problem Using Genetic Algorithm
import numpy as np
import matplotlib.pyplot as plt
import random

# Distance calculation
def distance(route, cities):
    return sum(np.linalg.norm(np.array(cities[route[i]]) - np.array(cities[route[i - 1]]))
               for i in range(len(route)))

# Create initial population
def create_population(pop_size, city_count):
    return [random.sample(range(city_count), city_count) for _ in range(pop_size)]

# Fitness function
def fitness(population, cities):
    return [1 / distance(route, cities) for route in population]

# Selection (tournament selection)
def selection(population, fitness_scores):
    selected = []
    for _ in range(len(population)):
        i, j = random.sample(range(len(population)), 2)
        winner = population[i] if fitness_scores[i] > fitness_scores[j] else population[j]
        selected.append(winner)
    return selected

# Crossover (ordered crossover)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    fill = [city for city in parent2 if city not in child]
    idx = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child

# Mutation (swap mutation)
def mutate(route, mutation_rate=0.01):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Main Genetic Algorithm
def genetic_algorithm(cities, pop_size=100, generations=500):
    population = create_population(pop_size, len(cities))
    best_route = None
    best_distance = float('inf')

    for gen in range(generations):
        fitness_scores = fitness(population, cities)
        new_population = []

        selected = selection(population, fitness_scores)
        for i in range(0, pop_size, 2):
            parent1, parent2 = selected[i], selected[(i + 1) % pop_size]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population
        gen_best = min(population, key=lambda r: distance(r, cities))
        gen_dist = distance(gen_best, cities)

        if gen_dist < best_distance:
            best_route, best_distance = gen_best, gen_dist

    return best_route, best_distance

# Example run
if __name__ == "__main__":
    num_cities = 10
    cities = np.random.rand(num_cities, 2) * 100

    best_route, best_distance = genetic_algorithm(cities)
    print("Best route:", best_route)
    print("Best distance:", best_distance)

    # Visualization
    route_coords = [cities[i] for i in best_route] + [cities[best_route[0]]]
    plt.plot([x for x, y in route_coords], [y for x, y in route_coords], marker='o')
    for i, (x, y) in enumerate(cities):
        plt.text(x, y, str(i))
    plt.title("Best TSP Route using Genetic Algorithm")
    plt.show()
