import networkx as nx

G = nx.Graph()

G.add_node(1) # how to add a node

G.add_nodes_from([2, 3]) # add multiple nodes...

H = nx.path_graph(10)
G.add_nodes_from(H) #Adds nodes from an nbunch
G.add_node(H) # H itself as a node. (graph of graph)

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)

G.add_edges_from([(1, 2), (1, 3)]) #exact format of my namedtuple

G.add_edges_from(H.edges()) #add from edges in H

# ADD AN EBUNCH OF EDGES. Contains dictionary of attributes. This would
# work for transfer ammount

[(2,3,{'bitcoins':3.1415, 'coinbase':False}),
 (2,3,{'bitcoins':3.1415, 'coinbase':False})
 ]

G.remove_node(H)


Attributes
>>> G.add_node(1, time='5pm')
>>> G.add_nodes_from([3], time='2pm')
>>> G.node[1]
{'time': '5pm'}
>>> G.node[1]['room'] = 714
>>> G.nodes(data=True)
[(1, {'room': 714, 'time': '5pm'}), (3, {'time': '2pm'})]




>> G.add_edge(1, 2, weight=4.7 )
>>> G.add_edges_from([(3,4),(4,5)], color='red')
>>> G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
>>> G[1][2]['weight'] = 4.7
>>> G.edge[1][2]['weight'] = 4


direct graph
>>> DG=nx.DiGraph()
>>> DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
>>> DG.out_degree(1,weight='weight')
0.5
>>> DG.degree(1,weight='weight')
1.25
>>> DG.successors(1)
[2]
>>> DG.neighbors(1

## CAn edges have a value attribute?
##
