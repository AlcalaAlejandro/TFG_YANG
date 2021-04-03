import Network_Slice_Orchestrator as NSO
import threading
import Candidate

def Orchestrator():
	while True:
		if Candidate.getSizeOfCandidate() > 0:
			NSO.checkNetworkSlice()
def main():
	hiloOrchestrator = threading.Thread(target=Orchestrator)
	#hiloGet = threading.Thread(target=getNetworkSlice)
	hiloOrchestrator.start()
	#hiloGet.start()
if __name__ == '__main__':
	main()