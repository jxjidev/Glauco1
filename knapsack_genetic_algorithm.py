import random
import numpy as np
import time

# Função para inicializar a população
def initialize_population(pop_size, n_items):
    return [np.random.randint(0, 2, n_items).tolist() for _ in range(pop_size)]

# Função de aptidão (fitness)
def fitness(solution, weights, values, capacity):
    total_weight = sum(w * s for w, s in zip(weights, solution))
    total_value = sum(v * s for v, s in zip(values, solution))
    
    # Penalizar soluções que excedem a capacidade
    if total_weight > capacity:
        return -total_weight  # Penalização proporcional ao excesso
    return total_value

# Seleção por torneio
def tournament_selection(population, fitnesses, tournament_size):
    tournament = random.sample(range(len(population)), tournament_size)
    tournament_fitnesses = [fitnesses[i] for i in tournament]
    winner_idx = tournament[np.argmax(tournament_fitnesses)]
    return population[winner_idx]

# Crossover de dois pontos
def crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1, len(parent1) - 1)
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

# Mutação
def mutate(solution, mutation_rate):
    return [1 - s if random.random() < mutation_rate else s for s in solution]

# Algoritmo Genético
def genetic_algorithm(weights, values, capacity, pop_size=100, generations=100, mutation_rate=0.01, tournament_size=3):
    n_items = len(weights)
    population = initialize_population(pop_size, n_items)
    
    for gen in range(generations):
        # Avaliar aptidão de toda a população
        fitnesses = [fitness(ind, weights, values, capacity) for ind in population]
        
        # Criar nova população
        new_population = []
        
        # Elitismo: manter o melhor indivíduo
        best_idx = np.argmax(fitnesses)
        new_population.append(population[best_idx])
        
        # Gerar o restante da população
        while len(new_population) < pop_size:
            # Seleção
            parent1 = tournament_selection(population, fitnesses, tournament_size)
            parent2 = tournament_selection(population, fitnesses, tournament_size)
            
            # Crossover
            child1, child2 = crossover(parent1, parent2)
            
            # Mutação
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            new_population.extend([child1, child2])
        
        population = new_population[:pop_size]
    
    # Encontrar a melhor solução
    fitnesses = [fitness(ind, weights, values, capacity) for ind in population]
    best_idx = np.argmax(fitnesses)
    return population[best_idx], fitnesses[best_idx]

# Função para executar testes
def run_tests():
    # Conjunto de teste pequeno
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    
    print("Teste com conjunto pequeno:")
    start_time = time.time()
    best_solution, best_value = genetic_algorithm(weights, values, capacity)
    end_time = time.time()
    
    print(f"Melhor solução: {best_solution}")
    print(f"Valor total: {best_value}")
    print(f"Peso total: {sum(w * s for w, s in zip(weights, best_solution))}")
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos\n")
    
    # Conjunto de teste grande
    np.random.seed(42)
    n_items_large = 1000
    weights_large = np.random.randint(1, 100, n_items_large).tolist()
    values_large = np.random.randint(1, 100, n_items_large).tolist()
    capacity_large = 5000
    
    print("Teste com conjunto grande (1000 itens):")
    start_time = time.time()
    best_solution, best_value = genetic_algorithm(weights_large, values_large, capacity_large)
    end_time = time.time()
    
    print(f"Valor total: {best_value}")
    print(f"Peso total: {sum(w * s for w, s in zip(weights_large, best_solution))}")
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")

# Executar os testes
if __name__ == "__main__":
    run_tests()