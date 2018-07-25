import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('plcr.csv')


print df.groupby('Type')['Aboard', 'Fatalities'].sum().sort(['Fatalities'],ascending = 0).plot(kind='line', subplots = True)
