from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Näite sõnastik
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Alguspunkt
start_node = 'A'

# Käivitus
bfs(graph, start_node)

"""
Tipp 'A' on ühendatud tippudega 'B' ja 'C'
Tipp 'B' on ühendatud tippudega 'A', 'D' ja 'E'
Tipp 'C' on ühendatud tippudega 'A' ja 'F'
Tipp 'D' on ühendatud tippudega 'B'
Tipp 'E' on ühendatud tippudega 'B' ja 'F'
Tipp 'F' on ühendatud tippudega 'C' ja 'E'
Alguspunkt on 'A'. Trükib välja tipud külastamise järjekorras ehk A B C D E F
BFS otsingus külastatakse kõigepealt alguspunktist naabruses olevaid tippe, seejärel nende naabreid jne kuni kõik tipud on läbi käidud.
"""
