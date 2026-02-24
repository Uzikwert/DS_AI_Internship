import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PHASE 1: The Detective Work

df=pd.read_csv("customer_analytics (1).csv")
print(df.head())
#First 5 rows of the dataset can be observed by the analyst
print(df.info())
#Datatype and number of non-null values of columns is displayed
print(df.describe())
#Provides count, mean, standard deviation, min and max value of each column
print("The dataset represents 205 customer data with features such as age, annual income, purchase amount, prefered devices, etc")

#PHASE 2: The Cleanup

print(df.isnull().sum())
#Gets the sum of number of null values in each column
df = df.drop(columns=['Education'])
print("Dropping the Education Column beacuse it doesn't have much significance in our dataset")
df["AnnualIncome"]=df["AnnualIncome"].fillna(df["AnnualIncome"].mean())
print("Replacing all the null values with the mean of the annual income\nTaking mean because it helps preserve the overall average of the column")
print("Duplicates",df.duplicated().sum())
#Checks for duplicate values in the dataset
df=df.drop_duplicates()
#Drops all the duplicate values in the dataset as theyn can cause error while prediction
print("Duplicates:",df.duplicated().sum())
#Verifying that the rows have been dropped

#PHASE 3: The Deep Dive

sns.histplot(df["AnnualIncome"],kde=True)
plt.title("Histogram of'Annual Income'\nRight Skewed Distribution observed")
plt.xlabel('Income')
plt.ylabel('Count')
plt.show()

sns.countplot(x='Gender',data=df)
plt.title("Countplot of 'Gender Count'\nWell balanced gender ratio")
plt.xlabel('Gender')
plt.ylabel('Population')
plt.show()

sns.histplot(df["SpendingScore"],kde=True)
plt.title("Histogram of 'Spending Scrore'\nA well shaped and smooth curve, normally distributed")
plt.xlabel('Spending Score')
plt.ylabel('Count')
plt.show()


plt.scatter(x='Age',y='YearsEmployed',data=df)
plt.title('Age VS Years Employed\nStrong correlation between age and years employed')
plt.xlabel('Age')
plt.ylabel('Years Employed')
plt.show()

sns.boxplot(x=df['MaritalStatus'],y=df['LastPurchaseAmount'])
plt.title('Marital Statuts VS Last Purchase Amount\nSingle customer tend to spend more money on their purchases')
plt.xlabel('Marital Status')
plt.ylabel('Last Purchase Amount')
plt.show()

# PHASE 4: The Big Picture

corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
sns.heatmap(corr_matrix,annot=True,cmap='Blues')
plt.title('HeatMap of Correlation Matrix')
plt.show()
print("Executive Summary:")
print("1. Most bought device is tablet")
print("2. Most of our customers have an annual income of upto 100000")
print("3. Most features provided do not have high correlation at all, except age and years employed, having a strong positive correlation 0f 0.97")


df.to_csv('customer_analysis.csv', index=False)
#It reflects all the changes that were made onto the dataframe in a .csv file