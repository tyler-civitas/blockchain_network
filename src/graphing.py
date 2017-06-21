from json_fmt import trace_transaction
import networkx as nx
import os
import cPickle
import matplotlib as plt

def get_graph(name):
    relative_dir = "../gexfs/" + name + ".gexf"
    direc = os.path.dirname(__file__)
    filedir = os.path.join(direc, relative_dir)

    return nx.read_gexf(filedir)
#    with open(filedir, 'r') as f:
#        return cPickle.load(f)

def store_graph(graph, name):
    relative_dir = "../gexfs/" + name + ".gexf"
    direc = os.path.dirname(__file__)
    filedir = os.path.join(direc, relative_dir)

    print "WRITING GRAPH"
    print "{} nodes".format(len(graph))
    nx.write_gexf(graph, filedir)
#    with open(filedir, 'w') as f:
#        cPickle.dump(graph, f)

def build_graph(txid, depth, name):
    ebunch, nbunch = trace_transaction(txid, distance=depth)

    DG = nx.DiGraph()
    DG.add_edges_from(ebunch)
    DG.add_nodes_from(nbunch)
    store_graph(DG, name)

def analyze_graph(graphname):
    DG = get_graph(graphname)
    UG = DG.to_undirected()
    print "-" * 50
    print "Graph: \t{}".format(graphname)
    print "-" * 50

    attributes = {
        #'connected_components'      : nx.connected_components(UG),
        'degrees of nodes'          : nx.degree(DG).values(),
        'clustering'                : nx.clustering(UG, 'weight'),
        'order'                     : DG.order(),
        'size'                      : DG.size(),
        }

    print attributes

def plot_graph(graphname):
    DG = get_graph(graphname)

    nx.draw(DG)
    plt.show()
    nx.draw_random(DG)
    plt.show()
    nx.draw_circular(DG)
    plt.show()
    nx.draw_spectral(DG)
    plt.show()

if __name__ == "__main__":
    name = 'block200k'
    tx = u'dd3bc0242502cccf0d24f1650fd398373ff68b43b366bacb0d481fe4323747fc'
    #build_graph(tx, 10, name)
    name = 'block400k'
    tx = u'ee475443f1fbfff84ffba43ba092a70d291df233bd1428f3d09f7bd1a6054a1f'
    #build_graph(tx, 10, name)
    #g = get_graph(name)
    #analyze_graph(name)
    #plot_graph(name)

    name = 'block100k'
    tx = u'6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4'
    #build_graph(tx, 10, name)

    name = 'block350k'
    tx = u'5415ab4217b1eeb6e74f60b2b86e40b51cb55e828c2cbda52cd40cb2589d670b'
#    build_graph(tx, 30, name)

    name = 'block450k'
    tx = u'2c14fbd463a6a1f37ef2507b71f2bd2a5b78391602c4bd20c6b86a5537bedd95'
    #build_graph(tx, 15, name)

    name = '2_5mil472152'
    tx = u'447db4813aec4234a33f0f5d1cd7d4c986997cf57136d15cc6bdbf0bf7a5c265'
    #build_graph(tx, 20, name)

    name = "Ryan1"
    tx = u'e8ba04049ef3bee2f639e8fedc51a91ddd7f6961f6ba06b7ecbfeaaa98dadae2'
    build_graph(tx, 5, name)

    name = "Ryan2"
    tx = u'ccab13c0b5fc3be5b10fa1520fb870b50d1b032d5608d2ed887f07fa1d0e3ce1'
    build_graph(tx, 5, name)
