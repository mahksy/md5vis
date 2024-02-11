import seaborn as sns
import hashlib
import pandas as pd
import matplotlib.pyplot as plt


tohash = "hi"

dataset={}


def hashandint(input):
    input=str(input)
    md5hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    return int(md5hash,16)



for x in range(1,1000):
    tohash=hashandint(tohash)
    dataset.update({x:tohash})

keys = list(dataset.keys())
vals = list(dataset.values())

plt.plot(range(len(dataset)),vals)
plt.show()
