import heapq

# Define the graph as a dictionary (adjacency list)
graph = {
    'Pune': [('Mumbai', 150), ('Nashik', 120)],
    'Mumbai': [('Pune', 150), ('Nashik', 170), ('Nagpur', 700)],
    'Nashik': [('Pune', 120), ('Mumbai', 170), ('Nagpur', 500), ('Aurangabad', 350)],
    'Nagpur': [('Mumbai', 700), ('Nashik', 500), ('Aurangabad', 250), ('Akola', 300)],
    'Aurangabad': [('Nashik', 350), ('Nagpur', 250)],
    'Akola': [('Nagpur', 300)]
}

# Dijkstra's algorithm to find the shortest path
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

# Function to rebuild the shortest path from start to end
def shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else None

# Main program execution
def main():
    print("📍 Available cities in the graph:", ', '.join(graph.keys()))
    start = input("Enter start city (e.g., Pune): ")
    end = input("Enter end city (e.g., Akola): ")


    if start not in graph or end not in graph:
        print("❌ Invalid node name. Please choose from the listed nodes.")
        return

    distances, previous_nodes = dijkstra(graph, start)
    path = shortest_path(previous_nodes, start, end)

    if path:
        print(f"\n✅ Shortest path from {start} to {end}: {' -> '.join(path)}")
        print(f"🛣️ Total distance: {distances[end]}")
    else:
        print("❌ No path found.")

# Start the program
if __name__ == "__main__":
    main()
