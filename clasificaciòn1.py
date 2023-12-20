import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
df = df.drop(columns=['categoria_edad'], errors='ignore')
plt.figure(figsize=(8, 6))
sns.countplot(x='DEATH_EVENT', data=df)
plt.title('distribuciòn de clases')
plt.show()

X = df.drop(columns=['DEATH_EVENT']).values
Y = df['DEATH_EVENT'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, Y_train)
y_pred = tree_model.predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)
print(f"àrbol de decisiòn:{accuracy}")
