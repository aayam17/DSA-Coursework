import heapq

def dijkstra(graph, n, start, end):
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            if weight == -1:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances[end]

def modify_road_times(n, roads, source, destination, target):
    graph = {i: [] for i in range(n)}
    to_be_constructed = []

    for u, v, w in roads:
        if w == -1:
            to_be_constructed.append((u, v))
        else:
            graph[u].append((v, w))
            graph[v].append((u, w))

    # Calculate the shortest path with existing roads
    initial_shortest_path = dijkstra(graph, n, source, destination)
    
    if initial_shortest_path == target:
        return [[u, v, 1 if w == -1 else w] for u, v, w in roads]

    # Binary search to find the appropriate weight for construction roads
    low, high = 1, 2 * 10**9
    while low < high:
        mid = (low + high) // 2
        
        # Temporarily update graph with mid as the weight for construction roads
        for u, v in to_be_constructed:
            graph[u].append((v, mid))
            graph[v].append((u, mid))
        
        current_shortest_path = dijkstra(graph, n, source, destination)
        
        # Remove the temporary mid weights for the next iteration
        for u, v in to_be_constructed:
            graph[u].remove((v, mid))
            graph[v].remove((u, mid))
        
        if current_shortest_path < target:
            low = mid + 1
        else:
            high = mid

    final_weight = low

    # Final update of the graph with the determined weight for construction roads
    for u, v in to_be_constructed:
        graph[u].append((v, final_weight))
        graph[v].append((u, final_weight))

    return [[u, v, final_weight if w == -1 else w] for u, v, w in roads]

# Example usage:
n = 5
roads = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
source = 0
destination = 1
target = 5

print(modify_road_times(n, roads, source, destination, target))
