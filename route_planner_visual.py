import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'Pune': [('Mumbai', 150), ('Nashik', 120)],
    'Mumbai': [('Pune', 150), ('Nashik', 170), ('Nagpur', 700)],
    'Nashik': [('Pune', 120), ('Mumbai', 170), ('Nagpur', 500), ('Aurangabad', 350)],
    'Nagpur': [('Mumbai', 700), ('Nashik', 500), ('Aurangabad', 250), ('Akola', 300)],
    'Aurangabad': [('Nashik', 350), ('Nagpur', 250)],
    'Akola': [('Nagpur', 300)]
}

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

def shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else None

def visualize_graph(graph, path=None):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)

    plt.title("Route Planner Graph")
    plt.show()

def main():
    print("📍 Available cities in the graph:", ', '.join(graph.keys()))
    start = input("Enter start city (e.g., Pune): ")
    end = input("Enter end city (e.g., Akola): ")

    if start not in graph or end not in graph:
        print("❌ Invalid city name.")
        input("\nPress Enter to exit...")
        return

    distances, previous_nodes = dijkstra(graph, start)
    path = shortest_path(previous_nodes, start, end)

    if path:
        print(f"\n✅ Shortest path from {start} to {end}: {' -> '.join(path)}")
        print(f"🛣️ Total distance: {distances[end]}")
        visualize_graph(graph, path)
    else:
        print("❌ No path found.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
