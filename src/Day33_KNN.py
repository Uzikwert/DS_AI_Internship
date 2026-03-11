import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
 

# Load data
url='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
df=pd.read_csv(url)
X=df.drop("species", axis=1)
y=df['species']
# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 2. Initialize model
knn = KNeighborsClassifier(n_neighbors=5)

# 3. Fit model
knn.fit(X_train, y_train)

# 4. Predict
predictions = knn.predict(X_test)

# 5. Evaluate
acc = accuracy_score(y_test, predictions)
print(f"Final Accuracy: {acc:.4f}")
print(f"First 5 predictions: {predictions[:5]}")
print(f"First 5 actual labels: {y_test[:5]}")