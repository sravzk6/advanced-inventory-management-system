import networkx as nx
import matplotlib.pyplot as plt

# Function to visualize the shortest path in the graph
def visualize_shortest_path(G, pos, shortest_path):
    plt.figure(figsize=(10, 8))
    # Draw the entire graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_weight='bold', arrows=True)
    # Highlight the edges of the shortest path
    path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red')
    # Set a title for the plot
    plt.title(f'Shortest Path from {shortest_path[0]} to {shortest_path[-1]}')
    plt.show()

# Function to visualize the graph with edge weights
def visualize_graph(G, pos, edge_labels):
    plt.figure(figsize=(10, 8))
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=500, font_weight='bold', arrows=True)
    # Add edge weights avoiding overlap
    for edge, weight in edge_labels.items():
        x1, y1 = pos[edge[0]]
        x2, y2 = pos[edge[1]]
        x, y = (x1 + x2) / 2, (y1 + y2) / 2
        dx = (x2 - x1) * 0.1
        dy = (y2 - y1) * 0.1
        plt.text(x + dx, y + dy, str(weight), fontsize=10, ha='center', va='center', color='darkblue')
    # Set a title for the plot
    plt.title('Directed Graph with Edge Weights')
    plt.show()

# Function to visualize BFS tree
def visualize_bfs_tree(G, source):
    bfs_tree = nx.bfs_tree(G, source=source)
    pos = nx.spring_layout(bfs_tree)
    plt.figure(figsize=(10, 8))
    nx.draw(bfs_tree, pos, with_labels=True, node_color='lightcoral', edge_color='black', node_size=500, font_weight='bold', arrows=True)
    plt.title('Directed BFS Tree')
    plt.show()

# Function to visualize DFS tree
def visualize_dfs_tree(G, source):
    dfs_tree = nx.dfs_tree(G, source=source)
    pos = nx.spring_layout(dfs_tree)
    plt.figure(figsize=(10, 8))
    nx.draw(dfs_tree, pos, with_labels=True, node_color='lightyellow', edge_color='purple', node_size=500, font_weight='bold', arrows=True)
    plt.title('Directed DFS Tree')
    plt.show()

# Main function to interactively create and analyze the graph
def main():
    # Create an empty directed graph
    G = nx.DiGraph()

    # Input the number of nodes and their names
    n = int(input("Enter the Number of nodes: "))
    arr = list(map(str, input("Enter the Nodes: ").split()))
    G.add_nodes_from(arr)

    edges = []
    test = 1
    print("Enter The Connections For The Graph: ")

    # Input the edges and their weights
    while test == 1:
        src = input("Enter source node: ")
        tar = input("Enter target node: ")
        weight = float(input("Enter edge weight: "))
        connections = (src, tar, weight)
        edges.append(connections)
        test = int(input("Do you want to continue(1 or 0): "))

    # Add edges to the graph
    G.add_weighted_edges_from(edges)

    # Generate positions for nodes in the graph
    pos = nx.spring_layout(G)

    # Extract edge weights for visualization
    edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}

    # Visualize the graph with edge weights
    visualize_graph(G, pos, edge_labels)

    # Analyze the graph using BFS, DFS, and shortest path algorithms
    source_node = input("Enter source node for BFS and DFS: ")
    try:
        visualize_bfs_tree(G, source_node)
        visualize_dfs_tree(G, source_node)

        source_nodesh = input("Enter the source node for shortest path: ")
        target_node = input("Enter target node for shortest path: ")
        shortest_path = nx.shortest_path(G, source=source_nodesh, target=target_node, weight='weight')
        print("Shortest Path with Weights:", shortest_path)
        visualize_shortest_path(G, pos, shortest_path)
    except nx.NetworkXError as e:
        print(f"Error: {e}")

# Call the main function
if __name__ == "__main__":
    main()
