import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def build_park(input_matrix):
    G = nx.Graph()
    for row in input_matrix:
        intersection1, intersection2, steps = row
        G.add_node(intersection1)
        G.add_node(intersection2)
        prev_node = intersection1
        for step in range(1, steps + 1):  
            step_node = f"{intersection1}{intersection2}{step}"
            int_step_node=int(step_node)
            G.add_node(int_step_node)
            G.add_edge(prev_node, int_step_node)
            prev_node = int_step_node
        G.add_edge(prev_node, intersection2)
    return G

def adjacency_matrix(G):
    nodes = sorted(G.nodes())
    n = len(nodes)
    adj_matrix = np.zeros((n, n), dtype=int)
    for i, node in enumerate(nodes):
        for neighbor in sorted(G.neighbors(node)):
            adj_matrix[i][nodes.index(neighbor)] = 1
    return adj_matrix

def correct_adjacency(matrix):
    correct_matrix=[]
    for i in range(len(matrix)):
        correct_matrix_i = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                correct_matrix_i.append(j)
        correct_matrix.append(correct_matrix_i)
    return correct_matrix, len(matrix)
                
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])
    for row in data:
        row[2]-=1
    return data

input_matrix= read_data("dane.txt")
park_graph = build_park(input_matrix)
nx.draw(park_graph, with_labels=True)
# plt.show()
plt.savefig("graf-1.png") 

adj_matrix = correct_adjacency(adjacency_matrix(park_graph))
# print("Macierz sąsiedztwa:")
# print(adj_matrix)

