# DFS: Depth First Search

graph_A = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['A', 'D']
}

def dfs(graph, start_node):
    visited = set()
    result = []

    def dfs_recursive(node):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start_node)
    return result

if __name__ == "__main__":
    print("DFS traversal starting from node 'A':")
    print(dfs(graph_A, 'A'))
    print("DFS traversal starting from node 'E':")
    print(dfs(graph_A, 'E'))
