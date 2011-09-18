"""Methods on the server that can be called from
the client by sending a POST request with a "request"
paramater that has a value of the name of the method"""
import pickle
import urllib

import ServerState

state = ServerState.ServerState()

def newProgram(requestHandler, clientData):
    requestHandler.send_response(200)
    requestHandler.send_header("Content-Type", "application/octet-stream")
    requestHandler.end_headers()
    requestHandler.wfile.write(open("TestProgram.exe", "rb").read())

def newRange(requestHandler, clientData):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-Type', 'text/plain')
    requestHandler.end_headers()
    range = state.nextData()
    data = (str(range[0]) + "\n" + str(range[1]) + "\n").encode("utf-8")
    requestHandler.wfile.write(data)

def reportValues(requestHandler, clientData):
    range = clientData.getvalue("computedRange")
    matchingValues = pickle.loads(urllib.parse.unquote_to_bytes(clientData.getvalue("matchingValues")))

    state.aggregateResults(matchingValues)

    requestHandler.send_response(200)
    requestHandler.end_headers()
