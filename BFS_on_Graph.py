from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
    "X": []
}

def find_path(graph, start, goal):

    queue = deque([start])
    visited = [start]
    parents = {start: None}

    #BFS
    while (queue):
        current = queue.popleft()

        #goal found, stop searching
        if current == goal:
            break

        #keep searching
        for neighbor in graph[current]:
            if neighbor not in visited: 
                queue.append(neighbor)
                visited.append(neighbor)
                parents[neighbor] = current

    #path deconstruction
    path = []
    node = goal
    while (node is not None):
        path.append(node)
        node = parents[node]
    path.reverse()

    return(path)

print(find_path(graph, "A", "G"))
#print(find_path(graph, "A", "D"))
#print(find_path(graph, "C", "E"))
#print(find_path(graph, "A", "X"))
#print(find_path(graph, "A", "A"))