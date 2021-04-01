import Candidate
import Running
import json
import time
import os

def checkNetworkSlice ():
	running = True
	node_json = {}

	if getCandidateOrchestrator == 0:
		print("Error in checkNetworkSlice.")
	networkSlice = Candidate.getCandidate()

	if len(networkSlice["ietf-network:networks"]) == 0:
		print("Error in checkNetworkSlice. Length is zero")
		return -1

	if "network" in networkSlice["ietf-network:networks"]:
		for network in networkSlice["ietf-network:networks"]["network"]:
			nodes_id = []
			print("Network-id: "+ str(network["network-id"]))
			print("Nodes of Network:")
			if "node" in network:
				port = {}
				node_json.clear()
				for node in network["node"]:
					print("\t Node id: "+ str(node["node-id"]))
					if "ietf-network-topology:termination-point" in node:
						for tp in node["ietf-network-topology:termination-point"]:
							print("\t Termination Point id: "+ str(tp["tp-id"]))
							nodes_id.append(str(tp["tp-id"]))
					for n in nodes_id:
						if os.path.exists(str(n)) == False:
							os.mkdir(str(n))
						node_json["device_id"] = str(n)
						node_json["va_log_level"] = "INFO"
						node_json["nevi_log_leve"] = "INFO"
						node_json["ports"] = []
						port["autoneg"] = False
						port["mtu"] = 1500
						port["admin_status"] = "up"
						port["ports"] = 1
						port["ports"] = ["10G", "1G"]
						node_json["ports"].append(port)


						with open(str(n)+'/device-setup.json', 'w') as file:
							json.dump(node_json, file, indent = 4)
			else:
				running = False

			if "ietf-network-topology:link" in network:
				for link in network["ietf-network-topology:link"]:
					print("\t Link id: "+ link["link-id"])
					print("\t Link Source Node:"+ link["source"]["source-node"])
					print("\t Link Source TP:"+ link["source"]["source-tp"])
					print("\t Link Destination Node:"+ link["destination"]["dest-node"])
					print("\t Link Destination TP:"+ link["destination"]["dest-tp"])
			else:
				running = False
	else:
		running = False
		print("Error in Network Slice.")

	if running == True:
		print("******* AQUI VENDRÍAN LAS LLAMADAS A VOLTA. ********")
		sendToRunnig(networkSlice)

def getCandidateOrchestrator():

	if Candidate.getSizeOfCandidate != 0:
		networkCandidate = Candidate.getCandidate()
		return networkCandidate

def sendToRunnig(networkCandidate):
	if networkCandidate == None:
		print("Error in sendToRunnig.")
		return -1
	Running.saveRunning(json.dumps(networkCandidate))
