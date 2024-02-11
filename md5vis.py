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

    dataset={}

    for x in range(iterations):
        tohash=hashandint(tohash)
        dataset.update({x:tohash})

    keys = list(dataset.keys())
    vals = list(dataset.values())

    fig,ax=plt.subplots(2)


    ax[index].plot(range(len(dataset)),vals)
    ax[index].set_title(seed)

plotmd5("testkuh", 10, 0)
plotmd5("almananlage", 10, 1)
plt.show()