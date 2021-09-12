import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


def buildGraph():
    print("Let's construct a Graceful Labelling:")

    decision = input("Input graph from file? (y/n) ")

    if decision == 'y':
        data = open("input.txt", 'r')

        G = nx.Graph()
        length = data.readline()
        for n in range(int(length)):
            G.add_node(str(n))

        while True:
            edge = data.readline()
            if edge == "":
                print(G.nodes())
                print(G.edges())
                return G
            else:
                first, second = edge.split(',')
                G.add_edge(first,second)

    vCount = input("How many vertices? ")

    G = nx.Graph()
    for n in range(int(vCount)):
        G.add_node(str(n))

    finished = False
    while ~finished:
        edge = input("Enter an edge 'm,n' or type 'stop': ")
        if edge == "stop":
            print("Graph finished c:")

            #print(G.number_of_nodes())

            #nx.draw_planar(G, with_labels = True, node_color = 'white', node_size = 500)
            #plt.savefig("graph.png")
            #plt.clf()

            #G.clear()
            #nx.draw(G)
            #input("Finished?")

            return G
        else:
            first, second = edge.split(',')
            G.add_edge(first,second)
    return

def findGrace():
    n = 0
    graph = buildGraph()

    vertices = [0]*graph.number_of_nodes()
    for i in range(graph.number_of_nodes()):
        vertices[i] = i

    labelings = list(permutations(vertices))

    for labeling in labelings:
        map = {}
        inv_map = {}
        edgeLabeling = {}

        for i in range(len(labeling)):
            map[str(i)] = labeling[i]
            inv_map[labeling[i]] = str(i)

        graph = nx.relabel_nodes(graph, map)

        for edge in graph.edges():
            edgeLabeling[edge] = str(abs(int(edge[0])-int(edge[1])))

        if len(edgeLabeling.values()) == len(set(edgeLabeling.values())):
            print("Found one!")

            #print(str(n) + ':')
            #print(labeling)

            nx.draw_planar(graph, with_labels = True, node_color = 'white', node_size = 500)
            nx.draw_networkx_edge_labels(graph,nx.planar_layout(graph),edgeLabeling,font_color='red')
            plt.savefig("graph"+str(n)+".png")
            plt.clf()

            graph.clear()
            #nx.draw(graph)

            return

        graph = nx.relabel_nodes(graph, inv_map)
        #print(graph.edges())

    print("And that's all the labelings... phew!")
    return


findGrace()
