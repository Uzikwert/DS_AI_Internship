import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# TASK 1: The Shape Shifter
print("TASK 1")
data={
      "heights": [172,166,162,185,158,167,163,170,168,166],
      "income":[60000,42000,95000,37000,80000,110000,65000,55000,45000,42000],
      "test":[40,78,68,89,87,62,94,95,57,79]
      }

df=pd.DataFrame(data)
plt.figure()
sns.histplot(df['heights'],kde=True)
plt.title('Normal')
plt.show()
plt.figure()
sns.histplot(df['income'],kde=True)
plt.title('Right-Skewed')
plt.show()
plt.figure()
sns.histplot(df['test'],kde=True)
plt.title('Left-skewed')
plt.show()

print(f'Mean of Human Heights is {df['heights'].mean()}\nMedian of Human Heights is {df['heights'].median()}\n(NORMAL MEAN AND MEDIAN)')
print('-'*50)
print(f'Mean of Household Income is {df['income'].mean()}\nMedian of Household Income is {df['income'].median()}\n(RIGHT SKEWED MEAN AND MEDIAN)')
print('-'*50)
print(f'Mean of Test Scores is {df['test'].mean()}\nMedian of  Test Scores is {df['income'].median()}\n(LEFT SKEWED MEAN AND MEDIAN)')
print('-'*50)

# TASK 2: The Outlier Detector
mean_height=df['heights'].mean()
std_heights=df['heights'].std()
df['z_score']=(df['heights']-mean_height)/std_heights
outliers=df[np.abs(df['z_score'])>2]
print(outliers)

# TASK 3: The Magic Averages
means=[]
for i in range(1000):
    sample=np.random.choice(data['income'], size=30)
    means.append(sample.mean())

plt.figure()
sns.histplot(means,kde=True)
plt.title("Right-Skewed Data after CLT")
plt.show()
