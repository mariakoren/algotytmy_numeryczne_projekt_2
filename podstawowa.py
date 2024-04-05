import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generate_transition_matrix(n, d, adjacency_list):
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

def draw_graph(n, adjacency_list):
    G = nx.Graph()
    for i in range(n):
        for neighbor in adjacency_list[i]:
            G.add_edge(i+1, neighbor+1)
    pos = nx.spring_layout(G)  # Ustawienie pozycji węzłów na grafie
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')  # Rysowanie grafu
    plt.title("Graf skrzyżowań w parku")
    plt.savefig("graf.png")  # Zapisanie grafu jako plik obrazu

def main():
    n = 4
    d = [
        [0, 4, 6, 4],
        [4, 0, 4, 0],
        [6, 4, 0, 4],
        [4, 0, 4, 0]
    ]
    
    adjacency_list = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    
    transition_matrix = generate_transition_matrix(n, d, adjacency_list)
    equations = generate_equations(transition_matrix)
    draw_graph(n, adjacency_list)
    print("Układ równań:")
    for eq in equations:
        print(eq)

if __name__ == "__main__":
    main()
