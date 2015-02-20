import json, requests

def getRPCId():
    return 1

def sendJSONRequest(method, params):
    data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":getRPCId()})
    response = requests.post("http://localhost:1337", data=data)
    jsondata = response.json()
    if 'result' in jsondata:
        return jsondata['result']
    else:
        return jsondata['error']

def eth_coinbase():
    return sendJSONRequest("eth_coinbase", [])


# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setCoinbase(coinbase):
    return sendJSONRequest("eth_setCoinbase", [coinbase])

def eth_listening():
    return sendJSONRequest("eth_listening", [])

# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setListening(listen): 
    return sendJSONRequest("eth_setListening", [listen])

def eth_mining():
    return sendJSONRequest("eth_mining", [])

# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setMining(mining):
    return sendJSONRequest("eth_setMining", [mining])

