''' 
Help Sofia write a decrypter for the passwords that Nikola will
encrypt through the cipher map. A cipher grille is a 4×4 square of
paper with four windows cut out. Placing the grille on a paper sheet
of the same size, the encoder writes down the first four symbols of
his password inside the windows (see fig. below). After that, the
encoder turns the grille 90 degrees clockwise. The symbols written
earlier become hidden under the grille and clean paper appears inside
the windows. The encoder then writes down the next four symbols of the
password in the windows and turns the grille 90 degrees again. Then,
they write down the following four symbols and turns the grille once
more. Lastly, they write down the final four symbols of the password.
Without the same cipher grille, it is difficult to discern the
password from the resulting square comprised of 16 symbols. Thus, the
encoder can be confident that no hooligan will easily gain access to
the locked door. Write a module that enables the robots to easily
recall their passwords through codes when they return home. The cipher
grille and the ciphered password are represented as an array (tuple)
of strings.

How it is used: Here you can learn how to work with 2D arrays. You
also get to learn about the ancient Grille Cipher, a technique of
encoding messages which has been used for half a millenium. The
earliest known description of the grille cipher comes from the Italian
mathematician, Girolamo Cardano in 1550.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string. 

Precondition: 
len(cipher_grille) == 4 
len(ciphered_password) == 4 
all(len(row) == 4 for row in ciphered_password) 
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password) 
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

'''

def rotate_grille(grille):
	rotated = []
	for i in range(len(grille)):
		row = ""
		for j in reversed(range(len(grille))):
			row += grille[j][i]
		rotated.append(row)
	return rotated

def recall_password_my_sln(cipher_grille, ciphered_password):
	passwd = []
	for _ in cipher_grille:
		for grille, phrase in zip(cipher_grille, ciphered_password):
			passwd.extend([phrase[pos] for pos, char in enumerate(grille) if char == 'X'])
		cipher_grille = rotate_grille(cipher_grille)

	return ''.join(passwd)

def recall_password_online_sln(grill, cypher):
    password = ""
    for _ in grill:  # must be of len 4
        for grill_row, cypher_row in zip(grill, cypher):
            for grill_letter, cypher_letter in zip(grill_row, cypher_row):
                if grill_letter == 'X':
                    password += cypher_letter
        row1, row2, row3, row4 = grill
        grill = tuple(zip(row4, row3, row2, row1))  # rotate
    return password

cipher_grille = (
	'X...',
	'..X.',
	'X..X',
	'....'
	)

ciphered_password = (
	'itdf',
	'gdce',
	'aton',
	'qrdi'
	)

password = recall_password_my_sln(cipher_grille, ciphered_password)
print(password)
password = recall_password_online_sln(cipher_grille, ciphered_password)
print(password)

cipher_grille = (
	'....',
	'X..X',
	'.X..',
	'...X'
	)

ciphered_password = (
	'xhwc',
	'rsqx',
	'xqzz',
	'fyzr'
	)

password = recall_password_my_sln(cipher_grille, ciphered_password)
print(password)
password = recall_password_online_sln(cipher_grille, ciphered_password)
print(password)