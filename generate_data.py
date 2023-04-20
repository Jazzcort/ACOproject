import subprocess
import time
import sys
import math
from shortest_cycle import ShortestCycle
from ant_colony_optimization import ACO
from graph_utility import create_fully_connected_graph

EXEC= [["python3", "shortest_cycle.py"], ["python3", "ant_colony_optimization.py"]]


def run_naive(file1, file2, file3, file4):
    pp = ShortestCycle("out.txt")
    start = time.time()
    pp.shortest_cycle()
    end = time.time()

    with open(file1, mode="w") as a_file1:
        a_file1.write("Naive " + str(pp.shortestCycle) + " " + str(pp.minDistance) + " " + "{:.2f}".format(end - start) + "\n")

    with open(file2, mode="w") as a_file2:
        a_file2.write("Naive " + str(pp.shortestCycle) + " " + str(pp.minDistance) + " " + "{:.2f}".format(end - start) + "\n")

    with open(file3, mode="w") as a_file3:
        a_file3.write("Naive " + str(pp.shortestCycle) + " " + str(pp.minDistance) + " " + "{:.2f}".format(end - start) + "\n")

    with open(file4, mode="w") as a_file4:
        a_file4.write("Naive " + str(pp.shortestCycle) + " " + str(pp.minDistance) + " " + "{:.2f}".format(end - start) + "\n")

    return pp.shortestCycle[0]

def run_ant(src, number_of_times, file):
    pp = ACO("out.txt", 0.25, 40.0)

    start = time.time()
    for _ in range(number_of_times):
        pp.go_ants(src, 1)
    end = time.time()

    with open(file, mode="a") as a_file:
        a_file.write("ACO " + str(pp.bestRoute) + " " + str(pp.minDistance) + " " + "{:.2f}".format(end - start) + "\n")


def main():
    # create_fully_connected_graph("5_vertices.txt", 100)
    # src = run_naive("5_vertices_run1000_01.csv", "5_vertices_run2000_01.csv", "5_vertices_run5000_01.csv", "5_vertices_run10000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "5_vertices_run1000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "5_vertices_run2000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "5_vertices_run5000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "5_vertices_run10000_01.csv")
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("5_vertices.txt", 100)
    # src = run_naive("5_vertices_run1000_02.csv", "5_vertices_run2000_02.csv", "5_vertices_run5000_02.csv", "5_vertices_run10000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "5_vertices_run1000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "5_vertices_run2000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "5_vertices_run5000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "5_vertices_run10000_02.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("5_vertices.txt", 100)
    # src = run_naive("5_vertices_run1000_03.csv", "5_vertices_run2000_03.csv", "5_vertices_run5000_03.csv", "5_vertices_run10000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "5_vertices_run1000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "5_vertices_run2000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "5_vertices_run5000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "5_vertices_run10000_03.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("10_vertices.txt", 100)
    # src = run_naive("10_vertices_run1000_01.csv", "10_vertices_run2000_01.csv", "10_vertices_run5000_01.csv", "10_vertices_run10000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "10_vertices_run1000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "10_vertices_run2000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "10_vertices_run5000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "10_vertices_run10000_01.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("10_vertices.txt", 100)
    # src = run_naive("10_vertices_run1000_02.csv", "10_vertices_run2000_02.csv", "10_vertices_run5000_02.csv", "10_vertices_run10000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "10_vertices_run1000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "10_vertices_run2000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "10_vertices_run5000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "10_vertices_run10000_02.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("10_vertices.txt", 100)
    # src = run_naive("10_vertices_run1000_03.csv", "10_vertices_run2000_03.csv", "10_vertices_run5000_03.csv", "10_vertices_run10000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "10_vertices_run1000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "10_vertices_run2000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "10_vertices_run5000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "10_vertices_run10000_03.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("13_vertices.txt", 100)
    # src = run_naive("13_vertices_run1000_01.csv", "13_vertices_run2000_01.csv", "13_vertices_run5000_01.csv", "13_vertices_run10000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "13_vertices_run1000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "13_vertices_run2000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "13_vertices_run5000_01.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "13_vertices_run10000_01.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("13_vertices.txt", 100)
    # src = run_naive("13_vertices_run1000_02.csv", "13_vertices_run2000_02.csv", "13_vertices_run5000_02.csv", "13_vertices_run10000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "13_vertices_run1000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "13_vertices_run2000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "13_vertices_run5000_02.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "13_vertices_run10000_02.csv")
    #
    # #------------------------------------------------------------
    #
    # create_fully_connected_graph("13_vertices.txt", 100)
    # src = run_naive("13_vertices_run1000_03.csv", "13_vertices_run2000_03.csv", "13_vertices_run5000_03.csv", "13_vertices_run10000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 1000, "13_vertices_run1000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 2000, "13_vertices_run2000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 5000, "13_vertices_run5000_03.csv")
    #
    # for _ in range(100):
    #     run_ant(src, 10000, "13_vertices_run10000_03.csv")

if __name__ == "__main__":
    main()
