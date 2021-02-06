import API
import json

def main():

	# Creamos los endpoints de nuestra red
	endpoint1 = API.crear_nodo_network("DCSG-3", "220", "ietf-network-slice:physical-memory-isolation")
	print("---- DEVICE 220 ----")
	print(json.dumps(endpoint1, indent = 4))
	endpoint2 = API.crear_nodo_network("DCSG-5", "6", "ietf-network-slice:physical-memory-isolation")
	print("---- DEVICE 6 ----")
	print(json.dumps(endpoint2, indent = 4))
	#endpoint3 = API.crear_endpoint_slice(3, "endpoint3", "any-to-any-role")
	#print("---- ENDPOINT 3 ----")
	#print(json.dumps(endpoint3, indent = 4))

	#Creamos los enlances entre los endpoints
	link1 = API.crear_link_network("DCSG-3,220,,", "VR1", "220", "DCSG-5", "6", "ietf-network-slice:physical-memory-isolation")
	print("---- LINK DEL DEVICE ID 220 AL DEVICE ID 6 ----")
	print(json.dumps(link1, indent = 4))
	#link2 = API.crear_link_slice(23, 2, 3)
	#print("---- LINK 2 ----")
	#print(json.dumps(link2, indent = 4))
	#link3 = API.crear_link_slice(31, 3,1)
	#print("---- LINK 3 ----")
	#print(json.dumps(link3, indent = 4))


	# Creamos la network-slice
	network = API.crear_network("example-customized-blue-topology","ietf-network-slice:physical-memory-isolation")
	print("---- NETWORK ----")
	print(json.dumps(network, indent = 4))


	#Añadimos los endpoint a la network slice
	network = API.anadir_endpoint_network(network, endpoint1)
	print("---- NETWORK SLICE CON DEVICE 220 ----")
	print(json.dumps(network, indent = 4))
	network = API.anadir_endpoint_network(network, endpoint2)
	print("---- NETWORK SLICE CON DEVICE 6 ----")
	print(json.dumps(network, indent = 4))
	#networkslice1 = API.anadir_endpoint_network_slice(networkslice1, endpoint3)
	#print("---- NETWORK SLICE CON ENDPOINT 3 ----")
	#print(json.dumps(networkslice1, indent = 4))


	# Añadimos los link a la network slice
	network = API.anadir_link_network(network, link1)
	print("---- NETWORK SLICE CON LINK DEVICE 220 TO DEVICE 6 ----")
	print(json.dumps(network, indent = 4))
	#networkslice1 = API.anadir_link_network_slice(networkslice1, link2)
	#print("---- NETWORK SLICE CON LINK 2 ----")
	#print(json.dumps(networkslice1, indent = 4))
	#networkslice1 = API.anadir_link_network_slice(networkslice1, link3)
	#print("---- NETWORK SLICE CON LINK 3 ----")
	#print(json.dumps(networkslice1, indent = 4))

	#Creamos la lista de redes a subir al servidor
	networks = API.anadir_red(network)
	print("---- AÑADIDA LA PRIMERA NETWORK ----")
	print(json.dumps(networks, indent = 4))

	# Crearemos el body de la llamada
	#body = API.crear_body_servidor(networkslice1)
	#print("---- CUERPO DE LA LLAMADA ----")
	#print(json.dumps(body, indent = 4))

	with open('device-setup.json', 'w') as file:
		json.dump(networks, file, indent = 4)


	# Hacemos la petición POST
	ret = API.post_network_slice(networks)
	print("---- RESPUESTA DEL SERVIDOR POST ----")
	print(ret)
	# Hacemos la petición GET
	ret = API.get_network_slice()
	print("---- RESPUESTA DEL SERVIDOR GET ----")
	print(ret)
	# Hacemos la petición DELETE
	ret = API.delete_network_slice()
	print("---- RESPUESTA DEL SERVIDOR DELETE ----")
	print(ret)
	# Hacemos la petición GET
	ret = API.get_network_slice()
	print("---- RESPUESTA DEL SERVIDOR GET ----")
	print(ret)

if __name__ == '__main__':
	main()