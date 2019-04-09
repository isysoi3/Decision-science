import collections


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] is False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    print(parent)
    return visited[t]


def edmonds_karp_algoritm(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def main():
    matrix = [
        [0, 2, 0, 5, 0, 3, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 0, 0, 3, 1],
        [0, 0, 2, 0, 2, 4, 5, 0, 0],
        [0, 4, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 4, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0]]
    print(edmonds_karp_algoritm(matrix, 0, 8))


if __name__ == '__main__':
    main()
