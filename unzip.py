import argparse
import zipfile

def unzip(filepath,words):
    with zipfile.ZipFile(filepath) as zip:
        try:
            for word in words:
                if word != None:
                    zip.extractall(pwd=word.encode())
                else:
                    zip.extractall()
        except Exception as e:
            print (e)
            
def getwords(dictionaryFilePath):
    words = list()
    with open(dictionaryFilePath) as f:
        for word in f:
	        words.append(word.rstrip())
    return words

def main():
    parser = argparse.ArgumentParser(description='Unzips a file.')
    parser.add_argument('filepath', help='The path to the zipfile to extract.')
    parser.add_argument('dictionaryFilePath',help='The path to the dictionary file to use.')
    args = parser.parse_args()
    words = getwords(args.dictionaryFilePath)

    unzip(args.filepath,words)

main()
