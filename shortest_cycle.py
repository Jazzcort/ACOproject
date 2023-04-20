from collections import defaultdict, deque
import sys
class ShortestCycle:

    def __init__(self, filename):
        self.shortestCycle = []
        self.minDistance = float("inf")
        self.adj_dict = self.load_file(filename)

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
    def shortest_cycle(self):
        vertices = list(self.adj_dict.keys())
        vertices = deque(vertices)
        path = []

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


def main():
    pp = ShortestCycle("out.txt")
    pp.shortest_cycle()

    # print((pp.shortestCycle, pp.minDistance))

    return (pp.shortestCycle, pp.minDistance)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Usage: python3 shortest_cycle.py")
    else:
        main()
