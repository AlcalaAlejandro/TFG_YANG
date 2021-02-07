import redis
import json
import hashlib

redisClient = redis.Redis(host='localhost', port=6379, db=0)

def saveCandidate(networkSlice):
	ret = redisClient.lpush('Candidate', networkSlice)

def getCandidate():
	nts = redisClient.rpop('Candidate')
	if nts == None:
		return {}
	networkSlice = json.loads(nts.decode("utf-8"))
	return networkSlice

def getSizeOfCandidate():
	size = redisClient.llen('Candidate')
	return size