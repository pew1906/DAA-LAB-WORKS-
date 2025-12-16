# Assignment 08: Finding Connected Components Using Breadth-First Search

from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

graph = defaultdict(list)

edges = [(0,1), (1,2), (3,4), (5,6), (6,7)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def bfs(start, visited, graph):
    q = deque([start])
    component = []
    visited[start] = True
    while q:
        node = q.popleft()
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return component

def find_connected_components(graph):
    visited = defaultdict(bool)
    components = []
    for node in graph:
        if not visited[node]:
            comp = bfs(node, visited, graph)
            components.append(comp)
    return components

components = find_connected_components(graph)
print("Connected Components:", components)

G = nx.Graph()
G.add_edges_from(edges)

colors = ['skyblue', 'lightgreen', 'salmon', 'orange', 'violet']
node_colors = {}

for i, comp in enumerate(components):
    for node in comp:
        node_colors[node] = colors[i % len(colors)]

plt.figure(figsize=(6,4))
nx.draw(
    G, 
    with_labels=True, 
    node_color=[node_colors[node] for node in G.nodes()], 
    node_size=800, 
    font_weight='bold'
)
plt.title("Connected Components in Graph")
plt.show()