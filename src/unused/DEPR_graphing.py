import networkx as nx
from collections import namedtuple


def create_nodes(node_tuples):
    """Takes a list of tuples in the form
    [(txout, txin, value), ...]
    """

    DG = nx.DiGraph()




if __name__ == "__main__":

    E = namedtuple("Edge", ['TXOUT', 'TXIN'])

    test_edges = [
        E('tx1', 'tx2'),
        E('tx2', 'tx4'),
        E('tx2', 'tx3')
    ]

    for i in test_edges:
        print i.txout, i.txin




#NETWORKX, THEN GEPHI OR GRAPHLAB
