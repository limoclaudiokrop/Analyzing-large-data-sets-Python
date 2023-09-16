import time
print("man makes plans")

def readTask1(filename):
	arr = []
	with open(filename, 'r') as file:
		for line in file:
			for word in line.split():
				arr.append(word)

	return arr

def removeDuplicates(arr):
	#Get frequencies of items
	freq_dict = {}
	for i in arr:
		if i in freq_dict:
			freq_dict[i] = freq_dict[i] + 1
		else:
			freq_dict[i] = 1


	#Calculate index of element in frequency
	for val in freq_dict:
		freq_dict[val] = freq_dict[val]//2

	result = []
	counter_dict = {}
	for i in arr:
		if i in counter_dict:
			counter_dict[i] = counter_dict[i] +1
		else:
			counter_dict[i] = 0

		if counter_dict[i] == freq_dict[i]:
			result.append(i)

	return result

def Task1WriteFile(arr):
	content = ""
	for val in arr:
		content = content + val + " "
	f = open("task11Solution.txt", "w")
	f.write(content)
	f.close()

def Task1():
	start = time.time()
	filename = "task11numbers.txt"
	arr = readTask1(filename)
	arr = removeDuplicates(arr)
	Task1WriteFile(arr)
	end = time.time()
	elapsed = end - start
	print("Task 1 took: ", elapsed, " seconds")
Task1()