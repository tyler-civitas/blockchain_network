import json
import pickle
from get_data import node_rpc
from time import sleep
from collections import namedtuple
import networkx as nx


def store_response(decoded_json):

    error = decoded_json.get(u"error", None)
    if error:
        mess = error.get(u"message", "no message")
        print "Error : {}".format(mess)

    name = decoded_json.get(u"id", "No ID Found") + ".pkl"
    data = decoded_json.get(u"result", "No Results")

    with open(name, "w") as f:
        pickle.dump(data, f)

def load_response(path):

    with open(path, "r") as f:
        data = pickle.load(f)

    return data

def get_transaction(hex_txid):

    p = [hex_txid, True]
    decoded_json = node_rpc(
        rpc_id=1,
        verbose=True,
        cmd=u"getrawtransaction",
        params=p
                           )
    return decoded_json[u'result']

def get_block_hash(height):

    p = [height]
    decoded_json = node_rpc(
        rpc_id=1,
        verbose=True,
        cmd=u"getblockhash",
        params=p
                            )
    return decoded_json[u'result']


def get_block(header_hash):

    p = [header_hash, True]
    decoded_json = node_rpc(
        rpc_id=1,
        verbose=True,
        cmd=u"getblock",
        params=p
                            )
    return decoded_json[u'result']


def trace_transaction(hex_txid, outidx=None, outtxid=None, distance=5):

    print "Recursion Layer {}".format(distance)
    if distance == -1:
        return None

    sleep(2)
    result = get_transaction(hex_txid)

    if result == None: #################NEED TO ADD SUPPORT FOR COINBASE
        print "Transaction Not Found"
        return None


    DG = nx.DiGraph()

    # Populate Graph with current transaction and output addresses
    # For the TXID we recursively arrived from, use the TXID
    for i, out in enumerate(result[u'vout']):
        addresses = str(out[u'scriptPubKey'][u'addresses'])
        value = out[u'value']
        transaction = False
        if i == outidx:
            addresses = outtxid
            transaction = True

        print "Adding edge, {}, {}, {}".format(hex_txid, addresses, value)
        DG.add_edge(hex_txid, addresses, weight=value)
        DG.edge[hex_txid][addresses]['transaction'] = transaction

    # Recursively go back into all VIN transactions
    for vin in result[u'vin']:
        #print type(vin)
        if vin.get(u'coinbase', None):
            print "Coinbase transaction"
            DG.edge[hex_txid][outtxid]['coinbase'] = True
            newDG = None
        elif vin[u'txid']:
            input_hex_txid = vin[u'txid']
            newDG = trace_transaction(
                input_hex_txid,
                outidx=vin[u'vout'], #outpoint is simply the index number
                outtxid=hex_txid,
                distance=distance - 1)
        else:
            print "No coinbase or txid found"
            newDG = None

        if newDG:
            DG.add_edges_from(newDG)

    return DG.edges(data=True)



if __name__ == "__main__":
    # j = get_transaction(u'dd3bc0242502cccf0d24f1650fd398373ff68b43b366bacb0d481fe4323747fc')
    # ha = get_block_hash(470000)
    # print ha
    # j = get_block(ha)
    j = trace_transaction(u'dd3bc0242502cccf0d24f1650fd398373ff68b43b366bacb0d481fe4323747fc')
    print 'printing j'
    print j


    DG = nx.DiGraph()
    DG.add_weighted_edges_from(j)
    # DG.node[address]['TX'] = True
