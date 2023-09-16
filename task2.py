import time
print("man makes plans")


def Task2():
	start = time.time()
	#Store data
	store = set()
	freq_dict = {}
	with open("task12distinctnumbers.txt", 'r') as file:
		for line in file:
			for word in line.split():
				store.add(word)
				if word in freq_dict:
					freq_dict[word] = freq_dict[word] + 1
				else:
					freq_dict[word] = 1


	#Perform operations
	with open("task12operations.txt", 'r') as file:
		for line in file:
			words = line.split()
			operation = words[0]
			val = words[1]
			if "1" == operation:
				rs = val in store
			if operation == "2":
				store.add(val)
				if val in freq_dict:
					freq_dict[val] = freq_dict[val] + 1
				else:
					freq_dict[val] = 1

			if operation == "3":
				if freq_dict[val] == 0:
					store.remove(val)
				else:
					freq_dict[val] = freq_dict[val] - 1
	end = time.time()
	elapsed = end - start
	print("Task 2 took: ", elapsed, " seconds")

Task2()

