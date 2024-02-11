import seaborn as sns
import hashlib

tohash = "hellu"



def hashandint(input):
    input=str(input)
    md5hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    return int(md5hash,16)



for x in range(10):
    tohash=hashandint(tohash)
    print(tohash)