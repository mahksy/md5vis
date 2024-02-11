import seaborn as sns
import hashlib
import pandas as pd
import matplotlib.pyplot as plt

def hashandint(input):
    input=str(input)
    md5hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    return int(md5hash,16)



def plotmd5(seed, iterations, index):
    tohash = seed
    index+=1
    dataset={}

    for interation in range(iterations):
        tohash=hashandint(tohash)
        dataset.update({interation:tohash})

    keys = list(dataset.keys())
    vals = list(dataset.values())

    plt.subplot(len(words),1,index)


    plt.plot(range(len(dataset)),vals)
    plt.title(seed)

iterations = 100

words =["yeet", "roar", "damn", "flup"]

for x in words:
    plotmd5(x, iterations,words.index(x))
    print(words.index(x))


plt.show()