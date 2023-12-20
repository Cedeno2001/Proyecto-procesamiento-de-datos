import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
df = df.drop(columns=['categoria_edad'], errors='ignore')
X = df.drop(columns=['DEATH_EVENT'])
Y = df['DEATH_EVENT']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, Y_train)
y_pred = rf_model.predict(X_test) 
conf_matrix = confusion_matrix(Y_test, y_pred)
accuracy = accuracy_score(Y_test, y_pred)

f1 = f1_score(Y_test, y_pred)

print("Confusion de matriz!")
print(conf_matrix)
print("accuracy:", accuracy)
print("f1_score:", f1)