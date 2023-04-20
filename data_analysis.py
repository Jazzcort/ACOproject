def calculate_accuracy(file):
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
                if abs(float(tmp[-2]) - correct) < 0.01:
                    count += 1
                    total += 1
                else:
                    total += 1
    return count / total

def main():
    graph_5v_01 = ["5_vertices_run1000_01.csv", "5_vertices_run2000_01.csv", "5_vertices_run5000_01.csv", "5_vertices_run10000_01.csv"]
    graph_5v_02 = ["5_vertices_run1000_02.csv", "5_vertices_run2000_02.csv", "5_vertices_run5000_02.csv", "5_vertices_run10000_02.csv"]
    graph_5v_03 = ["5_vertices_run1000_03.csv", "5_vertices_run2000_03.csv", "5_vertices_run5000_03.csv", "5_vertices_run10000_03.csv"]
    graph_10v_01 = ["10_vertices_run1000_01.csv", "10_vertices_run2000_01.csv", "10_vertices_run5000_01.csv", "10_vertices_run10000_01.csv"]
    graph_10v_02 = ["10_vertices_run1000_02.csv", "10_vertices_run2000_02.csv", "10_vertices_run5000_02.csv", "10_vertices_run10000_02.csv"]
    graph_10v_03 = ["10_vertices_run1000_03.csv", "10_vertices_run2000_03.csv", "10_vertices_run5000_03.csv", "10_vertices_run10000_03.csv"]
    graph_13v_01 = ["13_vertices_run1000_01.csv", "13_vertices_run2000_01.csv", "13_vertices_run5000_01.csv", "13_vertices_run10000_01.csv"]
    graph_13v_02 = ["13_vertices_run1000_02.csv", "13_vertices_run2000_02.csv", "13_vertices_run5000_02.csv", "13_vertices_run10000_02.csv"]
    graph_13v_03 = ["13_vertices_run1000_03.csv", "13_vertices_run2000_03.csv", "13_vertices_run5000_03.csv", "13_vertices_run10000_03.csv"]

    

    # print(calculate_accuracy("5_vertices_run10000_02.csv"))

if __name__ == "__main__":
    main()
