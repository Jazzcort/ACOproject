from collections import defaultdict, deque
import sys
"""
This ShortestCycle class is the implementation of naive algorithm to solve TSP.
"""
class ShortestCycle:

    """
    shortestCycle is a list of vertices representing the shortestCycle
    minDistance is the distance of the shortest cycle.
    adj_dict is the hashmap to store the distance between all vertices.
    """
    def __init__(self, filename):
        self.shortestCycle = []
        self.minDistance = float("inf")
        self.adj_dict = self.load_file(filename)

    """
    This function is to load the distance information from the given file.
    filename is the name of the given file.
    Print error messages, if the given file doesn't exist.
    """
    def load_file(self, filename):

        adj_dict = defaultdict(lambda: defaultdict(float))

        try:
            with open(filename, mode="r") as r_file:
                for line in r_file:
                    tmp = line.strip("\n").split(" ")
                    adj_dict[tmp[0]][tmp[1]] = float(tmp[2])
                    adj_dict[tmp[1]][tmp[0]] = float(tmp[2])


        except FileNotFoundError:
            print(f"{filename} dose not exist")
            return

        return adj_dict

    """
    This is the function to find the shortest cycle in the graph.
    """
    def shortest_cycle(self):
        vertices = list(self.adj_dict.keys())
        vertices = deque(vertices)
        path = []

        # This is the recursive helper function to find the shortest cycle.
        def r_find(pre, curSum):
            if curSum >= self.minDistance:
                return

            if not vertices:
                total = curSum + self.adj_dict[pre][path[0]]
                if total < self.minDistance:
                    self.minDistance = total
                    self.shortestCycle = path[:] + [path[0]]

                return

            n = len(vertices)

            for _ in range(n):
                cur = vertices.popleft()
                path.append(cur)
                if pre:
                    curSum += self.adj_dict[pre][cur]

                r_find(cur, curSum)
                vertices.append(cur)
                if pre:
                    curSum -= self.adj_dict[pre][cur]
                path.pop()

        r_find(None, 0)


"""
This is the main drive.
"""
def main():
    pp = ShortestCycle("out.txt")
    pp.shortest_cycle()

    print((pp.shortestCycle, pp.minDistance))

    # return (pp.shortestCycle, pp.minDistance)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Usage: python3 shortest_cycle.py")
    else:
        main()
