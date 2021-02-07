import redis
import json

redisClient = redis.Redis(host='localhost', port=6379, db=0)

def saveRunning(networkCandidate):
	if networkCandidate == None:
		print("Error in saveRunning.")
		return -1
	ret = redisClient.lpush('Running', networkCandidate)

def getRunning():
	nts = redisClient.rpop('Running')
	if nts == None:
		return {}
	networkRunning = json.loads(nts.decode("utf-8"))
	return networkRunning

def getSizeOfRunning():
	size = redisClient.llen('Running')
	return size
