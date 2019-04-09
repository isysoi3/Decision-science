def nearest_neighbour(matrix):
    visited = [0]
    currentVertex = 0
    sum = 0
    for i in range(9):
        min = 1000
        indexOfMin = 0
        for index, element in enumerate(matrix[currentVertex]):
            if min > element and index not in visited:
                min = element
                indexOfMin = index
        visited.append(indexOfMin)
        sum += min
        currentVertex = indexOfMin
    return visited


def calculateRouteValue(route, matrix):
    sum = 0
    for i in range(len(route) - 1):
        # print(matrix[route[i]][route[i+1]])
        sum += matrix[route[i]][route[i + 1]]
    return sum


def twoOptSwap(route, i, k):
    tmp = route[i]
    route[i] = route[k]
    route[k] = tmp
    return route


def main():
    matrix = [
        [0, 5, 3, 8, 6, 7, 2, 1, 3, 4],
        [5, 0, 9, 7, 4, 2, 3, 4, 1, 3],
        [3, 9, 0, 1, 2, 4, 3, 5, 6, 7],
        [8, 7, 1, 0, 7, 2, 3, 4, 5, 8],
        [6, 4, 2, 7, 0, 3, 6, 7, 8, 9],
        [7, 2, 4, 2, 3, 0, 2, 1, 5, 6],
        [2, 3, 3, 3, 6, 2, 0, 9, 1, 3],
        [1, 4, 5, 4, 7, 1, 9, 0, 5, 4],
        [3, 1, 6, 5, 8, 5, 1, 5, 0, 8],
        [4, 3, 7, 8, 9, 6, 3, 4, 8, 0]]

    route = nearest_neighbour(matrix)
    numberOfVertex = 10

    for i in range(100):
        bestDistance = calculateRouteValue(route, matrix)
        for i in range(numberOfVertex):
            for k in range(i + 1, numberOfVertex):
                newRoute = twoOptSwap(route, i, k)
                distanceRoute = calculateRouteValue(newRoute, matrix)
                if distanceRoute < bestDistance:
                    route = newRoute
                    bestDistance = distanceRoute
                    print(bestDistance, route)
    print(calculateRouteValue(route, matrix), route)


if __name__ == '__main__':
    main()
