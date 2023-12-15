import pandas as pd 
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

df = pd.DataFrame(data)

personas_fallecidas = df[df["is_dead"] == 1] 
personas_no_fallecidas = df[df["is_dead"] == 0]

promedio_edad_fallecidos = personas_fallecidas["age"].mean()
promedio_edad_no_fallecidas = personas_no_fallecidas["age"].mean()

print(f"promedio de edad de las personas fallecidas: {promedio_edad_fallecidos}")
print(f"promedio de edad de las personas no fallecida: {promedio_edad_no_fallecidas}")

tipos_de_datos = df.dtypes
print("Tipos de datos:")
print(tipos_de_datos)

if 'is_male' in df.columns and 'is_smoker' in df.columns:
    fumadores_por_genero = df.groupby(['is_male', 'is_smoker']).size().unstack()
    print("\ncantidad de hombres y mujeres fumadores:")
    print(fumadores_por_genero)
else:
    print("las columnas'is_male' y 'is_smoker' no estan presentes en el dataframe.")