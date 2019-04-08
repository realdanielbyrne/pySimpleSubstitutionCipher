import argparse
import zipfile

def getwords(dictionaryFilePath):
    words = list()
    with open(dictionaryFilePath) as f:
        for word in f:
	        words.append(word.rstrip())
    return words


def unzip(filepath,words):
    with zipfile.ZipFile(filepath) as zip:
        for word in words:
            try:        
                zip.extractall(pwd=word.encode())
                print ("The password has been cracked!!!")
                print ("The password is: '" + word +"'")
                return True
            except Exception:
                print ("Bad password '" + word + "'")
        print("Password not cracked.")
        return False

def main():
    parser = argparse.ArgumentParser(description='Attempts to crack an encrypted zip file using a dictionary attack.')
    parser.add_argument('filepath', help='The path to the zipfile to extract.')
    parser.add_argument('dictionaryFilePath',help='The path to the dictionary file to use.')
    args = parser.parse_args()
    words = getwords(args.dictionaryFilePath)
    unzip(args.filepath,words)

main()
