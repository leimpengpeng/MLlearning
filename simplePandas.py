import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})
ax = plt.gca()

# df.plot(kind='bar', x='name', y='age', ax=ax)
# df.plot(kind='line',x='name',y='num_children',ax=ax)
# df.plot(kind='line',x='name',y='num_pets', color='red')
df.groupby('state')['name'].nunique().plot(kind='bar')

plt.show()
# the plot gets saved to 'output.png'


# Plot date histogram

df = pd.DataFrame({
    'name':[
        'john','lisa','peter','carl','linda','betty'
    ],
    'date_of_birth':[
        '01/21/1988','03/10/1977','07/25/1999','01/22/1977','09/30/1968','09/15/1970'
    ]
})
plt.savefig('output.png')
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],infer_datetime_format=True)

plt.clf()
df['date_of_birth'].map(lambda d: d.month).plot(kind='hist')
plt.show()