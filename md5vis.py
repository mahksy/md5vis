import seaborn as sns
import hashlib
import pandas as pd
import matplotlib.pyplot as plt

def hashandint(input):
    input=str(input)
    md5hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    return int(md5hash,16)



def plotmd5(seed, iterations, index, overlay):
    tohash = seed
    #index+=1
    dataset={}

    for interation in range(iterations):
        tohash=hashandint(tohash)
        dataset.update({interation:tohash})

    keys = list(dataset.keys())
    vals = list(dataset.values())



    plt.plot(range(len(dataset)),vals)
    plt.title(seed)
    plt.tight_layout(pad=1.0)

iterations = 100
words = ["python", "3", "heckin", "rocks", "hell", "yeah"]
overlay = False


for x in words:
    print(words.index(x)+1)
    if overlay == True:
        plotmd5(x, iterations,0,overlay)
        plt.title(words)
        plt.subplot(1,1,1)
        
        
    else:
        plotmd5(x, iterations,words.index(x),overlay) 
        plt.subplot(len(words),1,words.index(x))
        #print(words.index(x))
plt.show()