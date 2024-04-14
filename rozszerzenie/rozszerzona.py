import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generate_transition_matrix(n,  adjacency_list):
    transition_matrix = np.zeros((n, n))
    for i in range(n):
        neighbors = adjacency_list[i]
        num_neighbors = len(neighbors)
        for neighbor in neighbors:
            transition_matrix[i][neighbor] = 1 / num_neighbors
    return transition_matrix



def generate_equations(transition_matrix):
    n = len(transition_matrix)
    equations = []
    for i in range(n):
        eq = []
        for j in range(n):
            if i == j:
                eq.append(1 - transition_matrix[i][j])
            else:
                eq.append(-transition_matrix[i][j])
        equations.append(eq)
    return equations

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

def read_data2(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append([int(x) for x in line.split()])
    return data

def prepare_data(matrix, osk, exit):
    vector = []
    for i in range(1, len(matrix)+1):
        if i in osk or i in exit:
            for j in range(len(matrix[i])):
                if matrix[i][j]!=1:
                    matrix[i][j] = 0
    for i in range(1, len(matrix) + 1):
        if i in exit:
            vector.append(1)
        else:
           vector.append(0)
    return matrix, vector
            
def main():
    input_matrix= read_data("rozszerzenie/dane.txt")
    park_graph = build_park(input_matrix)
    nx.draw(park_graph, with_labels=True)
    # plt.show()
    plt.savefig("graf-1.png") 
    adj_matrix, n = correct_adjacency(adjacency_matrix(park_graph))
    transition_matrix = generate_transition_matrix(n, adj_matrix)
    equations = generate_equations(transition_matrix)
    osk = read_data2("rozszerzenie/dane2.txt")[0]
    wyjscie = read_data2("rozszerzenie/dane2.txt")[1]
    matrix, vector = prepare_data(equations, osk, wyjscie)
    for row in matrix:
        print(row)
    # return matrix, vector


def prepare_for_monte_carlo():
    input_matrix= read_data("dane.txt")
    park_graph = build_park(input_matrix)

    adj_matrix, n = correct_adjacency(adjacency_matrix(park_graph))
    slownik = {indeks: wartosc for indeks, wartosc in enumerate(adj_matrix)}
    nowy_slownik = {}
    nowy_slownik = {}
    for key, values in slownik.items():
        nowy_slownik[key + 1] = [val + 1 for val in values]
    osk = read_data2("dane2.txt")[0]
    wyjscie = read_data2("dane2.txt")[1]
    start = read_data2("dane2.txt")[2]
    # print(slownik)
    # print()
    # print(nowy_slownik)

    return nowy_slownik, osk, wyjscie, start
    

if __name__ == "__main__":
    main()
# prepare_for_monte_carlo()