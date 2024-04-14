import random
from rozszerzona import *

def monte_carlo(graph, start, target, pit, num_iterations):
    num_target_reached = 0
    num_pit_encountered = 0
    
    for _ in range(num_iterations):
        current_node = start 
          
        while True:
            neighbors = graph[current_node]
            next_node = random.choice(neighbors)   
            if current_node in target:
                return 1, 0
            elif current_node in pit:
                return 0, 1 
                
            if next_node in target:
                num_target_reached += 1
                break
            elif next_node in pit:
                num_pit_encountered += 1
                break
            current_node = next_node
    probability_success = num_target_reached / num_iterations
    probability_failure = num_pit_encountered / num_iterations
    return probability_success, probability_failure

graph, pit_node, target_node, start = prepare_for_monte_carlo()

success_probability, failure_probability = monte_carlo(graph, 4, target_node, pit_node, 1000)
print("Szacowane prawdopodobieństwo sukcesu (dotarcia do celu):", success_probability)
print("Szacowane prawdopodobieństwo porażki (wpadnięcia do studzienki):", failure_probability)