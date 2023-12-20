import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

df = pd.read_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
X = df.drop(columns=['DEATH_EVENT']).values
Y = df['DEATH_EVENT'].values
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

df_embedded = pd.DataFrame(X_embedded, columns=['componente 1', 'componente 2', 'componente 3'])
df_embedded['DEATH_EVENT'] = Y

fig = px.scatter_3d(df_embedded, x='componente 1', y='componente 2', z='componente 3', color='DEATH_EVENT')
fig.show()