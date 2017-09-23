import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk import FreqDist
from nltk.corpus import stopwords
import string 
from nltk import bigrams
import plotly
plotly.offline.init_notebook_mode()
import plotly.plotly as py


df = pd.read_csv('finally.csv')
print df.head()

#print df.head()
df1 = df.groupby('COUNTRY')['Cleaned Country'].sum().sort_values(ascending = True).iloc[-20:]
df2 = pd.DataFrame({'Country':df1.index, 'Number Of Plane Crashes':df1.values})
df2 = df2.set_index('Country')
ax = df2.plot(kind = 'barh', grid = True, xlim=[0,1500])
for i, v in enumerate(list(df2['Number Of Plane Crashes'])):
    ax.text(v + 10, i-.26, str(v), color='blue')


ax.set_xlabel = 'Number Of Plane Crashes' 
ax.set_ylabel = 'Country'
plt.subplots_adjust(left = 0.25, bottom = 0.25)
#plt.show()


data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['Cleaned Country'],
        text = df['COUNTRY'],
        colorscale = [[0,"rgb(5, 10, 0)"],[0.05,"rgb(40, 60, 40)"],[0.1,"rgb(70, 100, 100)"],\
            [0.15,"rgb(90, 120, 150)"],[0.2,"rgb(106, 137, 200)"],[1,"rgb(220, 220, 255)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = 'Number Of Crashes'),
      ) ]

layout = dict(
    title = 'Plane Crashes',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
plotly.offline.plot( fig, validate=False, filename='d5-world-map' )


