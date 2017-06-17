from json_fmt import trace_transaction
import networkx as nx
import os
import cpickle


def get_graph(filename):
    relative_dir = "../graphs/" + filename + ".pkl"
    direc = os.path.dirname(__file__)
    filedir = os.path.join(direc, relative_dir)

    return cpickle.load(filedir)

def store_graph(graph):
    relative_dir = "../graphs/" + graph.__name__ + ".pkl"
    direc = os.path.dirname(__file__)
    filedir = os.path.join(direc, relative_dir)

    with open(filedir, 'w') as f:
    cpickle.dump(graph, filedir)

def build_graph(txid, depth):
    ebunch = get_transaction(txid, depth)

    DG = nx.DiGraph()
    DG.add_edges_from(ebunch)
    store_graph(DG)

def analyze_graph(graphname):

