from graph_utility import create_fully_connected_graph
from ant_colony_optimization import ACO
from shortest_cycle import ShortestCycle
import sys

"""
This program is designed for the users to simply test the ACO algorithm and compare the output
with the shortest cycle.

Because the output given by ACO is not guaranteed to be the shortest cycle, it is meaningless
to write testing cases. I did a very detailed analysis for ACO algorithm in the Empirical Analysis
section. You can take that part as the algorithm testing.
"""

def main(option, number_of_times):
    files = ["5_vertices.txt", "10_vertices.txt", "13_vertices.txt"]
    create_fully_connected_graph(files[option], 100)
    ant = ACO("out.txt", 0.25, 40.0)
    naive = ShortestCycle("out.txt")

    naive.shortest_cycle()

    for _ in range(number_of_times):
        ant.go_ants(naive.shortestCycle[0], 1)

    print("Naive", naive.shortestCycle, naive.minDistance)
    print("ACO", ant.bestRoute, ant.minDistance)
    print("margin: {:.1f}%".format(((ant.minDistance - naive.minDistance) / naive.minDistance) * 100))

if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or 0 > int(sys.argv[1]) > 2:
        print("Usage: python3 tests.py [option] [number_of_time]")
        print("       option -> 0: 5 vertices, 1: 10 vertices, 2: 13 vertices")
        print("       number_of_time -> the number of time to run go_ant() function")
    else:
        main(int(sys.argv[1]), int(sys.argv[2]))
