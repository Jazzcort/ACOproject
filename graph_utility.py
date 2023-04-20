from random import randint
from math import sqrt
def create_fully_connected_graph(filename, maxDistance):
    vertices = set()
    try:
        with open(filename, mode="r") as r_file:
            for line in r_file:
                tmp = line.strip("\n").strip(" ")
                vertices.add(tmp)
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return

    vertices = list(vertices)
    n = len(vertices)
    coordinate = []
    seen = set()

    for i in range(n):
        x = randint(-maxDistance, maxDistance)
        y = randint(-maxDistance, maxDistance)

        while (x, y) in seen:
            x = randint(-maxDistance, maxDistance)
            y = randint(-maxDistance, maxDistance)

        coordinate.append((x, y))
        seen.add((x, y))

    out = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            dis = sqrt((coordinate[i][0] - coordinate[j][0])**2 + (coordinate[i][1] - coordinate[j][1])**2)
            out.append(vertices[i] + " " + vertices[j] + " " + "{:.2f}".format(dis))


    try:
        with open("out.txt", mode="w") as a_file:
            a_file.write("\n".join(out))
    except:
        print("Can not export file")
        return


def main():
    pass
    # create_fully_connected_graph("5_vertices.txt", 100)

if __name__ == "__main__":
    main()
