"""
Author: Lauren Ruff
Due Date: May 31, 2022
Module: 9
Assignment: NP-Completeness

Description: Implement Traveling Salesman Problem using the nearest - neighbor heuristic. The input graph is in the form
             of a 2D matrix (adjacency matrix) and the first node is considered the starting point. The output will be a
             list of indices indicating the path taken.
"""


def solve_tsp(G):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    G = [[0, 2, 3, 20, 1],
         [2, 0, 15, 2, 20],
         [3, 15, 0, 20, 13],
         [20, 2, 20, 0, 9],
         [1, 20, 13, 9, 0]]

    print(solve_tsp(G))
