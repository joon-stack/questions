def solution(n, vertex):
    # make adjacency list and distance dictionary
    graph, distance = {}, {}
    for i in range(1, n+1):
        graph[str(i)] = []
        # for Dijkstra algorithm
        distance[str(i)] = float('inf')
    distance['1'] = 0
    # undirected edges
    for v in vertex:
        graph[str(v[0])].append(str(v[1]))
        graph[str(v[1])].append(str(v[0]))
    # to reduce time complexivity of operator 'in', used set
    # set, dict: O(1) (use hash) / list, tuple: O(n)
    visited, need_visit = set(), list()
    need_visit.append(str(1))
    # Dijkstra algorithm with same weight 1
    # used queue because it has no weights
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.add(node)
            need_visit.extend(graph[node])
            for n in graph[node]:
                # compare distances
                distance[n] = min(distance[n], distance[node] + 1)
    # find max distance and count nodes that have the max distance
    maxDist = 0
    count = 0
    for key in distance:
        maxDist = max(maxDist, distance[key])
    for key in distance:
        if maxDist == distance[key]:
            count += 1
    return count