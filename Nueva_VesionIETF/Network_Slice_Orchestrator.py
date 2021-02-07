import Candidate
import Running
import json
import time

def checkNetworkSlice ():
	running = True

	if getCandidateOrchestrator == 0:
		print("Error in checkNetworkSlice.")
	networkSlice = Candidate.getCandidate()

	if len(networkSlice["ietf-network:networks"]) == 0:
		print("Error in checkNetworkSlice. Length is zero")
		return -1

	if "network" in networkSlice["ietf-network:networks"]:
		for network in networkSlice["ietf-network:networks"]["network"]:
			print("Network-id: "+ str(network["network-id"]))
			print("Nodes of Network:")
			if "node" in network:
				for node in network["node"]:
					print("\t Node id: "+ str(node["node-id"]))
					if "ietf-network-topology:termination-point" in node:
						for tp in node["ietf-network-topology:termination-point"]:
							print("\t Termination Point id: "+ str(tp["tp-id"]))
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
