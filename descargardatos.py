import requests 

def descargar_y_guardar(url, nombre_archivo):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(respuesta.text)
        print(f"descarga completada. Datos guardados en {nombre_archivo}")
    else:
        print(f"Error al cargar los datos de la base de datos: {respuesta.status_code}")

url_de_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo_csv = "heart_failure_dataset.csv"
descargar_y_guardar(url_de_datos, nombre_archivo_csv) 
     
        