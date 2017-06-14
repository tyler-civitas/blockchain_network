import json
import pickle
from get_data import node_rpc
from time import sleep

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


def trace_transaction(hex_txid, distance=5):

    distanceless = distance - 1
    if distanceless == 0:
        return set()

    edges = set()
    sleep(2)
    result = get_transaction(hex_txid)
    print result

    if result == None:
        print "Transaction Not Found"
        return set()

############## SERVER ERRORS DUE TO REINDEXING NEEDED??? ######
### GET VALUES, MULTITRANSACTION BOOLEAN, ETC MULTIINPUT/MULTIOUTPUT ####

    for value in result[u'vin']:
        prev_hex_txid = value[u'txid']
        edges.add((prev_hex_txid, hex_txid))
        new = trace_transaction(prev_hex_txid, distance=distanceless)
        edges.update(new)

    return edges



if __name__ == "__main__":
    j = get_transaction(u'8ff670d6397969a4f8973a02938c06680485f6760e85d86809ae9ac53eb2bfac')
    # ha = get_block_hash(470000)
    # print ha
    # j = get_block(ha)
    # j = trace_transaction(u'dd3bc0242502cccf0d24f1650fd398373ff68b43b366bacb0d481fe4323747fc')
    print j
