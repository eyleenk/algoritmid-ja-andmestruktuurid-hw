def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Näite sõnastikust
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A' # Alguspunkt

# Käivitus
dfs(graph, start_node)

#Ajakompleksus: O(V + E), kus V on tippude arv (verticles, kuna tegu graafiga) ja E on servade arv.
#Ruumikompleksus: O(V), kus V on tippude arv.