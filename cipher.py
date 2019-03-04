import sys 
import argparse

def encrypt(plaintext, k):
	cipher = ''
	
	for letter in plaintext:
		c = ord(letter)
		
		if (c >= 65 and c <= 90):
			c = (c + k) % 91
			if c < 65:
				c+=65

		elif (c >= 97 and c <= 122):
			c = (c + k) % 123
			if c < 97:
				c+=97
			
		cipher += chr(c)
		
	print ('Your encrypted message is: ' + cipher)

def decrypt(ciphertext, k):
	plaintext = ''
	
	for letter in ciphertext:
		c = ord(letter)		
		
		if (c >= 65 and c <= 90):
			c = (c-k-64) % (90-64) + 64
			if c < 65:
				c += 66

		elif (c >= 97 and c <= 122):
			c = (c-k-96) % (122-96) + 96
		
		plaintext +=chr(c)

		
	print ('Your plain text message is: ' + plaintext)

def obfuscate(message):
	obfuscated = ''

	for letter in message:
		c = ord(letter)

		if (c >= 65 and c <= 90):
			c = 88
		elif (c >= 97 and c <= 122):
			c = 120
			
		obfuscated += chr(c)

	print ('Your obfuscated message is: ' + obfuscated)

def main():
	parser = argparse.ArgumentParser(description='Encrypts plaintext or decrypts ciphertext.')
	parser.add_argument('message', help='The message to be either encrypted or decrypted.')
	parser.add_argument('-o', action='store_true', help="Obfuscate a message by replacing every lowercase character with an x, and every uppercase character with an X.")
	parser.add_argument('-k', nargs='?', default = 3, const = 3, help='The Ceasar cipher rotation key. Default = 3.')
	parser.add_argument('-d', help='Decrypt a plaintext message. Default action is to encrypt', action='store_true')

	args = parser.parse_args()

	if args.o:
		obfuscate(args.message)
	elif args.d:
		decrypt(args.message, int(args.k))
	else:
		encrypt(args.message, int(args.k))

main()