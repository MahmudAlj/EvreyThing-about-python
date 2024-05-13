import os
import numpy as np
from random import choices
from matplotlib import pyplot as plt

def data_set(num):
    dir = 'data/'
    data = []
    for n in os.listdir(dir):
        for m in os.listdir(dir + str(n)):
            with open(dir + n + '/' + m) as f:
                lines = [int(line.strip()) for line in f]
                data.append(lines)
    return data[num * 4:(num * 4) + 4]

def heuristic_info(weight, profit, capacity):
    # return profit/(weight/capacity) #profit/(weight**2)
    return capacity / weight


def probability_selector(available_solutions, probabilities):
    selected_item = choices(available_solutions, probabilities)
    return selected_item[0]


def main():
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
    avg_ants = []
    graph = []
    weight_graph = []
    average_ants_graph = []

    for iter in range(150):
        ants = [[], []]
        for ant_num in range(ant_count):
            availability = [True] * len(weight)
            S = []
            profit = 0
            capacity = capacity_org
            while (capacity >= 0):
                chosen_obj = [((pheromone_track[item]) ** alfa) * (
                            (heuristic_info(weight[item], profit[item], capacity_org)) ** beta) if availability[item] == True else 0
                              for item in range(len(weight))]
                chosen_objects_sum = np.sum(chosen_obj)
                p_j = [chosen_obj[item] / chosen_objects_sum for item in range(len(weight))]
                o_j = probability_selector(weight, p_j)
                taken_object_idx = weight.index(o_j)
                S.append(taken_object_idx)
                availability[taken_object_idx] = False

                capacity -= weight[taken_object_idx]
                profit += profit[taken_object_idx]

                for x in range(0, len(availability)):
                    if weight[x] > capacity:
                        availability[x] = False

                if not any(availability): break

            ants[0].append(S)
            ants[1].append(profit)
            avg_ants = sum(ants[1]) / len(ants[1])

            if ants[1][ant_num] >= ants[1][int(np.argmax(ants[1]))]:
                best_ant[0], best_ant[1] = ants[0][ant_num], ants[1][ant_num]
            else:
                pass

        best_ants[0].append(best_ant[0])
        best_ants[1].append(best_ant[1])
        average_ants_graph.append(avg_ants)

        if best_ants[1][iter] >= best_ants[1][int(np.argmax(best_ants[1]))]:
            global_best_ant[0], global_best_ant[1] = best_ants[0][iter], best_ants[1][iter]
        else:
            pass

        delta_tau = np.zeros(len(profit))
        for n in global_best_ant[0]:
            delta_tau[n] = 1 / (1 + ((max(profit) - profit[n]) / max(profit)))

        pheromone_track *= 1 - ro
        pheromone_track += delta_tau

        waga_it = np.sum([weight[n] for n in global_best_ant[0]])
        print(global_best_ant, waga_it)

        graph.append(global_best_ant[1])
        weight_graph.append(waga_it)

    fig, axs = plt.subplots(1, 3, figsize=(18, 4))
    axs[0].plot(graph, label='Best ant profit')
    axs[0].plot(average_ants_graph, label='Average ants profit', color='green')
    axs[0].legend(loc="lower right")
    axs[0].set_title('Profit')
    axs[0].set_xlabel('Iteration')

    axs[1].plot(weight_graph)
    axs[1].axhline(y=capacity_org, color='r', linestyle='-')
    axs[1].set_title('Weight')
    axs[1].set_xlabel('Iteration')

    axs[2].bar((list(range(0, len(solution)))), solution, color='cyan')
    axs[2].set_title('Solution')
    for xc in global_best_ant[0]:
        axs[2].axvline(x=xc, color='navy')
    axs[2].set_xlabel('Selected item')
    axs[2].set_yticklabels([])

    plt.show()


if __name__ == '__main__':
    main()