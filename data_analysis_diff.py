"""
This function is used to calculate the margin between average output from ACO algorithm
and the shortest cycle.
"""
def calculate_differences(file):
    firstLine = True
    count = 0
    total = 0

    with open(file, mode="r") as r_file:
        for line in r_file:
            tmp = line.strip("\n").split(" ")
            if firstLine:
                correct = float(tmp[-2])
                firstLine = False
            else:
                total += float(tmp[-2])
                count += 1
    return ((total / count) - correct) / correct

def main():
    graph_5v_02 = ["5_vertices_run1000_02.csv", "5_vertices_run2000_02.csv", "5_vertices_run5000_02.csv", "5_vertices_run10000_02.csv"]
    graph_10v_03 = ["10_vertices_run1000_03.csv", "10_vertices_run2000_03.csv", "10_vertices_run5000_03.csv", "10_vertices_run10000_03.csv"]
    graph_13v_03 = ["13_vertices_run1000_03.csv", "13_vertices_run2000_03.csv", "13_vertices_run5000_03.csv", "13_vertices_run10000_03.csv"]

    with open("differences.csv", mode="w") as w_file:
        w_file.write("Graph 1000 2000 5000 10000\n")

    #----------------------------------------------------------

    tmp = ["5v_graph02"]
    for g in graph_5v_02:
        tmp.append("{:.1f}%".format((calculate_differences(g) * 100)))
    tmp.append("\n")

    with open("differences.csv", mode="a") as a_file:
        a_file.write(" ".join(tmp))

    #----------------------------------------------------------

    tmp = ["10v_graph03"]
    for g in graph_10v_03:
        tmp.append("{:.1f}%".format((calculate_differences(g) * 100)))
    tmp.append("\n")

    with open("differences.csv", mode="a") as a_file:
        a_file.write(" ".join(tmp))

    #----------------------------------------------------------

    tmp = ["13v_graph03"]
    for g in graph_13v_03:
        tmp.append("{:.1f}%".format((calculate_differences(g) * 100)))
    tmp.append("\n")

    with open("differences.csv", mode="a") as a_file:
        a_file.write(" ".join(tmp))


if __name__ == "__main__":
    main()
