class KeyValue:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashTable:
	SIZE = 6
	def __init__(self):
		self.array = []
		for i in range(0, self.SIZE):
			self.array.append([])	
	
	def lookup_number(self , key):
		h = self.hash(key)
		bucket = self.array[h]
		for x in bucket:
			if x.key == key:
				print (x.value)

	def setValue(self, key, value):
		h = self.hash(key)
		self.array[h].append(KeyValue(key, value))
	
	def hash(self,key):
		i = 0
		total = 0
		while i < len(key):
			total = total + ord(key[i])
			i = i + 1
		return total % self.SIZE

	def even_out(self, array):
		for x in range(0, len(array)):
			while len(array[x]) > 1:
				for y in range(1, len(array[x])):
					w = x
					while len(array[x]) != 0:
						if x == len(array) - 1:
							x = 0
						else:
							x = x + 1	
					array[x].append(array[w][y])
		return array									

	def quicksort_function(self, array):
		less = []
		equal = []
		greater = []

		if len(array) > 1:
			pivot = array[0]
			for x in range(0 , len(array)):
				if array[x] < pivot:
					less.append(array[x])
				elif array[x] == pivot:
					equal.append(array[x])
				else:
					greater.append(array[x])
			return self.quicksort_function(less) + equal + self.quicksort_function(greater)

		else:
			return array

	def starts_with(self, array , key):
		z = self.even_out(self.array)
		x = self.quicksort_function(z)
		print (x)

		first = 0
		last = len(x) - 1
		found = False

		while not found:
			midpoint = (first + last) // 2
			print key[0], x[midpoint][0].key[0], midpoint
			if key[0] == x[midpoint][0].key[0]:
				while key[0] == x[midpoint][0].key[0]:
					while x[midpoint - 1][0].key[0] == x[midpoint][0].key[0]:
						midpoint = midpoint - 1
					if key in x[midpoint][0].key:
						print x[midpoint][0].key
						found = True
						print (x[midpoint][0].key) + ":",
						print (x[midpoint][0].value)
						midpoint = midpoint + 1
			else:
				print first, last, midpoint, key < x[midpoint][0].key
				if key < x[midpoint][0].key:
					last = midpoint - 1
				else:
					first = midpoint + 1
				print first, last

phonebook = HashTable()
phonebook.setValue("Kavle", "641-713-1266")
phonebook.setValue("Kavya Anbarasu","359-921-4787")
phonebook.setValue("Home","232-631-8923")
phonebook.setValue("Hari","341-234-4821")
phonebook.setValue("Daddy","234-631-8981")
phonebook.setValue("Mommy","139-180-6532")
phonebook.lookup_number("Kavya Anbarasu")
phonebook.lookup_number("Home")
phonebook.lookup_number("Daddy")
phonebook.lookup_number("Hari")
phonebook.lookup_number("Mommy")
phonebook.starts_with(phonebook.array, "Kav")