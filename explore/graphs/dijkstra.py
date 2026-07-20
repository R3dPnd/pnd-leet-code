"""
Takes in an adjacency list representation of a graph and a source node, and returns the shortest path from the source to all other nodes using Dijkstra's algorithm.
"""
from turtle import distance


def dijkstra(adj, src):
    """
    Dijkstra's algorithm for finding the shortest path in a graph.
    This function is a placeholder and should be implemented with the actual algorithm.
    """

    # Initialize distances and priority queue
    distance = [sys.maxsize] * len(adj)
    distance[src] = 0
    pq = []

    # Add the source node to the priority queue
    pq.append((0, src))  # (distance, node)

    # while there are nodes to process, 
    while pq:
        d,u = pq.pop(0)  # Get the node with the smallest distance

        # If the distance is greater than the recorded distance, skip processing
        if d > distance[u]:
            continue
        
        # For each neighbor of the current node, update the distance if a shorter path is found
        for v, weight in adj[u]:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                pq.append((distance[v], v))  # Add the neighbor to the priority queue, basically processing each vector of the graph
    return distance