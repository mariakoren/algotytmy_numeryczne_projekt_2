import random
from podstawowa import *

def monte_carlo(graph, start, target, pit, num_iterations):
    num_target_reached = 0
    num_pit_encountered = 0
    
    for _ in range(num_iterations):
        current_node = start       
        while True:
            neighbors = graph[current_node]
            next_node = random.choice(neighbors)        
            if next_node == target:
                num_target_reached += 1
                break
            elif next_node == pit:
                num_pit_encountered += 1
                break
            current_node = next_node
    probability_success = num_target_reached / num_iterations
    probability_failure = num_pit_encountered / num_iterations
    return probability_success, probability_failure

# Przykładowy graf reprezentowany jako słownik, gdzie klucze to węzły, a wartości to listy sąsiedztwa
graph, pit_node, target_node = prepare_for_monte_carlo()
start_node = 1  
num_iterations = 10000 

success_probability, failure_probability = monte_carlo(graph, start_node, 1, 2, num_iterations)
print("Szacowane prawdopodobieństwo sukcesu (dotarcia do celu):", success_probability)
print("Szacowane prawdopodobieństwo porażki (wpadnięcia do studzienki):", failure_probability)