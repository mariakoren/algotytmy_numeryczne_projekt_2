import networkx as nx
import random

def generate_park_graph(num_crossroads, crossroads, road_lengths):
    G = nx.Graph()
    for i in range(num_crossroads):
        G.add_node(crossroads[i])
    for i in range(num_crossroads):
        for j in range(i+1, num_crossroads):
            G.add_edge(crossroads[i], crossroads[j], weight=road_lengths[i][j])
            G.add_edge(crossroads[j], crossroads[i], weight=road_lengths[j][i])
    return G

def find_shortest_path(G, start, end):
    try:
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return None

def calculate_probability_of_success(G, path, osk_crossroad):
    num_success = 0
    num_trials = 10000
    
    for _ in range(num_trials):
        current_crossroad = path[0]
        for i in range(1, len(path)):
            neighbors = list(G.neighbors(current_crossroad))
            if osk_crossroad in neighbors:
                neighbors.remove(osk_crossroad)  # Exclude the OSK crossroad
            if path[i-1] in neighbors:  # Check if the previous crossroad is in neighbors
                neighbors.remove(path[i-1])  # Exclude the previous crossroad
            if neighbors:  # Check if there are any neighbors left
                next_crossroad = random.choice(neighbors)
                current_crossroad = next_crossroad
                if current_crossroad == path[i]:
                    num_success += 1
                    break
    
    probability = num_success / num_trials
    return probability



# Example usage
if __name__ == "__main__":
    num_crossroads = 5
    crossroads = ['v1', 'v2', 'v3', 'v4', 'v5']
    road_lengths = [
        [0, 10, 20, 0, 0],
        [10, 0, 15, 25, 0],
        [20, 15, 0, 10, 0],
        [0, 25, 10, 0, 30],
        [0, 0, 0, 30, 0]
    ]
    start_crossroad = 'v1'
    end_crossroad = 'v5'
    osk_crossroad = 'v3'  # Example OSK crossroad
    
    G = generate_park_graph(num_crossroads, crossroads, road_lengths)
    shortest_path = find_shortest_path(G, start_crossroad, end_crossroad)
    if shortest_path:
        print("Shortest path:", shortest_path)
        probability = calculate_probability_of_success(G, shortest_path, osk_crossroad)
        print("Probability of success:", probability)
    else:
        print("There is no path from start to end.")
