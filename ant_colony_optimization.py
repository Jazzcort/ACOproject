from collections import defaultdict
from random import randint
import sys
class ACO:
    def __init__(self, filename, evaporateSpeed, pheromonePerAnt):
        self.adj_dict = self.load_file(filename)
        self.pheromone_dict = self.create_pheromone_dict()
        self.evaporateSpeed = evaporateSpeed
        self.pheromonePerAnt = pheromonePerAnt
        self.bestRoute = []
        self.minDistance = float("inf")

    def load_file(self, filename):
        adj_dict = defaultdict(lambda: defaultdict(float))
        try:
            with open(filename, mode="r") as r_file:
                for i in r_file:
                    tmp = i.strip("\n").split(" ")
                    adj_dict[tmp[0]][tmp[1]] = float(tmp[2])
                    adj_dict[tmp[1]][tmp[0]] = float(tmp[2])

        except FileNotFoundError:
            print(f"{self.filename} does not exist")
            return

        return adj_dict

    def create_pheromone_dict(self):
        pher_dict = defaultdict(lambda: defaultdict(float))
        for src in self.adj_dict:
            for dest in self.adj_dict[src]:
                pher_dict[src][dest] = 0.01

        return pher_dict

    def make_decision(self, possibility):
        candidates = list(possibility.keys())

        for ind, candidate in enumerate(candidates):
            if ind != 0:
                if ind == len(candidates) - 1:
                    possibility[candidate] = 1.0
                else:
                    possibility[candidate] += possibility[candidates[ind - 1]]

        rand = randint(0, 100000) / 100000
        for candidate in candidates:
            if rand <= possibility[candidate]:
                return candidate


    def create_possibility(self, src, forbiden):
        candidates = []

        for option in self.adj_dict[src]:
            if option in forbiden:
                continue
            else:
                candidates.append(option)

        factor = defaultdict(float)
        total = 0
        for candidate in candidates:
            factor[candidate] = self.pheromone_dict[src][candidate] * (1 / self.adj_dict[src][candidate])
            total += factor[candidate]

        possibility = defaultdict(float)

        for candidate in candidates:
            possibility[candidate] = (factor[candidate] / total)

        return possibility


    def go_ants(self, start, antSize):
        count_dict = defaultdict(int)

        for _ in range(antSize):
            visited = set([start])
            src = start

            while len(visited) < len(self.adj_dict):
                dest = self.make_decision(self.create_possibility(src, visited))
                count_dict[(src, dest)] += 1
                count_dict[(dest, src)] += 1
                visited.add(dest)
                src = dest

            count_dict[(start, dest)] += 1
            count_dict[(dest, start)] += 1

        updated = set()

        for i in self.pheromone_dict:
            for j in self.pheromone_dict[i]:
                if (i, j) not in updated:
                    self.update_pheromone(i, j, count_dict[(i, j)])
                    updated.add((i, j))
                    updated.add((j, i))

        self.update_best_route(start)



    def update_pheromone(self, src, dest, count):
        old = self.pheromone_dict[src][dest]
        n_pher = (old * (1 - self.evaporateSpeed)) + ((count * self.pheromonePerAnt) / self.adj_dict[src][dest])
        if n_pher < 0.01:
            n_pher = 0.01
        self.pheromone_dict[src][dest] = n_pher
        self.pheromone_dict[dest][src] = n_pher

    def update_best_route(self, start):
        visited = set()
        visited.add(start)
        src = start
        route = [start]

        while len(visited) < len(self.adj_dict):
            possibility = self.create_possibility(src, visited)
            choice = self.select_highest_possibility(possibility)
            route.append(choice)
            visited.add(choice)
            src = choice

        route.append(start)
        distance = self.distance(route)

        if distance < self.minDistance:
            self.minDistance = distance
            self.bestRoute = route[:]

    def select_highest_possibility(self, possibility):
        res = None
        p = 0

        for dest in possibility:
            if possibility[dest] > p:
                res = dest
                p = possibility[dest]

        return res

    def distance(self, route):
        res = 0
        for i in range(len(route) - 1):
            res += self.adj_dict[route[i]][route[i + 1]]

        return res


def main(start, number_of_times):
    pp = ACO("out.txt", 0.25, 40.0)

    for _ in range(int(number_of_times)):
        pp.go_ants(start, 1)

    # print((pp.bestRoute, pp.minDistance))

    return (pp.bestRoute, pp.minDistance)


if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print("Usage: python3 ant_colony_optimization.py [start] [number_of_times]")
        print("       start is the starting vertex of the shortest cycle")
        print("       number_of_times is the number of times this algorithm would run")
    else:
        main(sys.argv[1], sys.argv[2])
