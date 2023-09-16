# Analyzing-large-data-sets-Python

### Report Task 1.1
Problem in this task involves reading a big amount of numbers and removing duplicate
numbers. Note that removing duplicate numbers follows a special rule where only the middle
element is retained. To complete this task, the values are read in from file into an array. A
python dictionary named freq_dict is created to store the numbers. Where the key is the number
itself and the value is the frequency of the number. After these values are read in, another
dictionary is created, named conter_dict. This dictionary saves the number as the key and the
position of the middle element as the value. Note that the position of the middle element is
calculated as n//2 where n is the frequency (obtained from the freq_dict). Finally the array
containing elements is iterated and only the number at the index indicated by the counter_dict
dictionary is appended to the final array. The array with all the duplicated elements removed is
obtained in the final array. Python dictionary data structure is chosen for this problem since it is
implemented with a hash map. Therefore inserting and accessing elements takes O(1). The
total time complexity for this task is O(n), where n is the number of elements in the file.

### Report Task 2.2
In this task, we are requested to come up with an efficient algorithm to read in two files. One file
containing numbers and another containing operations to be done. Operations include
searching, inserting and deleting elements. To complete this task, two data structures are used
i.e python set and python dictionary. When the values are read from the file, the number is
inserted into a set. Additionally the number is also added to the dictionary where the key is the
number and the value is the frequency of the number. To perform a search, built-in search for a
set is used to check if the number exists. To perform insert, the number to insert is first checked
if it exists in the dictionary, if so, the value of the number in the dictionary(its frequency) is
incremented. If the value does not exist, the value is added to the dictionary with value of 1 and
also inserted into the set. To delete a number, the number is removed from the set and its value
is decremented in the dictionary. Note that the number is only deleted in the set if its frequency
in the dictionary is equal to 1. A python set allows insertion, deletion and searching to be done
in O(1). However since a set does not support duplicate elements, a dictionary is used to check
if the frequency of the element has reached 0 before removing it. Furthemore, since the
dictionary allows O(1) for adding and lookup of elements, the entire algorithm takes O(n + k)
where n is the number of elements in the file and k is the number of operations.
### Report Task 2.3
This task involves using parallelism to find frequencies of words in a large text file. To
accomplish this, the algorithm first reads the text file and stores it as a list of words. It then reads
the words (to find their frequencies) into another list. The main function then creates processes
for each word(to be looked for its frequency). Each process takes in the list of words in the text
file, the word to find its frequency and a queue. Each process then runs a method that uses
linear search to find the frequency of the given word in the text file. After the frequency has been
evaluated, the result is saved into the queue. Additionally, another process is created which
keeps removing elements in the queue and writing it out to file until the queue is empty.
