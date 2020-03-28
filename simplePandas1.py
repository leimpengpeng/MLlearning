import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PastHires.csv")
print(df.head(10))
print(df[['Interned', 'Hired']][5:])
print(df.sort_values(['Years Experience']))


degree_counts = df['Level of Education'].value_counts()
print(degree_counts)
degree_counts.plot(kind='bar')

plt.show()
print ('please, show my graph')
