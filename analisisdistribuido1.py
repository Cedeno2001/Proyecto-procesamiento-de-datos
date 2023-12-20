import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos_limpio_y_preparados.csv")
plt.figure(figsize=(20, 12))
plt.hist(df['age'], bins=40, color='skyblue', edgecolor='black')
plt.title('distribucion de edades')
plt.xlabel('edad')
plt.ylabel('frecuencias')
plt.show()
grupos = ['sex', 'anemia', 'diabetes', 'smoking', 'DEATH_EVENT']
nombres = ['Hombres', 'Mujeres']
for i in grupos:
    plt.figure(figsize=(20, 12))
    for j, valor in enumerate(df[i].unique()):
        subconjunto = df[df[i] == valor]
        plt.bar(subconjunto['sex'].unique() + j * 0.4, subconjunto['sex'].value_counts(), width=0.4, label=f'{valor}')
    plt.title(f'Histograma de {i} por genero')
    plt.xlabel('genero')
    plt.ylabel('cantidad')
    plt.xticks([0.2, 1.2], nombres)
    plt.legend()
    plt.show()
        