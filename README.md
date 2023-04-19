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
- $p_{xy}^{k}$ represents the probability of $k$th ant moving from point $x$ to point $y$. 
- $(\tau_{xy})^{\alpha}$ is the amount of pheromone deposited on the edge between $x$ and $y$, and $0\leq \alpha$ represents a parameter to adjust the influence of $\tau_{xy}$.
- $(\eta_{xy})^{\beta}$ is the reciprocal of the distance between point $x$ and point $y$, and $\beta\geq1$ represents a parameter to adjust the influence if $\eta_{xy}$.
- The denominator part is the sum of $(\tau_{xz})^{\alpha}(\eta_{xz})^{\beta}$ for z $\in$ allowed destinations from $x$ 

Beside the formula of calculating possibility to choose paths, there is another formula to update the phoeromone amount on each edge.

$$\tau_{xy}^{new} = (1 - \rho)\tau_{xy}^{old} + \sum_{k}^{m} \Delta\tau_{xy}^{k}$$
- $\rho$ is the pheromone evaporation coefficient.
- $m$ is the amount of ants passing the edge between point $x$ to point $y$.
- $\Delta\tau_{xy}^{k}$ represents the amount of pheromone deposited by $k$th ant.
- $\Delta\tau_{xy}^{k} = \frac{Q}{L_{k}} \mbox{  or  } 0 \mbox{  if no ants pass edge xy}$ 



## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.


## Application
- What is the algorithm/datastructure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.


## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.
- If you found code in another language, and then implemented in your own language that is fine - but make sure to document that.


## Summary
- Provide a summary of your findings
- What did you learn?