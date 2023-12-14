import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
import sys


def algorithm_unoptimized_buid(graph, starting_nodes, _final_vertices):
    visited = {s_i: [] for s_i in starting_nodes}
    open = Queue()
    for s in starting_nodes:
        open.put(s)

    while not open.empty():
        current_node = open.get()
        for n in graph.neighbors(current_node):
            if n not in visited:
                visited[n] = [current_node]
            else:
                parents = visited[n]
                parents.append(current_node)
                visited[n] = parents
    return visited


def dict_to_networkx_graph(graph_dict):
    G = nx.Graph()
    for node, neighbors in graph_dict.items():
        G.add_node(node)
        G.add_edges_from((node, neighbor) for neighbor in neighbors)

    return G


def handle_graph_unoptimized(graph, starting_nodes, final_vertices):
    g = algorithm_unoptimized_buid(graph, starting_nodes, final_vertices)
    nx_g = dict_to_networkx_graph(g)
    cycles = list(nx.simple_cycles(nx_g))
    if len(cycles) > 0:
        for cycle in cycles:
            print(cycle, file=sys.stderr)
        return False
    else:
        return True


def get_random_graph_with_starting_vertices(n=10, p=0.3, n_starting_vertices=2, n_final_vertices=2, seed=None):
    # Generate a random graph with 10 nodes
    g = nx.gnp_random_graph(n, p, directed=True, seed=seed)
    nodes = list(g.nodes())
    starting_vertices = nodes[:n_starting_vertices].copy()
    final_vertices = nodes[n_starting_vertices:(n_starting_vertices + n_final_vertices)].copy()
    return g, starting_vertices, final_vertices

def simulate(n_simulations=100, initial_seed=42):
    seed = initial_seed
    for i in range(n_simulations):
        g, starting, final = get_random_graph_with_starting_vertices(seed=seed)
        if not handle_graph_unoptimized(g, starting, final):
            sys.exit(1)
        seed += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulate(100, 42)
