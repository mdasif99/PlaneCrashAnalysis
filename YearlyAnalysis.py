import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('plcr.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].apply(lambda x: x.year)
df['Number Of Crashes'] = 1
df1 = df.groupby('Year')['Number Of Crashes', 'Fatalities'].sum().plot(kind='bar', subplots = True)
plt.show()

df['Proportion of Fatalities to Aboard'] = df['Fatalities']/df['Aboard']
df['Proportion of Fatalities to Aboard'].plot(kind='line', subplots = True)
plt.show()

df2 = df.groupby('Type')['Number Of Crashes', 'Fatalities'].sum().sort(['Number Of Crashes', 'Fatalities'], ascending = True).iloc[-50:]
df2.plot(kind='bar', subplots = True)
plt.show()

plt.subplots_adjust( bottom = 0.45)
df2 = df.groupby('Operator')['Number Of Crashes', 'Fatalities'].sum().sort(['Number Of Crashes', 'Fatalities'], ascending = True).iloc[-50:]
df2.plot(kind='bar', subplots = True)
plt.subplots_adjust( bottom = 0.45)
plt.show()


df['Military Plane Crashes per Year'] = df['Operator'].str.contains('Military', regex = True)*1
df['Civilian Plane Crashes per Year'] = df['Accidents']-df['Military Plane Crashes per Year']
df.groupby('Year')['Military Plane Crashes per Year','Civilian Plane Crashes per Year'].sum().plot(kind='line', subplots = False)
plt.show()

