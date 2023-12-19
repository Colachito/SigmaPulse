import subprocess
import time
import firebase_admin
from firebase_admin import credentials, storage

# Inicializar la app de Firebase
cred = credentials.Certificate("sigmapulse-tech-firebase-adminsdk-93slm-5d2a80f414.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'sigmapulse-tech.appspot.com'})

# Obtener una referencia al bucket
bucket = storage.bucket()

# Reproducir archivos desde la memoria RAM
def reproducir_archivo_desde_ram(archivo_ram):
    # Ejemplo utilizando OMXPlayer (puede variar dependiendo del reproductor)
    # Asegúrate de tener instalado OMXPlayer
    subprocess.Popen(['omxplayer', '--live', archivo_ram])

# Lógica para descargar y reproducir archivos directamente desde la memoria RAM
def descargar_y_reproducir_desde_ram(nombre_archivo):
    # Obtener el blob del bucket de Firebase
    blob = bucket.get_blob(nombre_archivo)
    if blob:
        # Descargar el archivo desde Firebase Storage
        contenido = blob.download_as_string()
        
        # Ejemplo: reproducir el archivo desde la memoria RAM
        reproducir_archivo_desde_ram(contenido)

# Configuración del nombre del bucket
nombre_bucket = 'sigmapulse-tech.appspot.com'

# Lógica para descargar y reproducir archivos continuamente
def descargar_y_reproducir_continuamente():
    while True:
        # Obtener una lista de todos los archivos en tu bucket de Firebase Storage
        blobs = list(bucket.list_blobs())

        # Iterar sobre los archivos y descargarlos uno por uno
        for blob in blobs:
            # Descargar y reproducir cada archivo
            descargar_y_reproducir_desde_ram(blob.name)
            
        time.sleep(10)  # Espera 10 segundos antes de volver a verificar

# Llamar a la función para descargar y reproducir continuamente
descargar_y_reproducir_continuamente()
