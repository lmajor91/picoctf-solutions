#!/usr/bin/python3 -u
import signal
import string

"""
this encryption scheme seems to map each letter from plaintext
to a matrix which in turn yields a letter which is "encrypted"

plaintext gets mapped to a matrix which yields a number
"""

SQUARE_SIZE = 6

def print_matrix(matrix):
	for row in matrix:
		print("[", ", ".join(row), "]")

def generate_square(alphabet):
	"""
	this function generates a 2x2 matrix from a string,
	the matrix is formatted in a zigzag pattern from the string

	alphabet = string[]
	"""

	# the alphabet has to be 6^2=36 chars long
	# the alphabet has to have the same length as the matrix's dimension
	assert len(alphabet) == pow(SQUARE_SIZE, 2)

	# the return value
	matrix = []

	# building the matrix
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)

	# returning the matrix
	return matrix

def get_index(letter, matrix):
	"""
	this function looks for a letter within a given matrix and returns
	the row, col of where the letter was found.
	the PROGRAM WILL TERMINATE if the letter is NOT found

	letter = string
	matrix = string[][]
	"""
	# looking for the letter within the matrix
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				# letter found, return row column pair
				return (row, col)

	# literally exiting the program lmao
	print("letter not found in matrix.")
	exit()

def decrypt_pair(pair, matrix):
	"""
	this function takes a pair of letters and encrypts them

	pair = string[2]
	matrix = string[][]

	returns: char[2]
	"""
	p1 = get_index(pair[0], matrix) # char -> int[row, col]
	p2 = get_index(pair[1], matrix) # char -> int[row, col]

	# p1 = [0, 5]
	# p2 = [0, 4]

	def wrap(i, boundary = SQUARE_SIZE):
		ret = i - 1
		if i < 0:
			ret += boundary
		return ret

	# same row?
	if p1[0] == p2[0]:
	
		# since encryption goes to the right, we need to go left
		# right = +1, left = -1
		lchar = matrix[p1[0]][wrap(p1[1])]
		rchar = matrix[p2[0]][wrap(p2[1])]

	# same col?
	elif p1[1] == p2[1]:
		
		lchar = matrix[wrap(p1[0])][p1[1]]
		rchar = matrix[wrap(p2[0])][p2[1]]

	# neither?
	else:
		# matrix[0][4] + matrix[0][5]
		lchar = matrix[p1[0]][p2[1]]
		rchar = matrix[p2[0]][p1[1]]

	print('%s -> %s' % (pair, lchar + rchar))

	return lchar + rchar

def encrypt_pair(pair, matrix):
	"""
	this function takes a pair of letters and encrypts them

	pair = string[2]
	matrix = string[][]
	"""
	p1 = get_index(pair[0], matrix) # int[2] = [row, col]
	p2 = get_index(pair[1], matrix) # int[2] = [row, col]

	# same row?
	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1) % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1) % SQUARE_SIZE]

	# same col?
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1) % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1) % SQUARE_SIZE][p2[1]]

	# neither?
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def encrypt_string(s, matrix):
	"""
	takes a string, divides the string up into pairs, then
	encrypts each pair of numbers

	s = string[]
	matrix = string[][]
	"""

	# the encrypted result
	result = ""

	# padding the string if it is not an even number
	if len(s) % 2 == 0:
		# if there are an even number of "squares" within
		# the plaintext string
		plain = s
	else:
		# something weird, inlining a string for no reason
		# that string spits out "0", might be the contents
		# of "key"

		#plain = s + "0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q"[0]
		plain = s + "0"

	# encrypting the string
	for i in range(0, len(plain), 2):
		# this encrypts in pairs of two
		result += encrypt_pair(plain[i:i + 2], matrix)

	# returning the result
	return result

def decrypt_string(plain, matrix): # WIP
	"""
	takes a string, divides the string up into pairs, then
	decrypts each pair of letters

	s = string[], len % 2 = 0
	mapping = {string: string}
	"""

	# the decrypted result
	result = ""

	# decrypting the string
	for i in range(0, len(plain), 2):
		# this decrypts in pairs of two
		result += decrypt_pair(plain[i:i + 2], matrix)

	# returning the result
	return result

# reading the key, this is the "alphabet" of the program
alphabet = "0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q"

mapping = {}

# making some encryption box using an alphabet
m = generate_square(alphabet)

print_matrix(m)

# opening the message in plaintext
msg = "herfayo7oqxrz7jwxx15ie20p40u1i"

dec_msg = decrypt_string(msg, m)

print("here is the decrypted string:", dec_msg)
