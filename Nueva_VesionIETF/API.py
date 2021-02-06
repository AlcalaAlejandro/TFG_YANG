import requests
import json

def anadir_link_network (network, link):

	if network != {} and link != {}:
		network["ietf-network-topology:link"].append(link)
	else:
		print("Error en los parámetros de entrada.")

	return network

def crear_link_network (link_id, source_node, source_tp, dest_node, dest_tp, network_type):
	dicc = {}
	source = {}
	dest = {}
	network_types = {}

	if link_id != "" and  source_node != "" and source_tp != "" and dest_node != "" and dest_tp != "" and network_type != "":
		dicc["link-id"] = link_id
		source["source-node"] = source_node
		source["source-tp"] = source_tp
		dest["dest-node"] = dest_node
		dest["dest-tp"] = dest_tp
		dicc["source"] = source
		dicc["destination"] = dest
		network_types["isolation-level"] =  network_type
		dicc["ietf-network-slice:network-slice"] = network_types
	else:
		print("Error en los parámetros de entrada.")

	return dicc

def crear_nodo_network (network_id, network_point, network_type):
	dicc = {}
	termination_point = {}
	network_types = {}

	if network_id != "" and network_point != "" and network_types != "":
		dicc["node-id"] = network_id
		network_types["isolation-level"] =  network_type
		dicc["ietf-network-slice:network-slice"] = network_types
		dicc["ietf-network-topology:termination-point"] = []
		termination_point["tp-id"] = network_point
		dicc["ietf-network-topology:termination-point"].append(termination_point)
	else:
		print("Error en los parámetros de entrada.")

	return dicc


def crear_network (network_id, network_type):
	dicc = {}
	network_types = {}

	if network_id != ""  and network_type != "":
		dicc["network-id"] = network_id
		dicc["network-types"] = {"ietf-network-slice:network-slice" : {}}
		dicc["node"] = []
		dicc["ietf-network-topology:link"] = []
		network_types["isolation-level"] = network_type
		dicc["ietf-network-slice:network-slice"] = network_types
	else:
		print("Error en los parámetros de entrada.")

	return dicc


def anadir_endpoint_network(network, endpoint):

	if network != {} and endpoint != {}:
		network["node"].append(endpoint)
	else:
		print("Error en los parámetros de entrada.")

	return network

def anadir_red(network):
	networks = {}
	nets = []

	if network != {}:
		nets.append(network)
		networks["ietf-network:networks"] = {"network": nets}

	else:
		print("Error en los parámetros de entrada.")

	return networks

def post_network_slice(bodyParam):
	headers = {'content-type':'application/yang-data+json'}
	body = json.dumps(bodyParam, indent=4)
	ret = requests.post('http://localhost:8080/data/networks/',json=body)
	return ret.json()

def get_network_slice():
	ret = requests.get('http://localhost:8080/data/networks/')
	return ret.json()

def delete_network_slice():
	ret = requests.delete('http://localhost:8080/data/networks/')
	return ret.json()