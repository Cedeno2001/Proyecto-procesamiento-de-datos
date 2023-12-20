import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
X = df.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'], errors='ignore')
if 'age' in df.columns:
    Y = df['age'].values
    model = LinearRegression()
    model.fit(X, Y)
    y_pred = model.predict(X)
    mse = mean_squared_error(Y, y_pred)
    print(f"Error! Cuadratico del medio: {mse}")
    
else:
    print("la columna age no se encuentra en el dataframe!")

