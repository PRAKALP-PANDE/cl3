'''
Imagine you have a bunch of cells in your body, each with a unique receptor that can recognize different parts of a harmful invader, like a virus. When your body detects a virus, the cells with receptors that match parts of the virus multiply rapidly to fight off the infection.

Now, let's apply this idea to optimization problems, like finding the best solution to a complex mathematical equation or optimizing parameters for a machine learning model.

In the Clonal Selection Algorithm:

We start with a population of candidate solutions (like different antibodies in the immune system).
We evaluate each candidate solution's "fitness" (how good it is) based on the problem we're trying to solve.
Solutions with higher fitness are selected to "clone" themselves.
The cloned solutions undergo a process called "mutation," where they are slightly modified to introduce diversity.
The new solutions are evaluated for fitness, and the best ones are kept.
This process repeats over multiple generations until we find a solution that meets our criteria (like finding the best solution to a problem).
So, the Clonal Selection Algorithm mimics how the immune system adapts and evolves to fight off infections, using a process of cloning, mutation, and selection to find the best solutions to optimization problems.

'''


# import random
# import numpy as np

# class ClonalSelectionAlgorithm:
#     def __init__(self, population_size, num_clones, mutation_rate):
#         self.population = [random.random() for _ in range(population_size)]
#         self.num_clones = num_clones
#         self.mutation_rate = mutation_rate

#     def run(self, iterations):
#         for _ in range(iterations):
#             clones = sorted(self.population, reverse = True)[:self.num_clones] 
#             # sorts the population in descending order and selects the top num_clones antibodies as clones i.e. (top 10)
#             mutated_clones = [clone + np.random.normal(0, self.mutation_rate) for clone in clones] 
#             # applies mutation to each clone by adding a random value sampled from a normal distribution with mean 0 and standard deviation mutation_rate.
#             self.population = [clone if random.random() < 0.5 else mutated_clones[i] for i, clone in enumerate(clones)] 
#             # If the probability is less than 0.5, the original antibody remains in the population; 
#             # otherwise, the mutated clone replaces the original antibody.updates the population based on the replacement process.
#         return self.population

# # Example usage
# csa = ClonalSelectionAlgorithm(population_size = 50, num_clones = 10, mutation_rate=0.1)
# final_population = csa.run(iterations=100)
# print("Final population:", final_population)



import random 
import numpy as np

class clonalSelectionAlgorithm:
    def __init__(self, population_size, num_clones, mutation_rate):
        self.population = [random.random() for _ in range(population_size)]
        self.num_clones = num_clones
        self.mutation_rate = mutation_rate

    def run(self, iterations):
        for _ in range(iterations):
            # 1. Top clones selection
            # 2. Mutating the selected clones
            # 3. replace with mutated clones

            clones = sorted(self.population, reverse = True)[:self.num_clones]
            mutated_clones = [clone + np.random.normal(0, self.mutation_rate) for clone in clones]
            self.population = [clone if random.random() < 0.5 else mutated_clones[i] for i, clone in enumerate(clones)]
        
        return self.population

csa = clonalSelectionAlgorithm(population_size = 100, num_clones = 10, mutation_rate = 0.1)
final_population = csa.run(iterations = 100)
print("Final Population:- ")
for point in final_population:
    print(point)
