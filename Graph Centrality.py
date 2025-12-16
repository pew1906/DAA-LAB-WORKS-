#Assignment 04: Social Network Analysis Using Graph Centrality Measures
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

influencers = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

G.add_nodes_from(influencers)

edges = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "David"),
    ("David", "Eva"),
    ("Eva", "Frank"),
    ("Charlie", "Frank")
]
G.add_edges_from(edges)

shortest_path = nx.shortest_path(G, source="Alice", target="Frank")
print("Shortest path from Alice to Frank:", shortest_path)

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

print("\nDegree Centrality:", degree_centrality)
print("\nBetweenness Centrality:", betweenness_centrality)
print("\nCloseness Centrality:", closeness_centrality)
print("\nEigenvector Centrality:", eigenvector_centrality)

plt.figure(figsize=(7,5))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Influencer Graph")
plt.show()
