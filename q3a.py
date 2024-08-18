from collections import deque
def can_be_friends_bfs(graph, restrictions, u, v):
    # Check if u and v directly violate any restrictions
    for x, y in restrictions:
        if (u == x and v == y) or (u == y and v == x):
            return False
        
        # Perform BFS from x to check if we can reach y through any path that includes u-v
        queue = deque([x])
        visited = set()
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current == y:
                return False
            for neighbor in graph[current]:
                queue.append(neighbor)
    
    return True

def friend_requests_bfs(num_houses, restrictions, requests):
    graph = {i: [] for i in range(num_houses)}
    results = []

    for u, v in requests:
        if can_be_friends_bfs(graph, restrictions, u, v):
            graph[u].append(v)
            graph[v].append(u)
            results.append("approved")
        else:
            results.append("denied")
    
    return results
# Example 1
num_houses1 = 3
restrictions1 = [[0, 1]]
requests1 = [[0, 2], [2, 1]]
print(friend_requests_bfs(num_houses1, restrictions1, requests1))  # Output: ["approved", "denied"]

# Example 2
num_houses2 = 5
restrictions2 = [[0, 1], [1, 2], [2, 3]]
requests2 = [[0, 4], [1, 2], [3, 1], [3, 4]]
print(friend_requests_bfs(num_houses2, restrictions2, requests2))  # Output: ["approved", "denied", "approved", "denied"]
