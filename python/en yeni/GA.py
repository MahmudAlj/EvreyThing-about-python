from random import choices, randint, randrange, random
from typing import List, Tuple, Callable
from collections import namedtuple
from functools import partial
import time

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

things = [
    Thing('obje1', 30, 159),
    Thing('obje2', 33, 500),
    Thing('obje3', 120, 3430),
    Thing('obje4', 43, 540),
    Thing('obje5', 30, 330),
    Thing('obje6', 54, 545),
    Thing('obje7', 60, 800),
    Thing('obje8', 90,2000),
    Thing('obje9', 70, 1800),
    Thing('obje10', 150, 4500)
]

def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)


def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: List[Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same length")

    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

        if weight > weight_limit:
            return 0

    return value


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Tuple[Genome, Genome]:
    return tuple(choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    ))


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of the same length")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome


def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 100
) -> Tuple[Population, int]:
    population = populate_func()

    for generation in range(generation_limit):
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

            next_generation = sorted(
                next_generation,
                key=lambda genome: fitness_func(genome),
                reverse=True
)
    return population, generation


def genome_to_things(genome: Genome, things: List[Thing]) -> List[Thing]:
    return [thing for i, thing in enumerate(things) if genome[i] == 1]


start = time.time()
population, generation = run_evolution(
    populate_func=partial(
        generate_population, size=10, genome_length=len(things)
    ),
    fitness_func=partial(
        fitness, things=things, weight_limit=5000
    ),
    fitness_limit=1100,
    generation_limit=100
)
end = time.time()

print(f"Number of generations: {generation}")
print(f"Time: {end - start}s")
print(f"Best solution: {genome_to_things(population[0], things)}")