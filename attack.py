import argparse
from passlib import hash
from hmac import compare_digest as compare_has

def crack(users, words):
    cracked = {}
    for user in users:
        parts = user.split(':')
        username = parts[0]
        salt_hashedpwd = parts[1]
        salt = salt_hashedpwd[:2]

        for word in words:
            hashed_word = hash.des_crypt.hash(word,salt=salt)
            if hashed_word == salt_hashedpwd:
                cracked[username] = word
    return cracked

def getwords(dictionaryFilePath):
    words = list()
    with open(dictionaryFilePath) as f:
        for word in f:
	        words.append(word.rstrip())
    return words

def getusers(passwordFilePath):
    users = list()
    with open(passwordFilePath) as f:
        for user in f:
	        users.append(user.rstrip())
    return users

def main():
    parser = argparse.ArgumentParser(
        description='Attempts to guess unix passwords with dictionary attack.')
    parser.add_argument('dictionaryFilePath',
                        help='The path to the dictionary file to use.')
    parser.add_argument('passwordFilePath',
                        help='The path to the dictionary file to use.')
    args = parser.parse_args()
    words = getwords(args.dictionaryFilePath)
    users = getusers(args.passwordFilePath)
    cracked = crack(users, words)
    if len(cracked) > 0:
        print("Passwords found: {<username>: <password>}")
        print(cracked)
    else:
        print("No passwords found.")
main()
