# BFS: Breadth-First Search

graph_A = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['A', 'D']
}

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = []  # Initialize a queue

    visited.add(start)  # Mark the start node as visited
    queue.append(start)  # Add the start node to the queue

    while queue:  # While there are nodes to process
        vertex = queue.pop(0)  # Dequeue a vertex from the queue
        print(vertex, end=" ")  # Print the vertex

        for neighbor in graph[vertex]:  # Iterate through neighbors of the vertex
            if neighbor not in visited:  # If the neighbor hasn't been visited
                visited.add(neighbor)  # Mark it as visited
                queue.append(neighbor)  # Enqueue it
    print()  # Print a newline at the end
if __name__ == "__main__":
    print("BFS traversal starting from node 'A':")
    bfs(graph_A, 'A')
    print("BFS traversal starting from node 'E':")
    bfs(graph_A, 'E')
