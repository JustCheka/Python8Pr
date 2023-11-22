# Решение на сайте

'''import pandas as pd

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()
print(avg) '''

import pandas as pd

file1 = pd.read_csv("california_housing_train.csv")

file2 = file1[(file1['population'] >= 0) & (file1['population'] <= 500)]

avg = file2['median_house_value'].mean()
print(avg)
