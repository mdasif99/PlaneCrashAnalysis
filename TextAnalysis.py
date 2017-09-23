import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk import FreqDist
from nltk.corpus import stopwords
import string 
from nltk import bigrams
from nltk import SnowballStemmer

df = pd.read_csv('plcr.csv')


stop = stopwords.words('english')
stop.extend(['plane','crashed','aircraft','en','route'])

def remove_punctuation(s):
    exclude = set(string.punctuation)
    s = ''.join([i for i in s if i not in exclude])
    return s


t = df[['Summary','Fatalities']].dropna()
book = t['Summary'].str.lower().apply(remove_punctuation).str.split().values.sum()
#print book
wrd = [w for w in book if w not in stop]
#print wrd

bigrams = list(bigrams(wrd))
fd = FreqDist(bigrams)
#print fdistBigram
#ax.subplots_adjust(bottom = .25)
df1 = pd.DataFrame({'Pair of Consecutive Words':fd.keys(), 'Number of Occurences':fd.values()})
df1 = df1.sort('Number of Occurences' ,ascending = True)[-30:]
ax = df1.plot(x='Pair of Consecutive Words',y = 'Number of Occurences', kind = 'barh')



for i, v in enumerate(list(df1['Number of Occurences'])):
    ax.text(v + 3, i-.26, str(v), color='blue')



plt.subplots_adjust(left = 0.25, bottom = 0.25)











plt.show()
#df1 = df1.set_index('Bigrams')
#df1 = df1.sort_values().iloc[-10:]
#df1 = df1.groupby('Bigrams')['Occurences'].sum()
#'Bigrams':df1.index



print df1.columns
#fdist = FreqDist(wrd)
#fdist.plot(50,cumulative = True)


