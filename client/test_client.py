from __future__ import print_function
import requests
import json
import sys
import jsonpickle


def getDiscovery(addr, debug=False):
    # prepare headers for http request
    headers = {'content-type': 'application/json'}
    text_json = "" #data to test
    # send http request with image and receive response
    response_url = addr + '/api/discovery'
    response = requests.post(response_url, data=text_json, headers=headers)
    return response

def getAggregateResult(addr, debug=False):
    # prepare headers for http request
    headers = {'content-type': 'application/json'}
    text_json = "" #data to test
    # send http request with image and receive response
    response_url = addr + '/api/aggregate_result'
    response = requests.post(response_url, data=text_json, headers=headers)
    return response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <server ip> <cmd>")
        print(f"where <cmd> is one of services discovery, aggregate_result")

    host = sys.argv[1] #localhost or from environment
    cmd = sys.argv[2] #the service to test
    
    addr = f"http://{host}:5000"

    print("Testing the {cmd} service")

    if cmd == 'discovery':
        response = getDiscovery(addr)
        print("Response is", response)
        print(json.loads(response.text))

    if cmd == 'aggregate_result':
        response = getAggregateResult(addr)
        print("Response is", response)
        print(json.loads(response.text))
