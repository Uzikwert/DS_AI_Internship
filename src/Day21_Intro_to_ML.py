#Task 1: The Paradigm Shift (Traditional vs. Machine Learning)
print("Introduction to Machine Learning:-")
print("Machine learning is a sub field of artificial intelligence where a model is trained to give the output without explicitly mentioning the rules to it. Input data is provided and the machine figures out the rules by itself.")
print("Machine learning can be categorized into 3 types:\n1. Supervised learning - Here labelled data is used for building the model. Example use cases: prediction, classification, etc.\n2. Unsupervized learning - Unlabelled data is utilized. Example use cases: clustering.\n3. Reinforcement learning - Model learning is based on a reward-penalty system. Example use cases: robotics, games, etc.")

#Task 2: The Three Branches of ML
import pandas as pd
df = pd.read_csv('Housing.csv')
X = df.drop('price',axis=1)
Y = df['price']
print(X)
print(Y)