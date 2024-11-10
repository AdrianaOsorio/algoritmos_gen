# Algoritmos Gen

Una biblioteca en Python para implementar algoritmos genéticos personalizables, diseñada para ser flexible y fácil de usar.

## Instalación

```bash
pip install algoritmos_gen

#Ejemplo de uso 

from algoritmos_gen import GeneticAlgorithm
from algoritmos_gen.utils import initialize_population, calculate_population_fitness

# Definir la función de aptitud
def fitness(individual):
    return sum(individual)

# Crear la población inicial utilizando utils
initial_population = initialize_population(size=20, gene_length=10)

# Calcular la aptitud de la población inicial (opcional)
population_fitness = calculate_population_fitness(initial_population, fitness)

# Inicializar el algoritmo genético
ga = GeneticAlgorithm(
    population=initial_population,
    fitness_function=fitness,
    crossover_prob=0.8,
    mutation_prob=0.01,
    crossover_type="single_point",
    mutation_type="flip",
    selection_type="tournament",
    elitism=True
)

# Ejecutar el algoritmo genético
ga.run(generations=50)

