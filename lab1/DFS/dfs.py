graph1 = {
    '1': ['2', '3'],
    '2': ['1', '4'],
    '3': ['1'],
    '4': ['2'],
    '5': ['6'],
    '6': ['5'],
    '7': []
}


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


visited = []
component = 0
for key, value in graph1.items():
    if key not in visited:
        tmp = dfs(graph1, key, [])
        visited.extend(tmp)
        component += 1
        print(tmp)

print(component)
