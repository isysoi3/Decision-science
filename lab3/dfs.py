def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for index, vertex in enumerate(graph[node]):
            if index not in visited and vertex == 1:
                dfs(graph, index, visited)
    return visited

