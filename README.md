# Research Paper
Name: Chih-Tao Lee

Semester: 2023 Spring

Topic: Analyzing Ant Colony Optimization Algorithm and comparing it with naive shortest cycle algorithm

Link The Repository: https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort

## Introduction
- What is the algorithm/datastructure?
- What is the problem it solves? 
- Provide a brief history of the algorithm/datastructure. (make sure to cite sources)
- Provide an introduction to the rest of the paper. 

In this final research paper, I selected Ant Colony Optimization to be the algorithm I'd be introducing and analyzing later in the following section. The Ant Colony Optimization is the optimization algorithm to solve TSP(Travelling Salesman Problem). It was first proposed in 1991 by Marco Dorigo and inspired by the behavior of biological ants searching for food. Even though the initial versions didn't provide results that's promising enough, its potential encouraged many researchers starting to study and improve this algorithm. Nowadays, ACO (Ant Colony Optimization) has been widely used in the field of both scientific and industrial.

In the latter section of this paper, I would be demostrating the implementation of ACO of solving TSP problem and comparing it with a naive algorithm of solving TSP problem in the perspective of time complexity, space complexity, and accuracy.

## Analysis of Algorithm/Datastructure
Make sure to include the following:
- Time Complexity
- Space Complexity
- General analysis of the algorithm/datastructure

Since the ACO was inspired by the foraging behavior of natural ants, pheromone was introduced in this algorithm. Basically, when an ant is passing through an edge in the graph, it deposits pheromone on this edge. The amount of pheromone on the edge becomes one of the two factors that affects an ant to choose where it would go next. The other factor would be the reciprocal of the distance between two points. The formula to calculate the possibility of choosing each path is:

$$p_{xy}^{k} = \frac{(\tau_{xy})^{\alpha} (\eta_{xy})^{\beta}}{\sum_{z\in allowed_{x}}(\tau_{xz})^{\alpha}(\eta_{xz})^{\beta}}$$
- $p_{xy}^{k}$ represents the probability of kth ant moving from point $x$ to point $y$. 
- $(\tau_{xy})^{\alpha}$ is the amount of pheromone deposited on the edge between $x$ and $y$, and $0\leq \alpha$ represents a parameter to adjust the influence of $\tau_{xy}$.
- $(\eta_{xy})^{\beta}$ is the reciprocal of the distance between point $x$ and point $y$, and $\beta\geq1$ represents a parameter to adjust the influence if $\eta_{xy}$.
- The denominator part is the sum of $(\tau_{xz})^{\alpha}(\eta_{xz})^{\beta}$ for z $\in$ allowed destinations from $x$ 

Beside the formula of calculating possibility to choose paths, there is another formula to update the phoeromone amount on each edge.

$$\tau_{xy}^{new} = (1 - \rho)\tau_{xy}^{old} + \sum_{k}^{m} \Delta\tau_{xy}^{k}$$
- $\rho$ is the pheromone evaporation coefficient.
- $m$ is the amount of ants passing the edge between point $x$ to point $y$.
- $\Delta\tau_{xy}^{k}$ represents the amount of pheromone deposited by kth ant.
- $\Delta\tau_{xy}^{k} = \frac{Q}{L_{k}} \mbox{  or  } 0 \mbox{  if no ants pass edge xy}$, where $Q$ is the amount of pheromone carried per ant $L_{k}$ is the distance kth ant traveled.

Before we discuss the time complexity and the space complexity, there is a important precondition of my implementation that I have to mention. All the graphs we consider in this algorithm have to be fully connected graphs which means there is always an edge between every pair of vertices in this graph.

The time complexity of the Ant Colony Optimization I implemented is $O(n^{2})$, where $n$ is the number of vetices in the graph. Since the ant has to visit every vertex only once, when the ant made its decision, the avaliable options would decrease by one. To make a decision, the ant has to know all the possibility of avaliable paths. Therefore, an ant going through the graph once takes $\frac{n (n - 1)}{2}$ operations. Updating the pheromone takes $n$ operations. Updating the best route takes also $n$ operations. The total operations needed for a fully run of this algorithm would be $\frac{n (n - 1)}{2} + n + n$, so the time complexity is $O(n^{2})$. To increase the accuracy of this algorithm, we can decide how many time we want to run this algorithm. However, the number of times we run this algorithm actually would not affect the time complexity of the algorithm itself. Instead, it would just increase the runtime of the whole procedure.

The space complexity of my implementation is $O(n^{2})$, because I used two dectionaries of dictionaries(hashmap) to store the distance and pheromone amount between every two vertices. Each vertex in the dictionary has a dictionary of all the other vertices as keys and the distance or pheromone amount as values.

Here is the table of comparing the time complexity and space complexity between the ACO and naive algorithm of solving TSP in a fully connected graph:

| Algorithm |  Time Complexity | Space Complexity | 
| :-- | :--: |  :--: |
| ACO | $O(n^{2})$ | $O(n^{2})$ |
| Naive (Brute-force) | $O(n!)$  | $O(n)$ |

As what we can observe from the above table, ACO algorithm reduce the time complexity significantly from $O(n!)$ to $O(n^{2})$. However, the tradeoff is the accuracy of the result. In the ACO algorithm, the result is not guaranteed to be the shortest cycle of visiting every vertex, but it's close enough and practical to apply to the real world. Although the naive solution can always find the shortest cycle, it becomes impractical even there is only 20 vertices in the graph.

In the next cestion, I would use some data collected from different senarios to demonstrate the accuracy of ACO algorithm.

## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.

In this section, I used [graph_utility.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/graph_utility.py) to randomly generate 9 different graphs (3 graphs with 5 vertices, 3 graphs with 10 vertices, ans 3 graphs with 13 vetices). Then, I used [generate_data.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/generate_data.py) to apply the ACO algorithm to these graphs with different settings (run 1000 times, 2000 times, 5000 times, 10000times). Finally, I used [data_analysis.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/data_analysis.py) to calculate the accuracy of the shortest cycle given by the ACO algorithm and export the data in [accuracy.csv](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/accuracy.csv). Here is the table of accuracies:

| Graph |  Run 1000 times | Run 2000 times | Run 5000 times | Run 10000 times |
| :-- | :--: |  :--: | :--: | :--: |
| 5-vertices graph 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| 5-vertices graph 2 | 23.0% | 18.0% | 24.0% | 28.0% |
| 5-vertices graph 3 | 100.0% | 100.0% | 100.0% | 100.0% |
| 10-vertices graph 1 | 100.0% | 100.0% | 100.0% | 100.0% |
| 10-vertices graph 2 | 100.0% | 100.0% | 100.0% | 100.0% |
| 10-vertices graph 3 | 0.0% | 0.0% | 0.0% | 0.0% |
| 13-vertices graph 1 | 23.0% | 48.0% | 80.0% | 92.0% | 
| 13-vertices graph 2 | 93.0% | 100.0% | 100.0% | 100.0% | 
| 13-vertices graph 3 | 5.0% | 8.0% | 9.0% | 16.0% | 

As what we can observe from the table above, there are some graphs that are hard for ACO algorithm to find the shortest cycle due to their geometric features. The 10-vertices graph 2 demonstrated the extreme case. It showed that even though we increase the amount of running times, it still could not find the shortest cycle even once. Except for those special cases due to the geometric features, increasing the running times indeed increases the accuracy, and it becomes more obvious in the graphs with more vertices. For example, the accuracy of the 13-vertices graph 1 went from 23.0% to 92.0% as we increase the running times (run 1000 times v.s. run 10000 times).

The accuracy of finding the shortest cycle by ACO algorithm is actually quite random. It shows that the geometric feature has a significant influence on ACO algorithm for finding the shortest cycle. However, finding the shortest cycle is actually not that important. The main purpose of ACO algorithm is to come up with the cycle whose cost is close enough to the cost of shortest cycle with remarkable reduction in time complexity. Here is the table showing the differences of cost (distance) in percentage between the shortest cycle and the cycle given by ACO algorithm. (Here we only analyze the graphs with low accuracy of finding shortest cycle.)

| Graph |  Run 1000 times | Run 2000 times | Run 5000 times | Run 10000 times |
| :-- | :--: |  :--: | :--: | :--: |
| 5-vertices graph 2 |4.8% | 5.2% | 4.8% | 4.3% | 
| 10-vertices graph 3 | 4.0% | 3.8% | 3.8% | 3.8% | 
| 13-vertices graph 3 | 6.8% | 6.9% | 6.7% | 6.1% | 

From the table above, we can observe that the average distance of the cycles given by ACO algorithm only differ slightly from the shortest cycle (Less than 7%). This margins is small enough to trade with the reduction of time complexity for practical applications. Here is the table showing the time cost:

| Algorithm |  Time Cost | 
| :-- | :--: | 
| 5-vertices Naive | $\leq$ 0.01s | 
| 5-vertices ACO 1000 times | 0.02s |
| 5-vertices ACO 2000 times | 0.03s |
| 5-vertices ACO 5000 times | 0.07s |
| 5-vertices ACO 10000 times | 0.15s |
| 10-vertices Naive | 0.34s | 
| 10-vertices ACO 1000 times | 0.05s |
| 10-vertices ACO 2000 times | 0.11s |
| 10-vertices ACO 5000 times | 0.27s |
| 10-vertices ACO 10000 times | 0.53s |
| 13-vertices Naive | 42.44s | 
| 13-vertices ACO 1000 times | 0.09s |
| 13-vertices ACO 2000 times | 0.17s |
| 13-vertices ACO 2000 times | 0.43s |
| 13-vertices ACO 10000 times | 0.86s |

As the information showed above, when there are only 5 vertices in the graph, the difference in time cost is very small. However, as the vertices increase, the differences start to stand out. The time cost increases significantly (0.34 seconds to 42.44 seconds) for the naive algorithm while there are just three more vertices added to the graph (10 vertices v.s. 13 vertices). The time cost of applying naive algorithm to a 14-vertices graph is roughly 300 - 400 seconds, but the ACO algorithm still cost less than 1 second. Therefore, the ACO algorithm is much more practical to be applied in the real world, where we have ten thousand vetices or even hundred thousand vertices to deal with.

## Application
- What is the algorithm/datastructure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.

The ACO algorithm was originally intended for solving NP-hard problems such as TSP. Because there are no polynomial-time algorithms found for NP-hard problems, ACO algorithm is often used to generate solutions with high-quallity in reasonable time cost.

There are more NP-hard problems, where we can apply ACO algorithm to get optimized solutions. For example, 
VRP (Vehicle routing problem), Industrial scheduling, NSP (nurse scheduling problem), Bayesian networks, and DNA sequencing, etc. These problems covered a large range of applications including routing, scheduling, machine learning, and bioinformatics. Beside the academic applications, there are also many commercial company utilizing ACO algorithm to solve the real world problems. The company AntOptima ([www.antoptima.com](www.antoptima.com)) is one of the best example. It developes ACO-based solution methods for their customers to improve the efficiency of productive and logistic processes in their business.

### Citation: 
1. Stützle, Thomas, et al. "A concise overview of applications of ant colony optimization." Wiley encyclopedia of operations research and management science 2 (2011): 896-911.
## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.
- If you found code in another language, and then implemented in your own language that is fine - but make sure to document that.

- [ant_colony_optimization.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/ant_colony_optimization.py): implementation of ACO algorithm in Python
- [shortest_cycle.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/shortest_cycle.py): implementation of naive algorithm of finding shortest cycle in Python
- [graph_utility.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/graph_utility.py): auxiliary program of generating random graphs
- [generate_data.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/generate_data.py): auxiliary program of generating data for empirical analysis
- [data_analysis.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/data_analysis.py): auxiliary program of calculating the accuracies of ACO algorithm
- [data_analysis_diff.py](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort/blob/main/data_analysis_diff.py): auxiliary program of calculating the margins between the result given by ACO algorithm and the shortest cycle.

I used Python for my implementation of ACO algorithm, because it's the programming language I'm most familier with. It could prevent me from spending too much time figuring out the errors caused by syntex  or mechanism of the language, so I could focus more on the developement of my implementation. 

```Python
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
```

I used the defaultdict from collections library im Python. It's an advanced hashmap structure that is easiler to set up default value than the general dictionary does. I also used the randint() function from random library to simulate the ant choosing path with possibilities. To initiate an ACO instance, we need to pass the name of the file containing the distance information, the pheromone evaporation coefficient, and the pheromone amount carried per ant. In the initiating process, the load_file() function would load the given file and construct the adjacent hashmap. The result would be store in the instance variable adj_dict. The create_pheromone_dict() would initiate a hashmap to keep on tracking the pheromone amount in each edge. The instance variable bestRoute would be initiate as an empty list, and it would be used to store the shortest cycle this algorithm has checked so far. The instance variable minDistance would be used to store the distance of the bestRoute.

```Python
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
```
The create_possibility() function takes two parameters. The src is the name of the vertex where the ant is current at. The forbiden is a set of vertices that the ant has visited. In this function, it first iterates through all the vertices, and add the vertices that the ant has not visited into a list, candidates. Then, it creates a defaultdict, factor, to store the result of $\tau_{src-dest} \eta_{src-dest}$ for every vertex in candidates. After calculating the sum of all the elements in factor, it divides each elements in factor with the sum to get the possibility of choosing each path. The function creates another defaultdict, possibility, to store each avaliable vertex with its posibility and return the defaultdict.

```Python
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
```

After calculating possibilities, I wrote the make_decision() function to simulate ants choosing the path. This function uses the defaultdict created by create_possibility() and adds up the possibilities for each vertex. Eventually, every vertex would have its own possibility interval. Then, I used randint() to generate a number between 0 and 1. When the number falls into the possibility interval of a certain vertex, the ant would choose this vertex to be the next vertex it visits.

```Python
def update_pheromone(self, src, dest, count):
        old = self.pheromone_dict[src][dest]
        n_pher = (old * (1 - self.evaporateSpeed)) + ((count * self.pheromonePerAnt) / self.adj_dict[src][dest])
        if n_pher < 0.01:
            n_pher = 0.01
        self.pheromone_dict[src][dest] = n_pher
        self.pheromone_dict[dest][src] = n_pher
```
The update_pheromone() function is to update the pheromone amount on the edge. It takes three parameters, the src and dest are the two vertices connected by the edge, the count is the number of ants that have passed this edge in a certain period of time. It basically follows the formula given in the previous [section](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-Jazzcort#analysis-of-algorithmdatastructure) 



## Summary
- Provide a summary of your findings
- What did you learn?