import os
from functools import partial
from random import randint, randrange, random, choices
from typing import List, Tuple, Callable
from collections import namedtuple
import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Genetic Algorithm Functions
Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])


def generate_genome(length: int) -> Genome:
    return [randint(0, 1) for _ in range(length)]


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


def selection_pair(population: Population, fitness_func: FitnessFunc) -> tuple[list[int], ...]:
    return tuple(choices(
        population,
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


def read_things_from_file(file_path: str) -> List[Thing]:
    things = []
    with open(file_path, "r") as file:
        for line in file:
            name, value, weight = line.strip().split(',')
            things.append(Thing(name, int(value), int(weight)))
    return things


# Ant Colony Optimization Functions
def data_set(num: int) -> List[List[int]]:
    data_dir = 'Z:\ALL\CODE ALL\PYTHON ALL\python\ACO-AS-main\data'
    data = []
    for n in os.listdir(data_dir):
        subdir_path = os.path.join(data_dir, n)
        if os.path.isdir(subdir_path):
            for m in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, m)
                with open(file_path) as f:
                    lines = [int(line.strip()) for line in f]
                    data.append(lines)
    return data[num * 4:(num * 4) + 4]


def heuristic_info(weight, profit, capacity):
    return capacity / weight


def probability_selector(available_solutions, probabilities):
    return available_solutions[np.argmax(probabilities)]


def create_aco_table(average_ants, best_ants, weight_graph):
    data = {
        'Iteration': range(1, len(average_ants) + 1),
        'Average Ants Profit': average_ants,
        'Best Ants Profit': best_ants,
        'Weight': weight_graph
    }
    df = pd.DataFrame(data)
    return df


def main():
    print("Which algorithm do you want to use?")
    print("1. Genetic Algorithm")
    print("2. Ant Colony Optimization")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        things = read_things_from_file('Z:\ALL\CODE ALL\PYTHON ALL\python\ACO-AS-main\objeler.txt')
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

    elif choice == '2':
        dataset_nr = 4
        X = data_set(dataset_nr)
        capacity_org, weight, profit, solution = X[0][0], X[3], X[1], X[2]

        alfa = 1
        beta = 0.02
        ro = 0.05
        ant_count = 200

        pheromone_track = 0.1 * np.ones(len(weight))
        best_ant = [[0], 0]
        best_ants = [[], []]
        global_best_ant = [[0], 0]
        average_ants_graph = []
        weight_graph = []

        for iter in range(150):
            ants = [[], []]
            for ant_num in range(ant_count):
                availability = [True] * len(weight)
                S = []
                profit_sum = 0
                capacity = capacity_org
                while (capacity > 0):
                    chosen_obj = [((pheromone_track[item]) ** alfa) * (
                            (heuristic_info(weight[item], profit[item], capacity_org)) ** beta) if availability[
                                                                                                       item] == True else 0
                                  for item in range(len(weight))]
                    chosen_objects_sum = np.sum(chosen_obj)
                    p_j = [chosen_obj[item] / chosen_objects_sum for item in range(len(weight))]
                    o_j = probability_selector(weight, p_j)
                    taken_object_idx = weight.index(o_j)
                    S.append(taken_object_idx)
                    availability[taken_object_idx] = False

                    capacity -= weight[taken_object_idx]
                    profit_sum += profit[taken_object_idx]

                    for x in range(0, len(availability)):
                        if weight[x] > capacity:
                            availability[x] = False

                    if not any(availability): break

                ants[0].append(S)
                ants[1].append(profit_sum)

            avg_ants = sum(ants[1]) / len(ants[1])
            average_ants_graph.append(avg_ants)

            best_ant_idx = int(np.argmax(ants[1]))
            best_ant[0], best_ant[1] = ants[0][best_ant_idx], ants[1][best_ant_idx]

            best_ants[0].append(best_ant[0])
            best_ants[1].append(best_ant[1])

            global_best_ant_idx = int(np.argmax(best_ants[1]))
            global_best_ant[0], global_best_ant[1] = best_ants[0][global_best_ant_idx], best_ants[1][
                global_best_ant_idx]

            delta_tau = np.zeros(len(profit))
            for n in global_best_ant[0]:
                delta_tau[n] = 1 / (1 + ((max(profit) - profit[n]) / max(profit)))

            pheromone_track *= 1 - ro
            pheromone_track += delta_tau

            weight_it = np.sum([weight[n] for n in global_best_ant[0]])
            weight_graph.append(weight_it)

        # create ACO table
        df_aco = create_aco_table(average_ants_graph, best_ants[1], weight_graph)
        print("Ant Colony Optimization Table:")
        print(df_aco)

        fig, axs = plt.subplots(2, 1, figsize=(10, 12))
        axs[0].plot(average_ants_graph, label='Average Ants Profit', color='green')
        axs[0].plot(best_ants[1], label='Best Ants Profit')
        axs[0].set_title('Profit')
        axs[0].set_xlabel('Iteration')
        axs[0].set_ylabel('Profit')
        axs[0].legend()

        axs[1].plot(weight_graph, label='Weight')
        axs[1].axhline(y=capacity_org, color='r', linestyle='--', label='Capacity')
        axs[1].set_title('Weight')
        axs[1].set_xlabel('Iteration')
        axs[1].set_ylabel('Weight')
        axs[1].legend()

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    main()
