import random
import math

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.dist(city1, city2)

# Function to compute the total distance of the tour
def compute_total_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

# Function to generate a random initial solution (tour)
def create_initial_solution(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

# Function to generate neighboring solutions by swapping two cities in the tour
def create_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            neighbor = tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Hill Climbing algorithm to solve the TSP
def solve_tsp_with_hill_climbing(cities):
    num_cities = len(cities)
    current_solution = create_initial_solution(num_cities)
    current_distance = compute_total_distance(current_solution, cities)
    
    while True:
        neighbors = create_neighbors(current_solution)
        best_neighbor = min(neighbors, key=lambda tour: compute_total_distance(tour, cities))
        best_distance = compute_total_distance(best_neighbor, cities)
        
        if best_distance >= current_distance:
            break
        
        current_solution, current_distance = best_neighbor, best_distance
    
    return current_solution, current_distance

# Example cities with their (x, y) coordinates
cities = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 0), (2, 4), (5, 5), (7, 2)
]

# Solve the Traveling Salesman Problem using Hill Climbing
best_tour, best_distance = solve_tsp_with_hill_climbing(cities)
print("Best tour found:", best_tour)
print("Total distance of the best tour:", best_distance)
