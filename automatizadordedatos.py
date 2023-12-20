import sys 
import pandas as pd
import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(respuesta.text)
        print(f"Descarga exitosa!! Datos guardados en {nombre_archivo}")
    else:
        print(f"Error al descargar la base de datos, datos guardados en: {respuesta.status_code}")
        
def limpieza_y_preparacion(datos):
    faltantes = datos.isnull().sum()
    print("Valores faltantes:")
    print(faltantes)
    
    datos = datos.drop_duplicates()
    datos = datos[datos['age'] >= 0]
    
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor']
    datos['edad_categoria'] = pd.cut(datos['age'], bins=bins, labels=labels, right=False)
    
    datos.to_csv("datos_limpio_y_preparados.csv", Index=False)
    print("Limpieza y preparcion completada! Resultados guardados en datos_limpio_y_preparados.csv")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("automatizadordedatos.py <url>")
        sys.exit(1)
    url_datos = sys.argv[1]
    descargar_y_guardar_csv(url_datos, "datosdescargados.csv")
    
    df = pd.read_csv("datosdescargados.csv")
    
    limpieza_y_preparacion
    
    