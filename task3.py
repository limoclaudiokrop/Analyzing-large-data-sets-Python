import multiprocessing
import time
def readTask3Data():
	data = []
	file = open("task13text.txt", encoding="utf8")
	for line in file:
		for word in line.split():
			data.append(word) 
	return data

def freq_linear(name, q, data):
	
	freq = 0
	for word in data:
		if word == name:
			freq = freq + 1

	q.put((name, freq))




def print_queue(q):
	f = open("task13Solution.txt", "w")
	
	content = ""
	while not q.empty():
		temp = q.get()
		f.write(temp[0] + " " + str(temp[1]) + "\n")
	f.close()



def readTask3Names():
	names = []
	file = open("task13names.txt", encoding="utf8")
	for line in file:
		for word in line.split():
			names.append(word)

	return names

if __name__ == "__main__":
	# input list
	start = time.time()

	data = readTask3Data()

	names = readTask3Names()
	# creating multiprocessing Queue
	q = multiprocessing.Queue()
	# creating new processes
	for name in names:
		p1 = multiprocessing.Process(target=freq_linear, args=(name, q, data))
		p1.start()
		p1.join()

	p2 = multiprocessing.Process(target=print_queue, args=(q,))

	p2.start()
	p2.join()
	end = time.time()
	elapsed = end - start
	print("Task 3 took: ", elapsed, " seconds")

