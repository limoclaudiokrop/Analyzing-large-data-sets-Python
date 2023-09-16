import csv
import time
def readCountryCodes():
	filename = "task14countries.csv"
	csv_file = open(filename) 
	csv_rdr = csv.reader(csv_file) 
	codes = {}
	index = 0
	names = []
	for rec in csv_rdr: 
		col1, col2 = rec 
		codes[col2] = (col1, index)
		index = index + 1
		names.append(col2)
	

	return codes,names

def readFlights(codes):
	filename = "task14flights.csv"
	csv_file = open(filename) 
	csv_rdr = csv.reader(csv_file) 
	flights = []
	adj_matrix = []
	numItems = len(codes)
	for i in range(numItems):
		temp = []
		for j in range(numItems):
			temp.append(-1)
		adj_matrix.append(temp)

	for rec in csv_rdr: 
		col1,col2,col3 = rec
		row = codes[col1][1]
		col = codes[col2][1]
		adj_matrix[row][col] = int(col3)
	
	return flights, adj_matrix

def dijikstra(adj_matrix, source, destination):
	dist = {}
	prev = {}
	q = []
	visited = {}
	numVerts = len(adj_matrix[0])
	for i in range(numVerts):
		dist[i] = float('inf')
		prev[i] = None
		visited[i] = False
		q.append(i)

	dist[source] = 0

	for w in range(numVerts):
		v_u = -1
		minDist = float('inf')
		for i in range(numVerts):
			if visited[i] == False and dist[i] < minDist:
				v_u = i
				minDist = dist[i]
		
		
		visited[v_u] = True

		if v_u == destination:
			break;

		for i in range(numVerts):
			#find neigbors
			if adj_matrix[v_u][i] != -1 and not visited[i]:
				temp = dist[v_u] + adj_matrix[v_u][i]
				if dist[v_u] != float('inf') and temp < dist[i]:
					dist[i] = temp
					prev[i] = v_u

		
	
	s = []
	u = destination
	while u is not None:
		s.insert(0,u)
		u = prev[u]

	
	return dist[destination], s


def Task4():
	codes,names = readCountryCodes()
	flights, adj_matrix = readFlights(codes)
	
	origin = input("Enter origin location\n")

	if origin not in codes:
		print("Location entered does not exist")
	destination = input("Enter destination\n")

	if origin not in codes:
		print("Location entered does not exist")

	start = time.time()
	source = codes[origin][1]
	target = codes[destination][1]

	cost, route = dijikstra(adj_matrix, source, target)
	print("\n\nDeparture: ", origin, " Destination: ", destination)
	print("Flight cost: ", cost)
	content = ""
	for r in route:
		#print(names[r])
		#print(codes[names[r]])
		content = content + " " + names[r] + "(" + codes[names[r]][0] + ") ->"

	content = content[:-2]
	print("Route: ", content, "\n\n")
	end = time.time()
	elapsed = end - start
	print("Task 4 took: ", elapsed, " seconds")
Task4()