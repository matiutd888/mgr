# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import networkx as nx
import matplotlib.pyplot as plt


def

def hello_world():
    # Generate a random graph with 10 nodes
    G = nx.gnp_random_graph(10, p=0.3)

    # Plot the graph
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_world()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
