import os
from watchdog.events import FileSystemEventHandler
from firebase_functions import storage, reproducir_archivo

class ManejadorCambios(FileSystemEventHandler):
    def __init__(self, carpeta_local, carpeta_firebase):
        self.carpeta_local = carpeta_local
        self.carpeta_firebase = carpeta_firebase
        self.archivos_locales = set()

    def on_created(self, event):
        if not event.is_directory:
            nuevo_archivo = event.src_path
            # Descargar nuevo archivo desde Firebase
            nombre_archivo = nuevo_archivo.split('/')[-1]
            archivo_firebase = f"{self.carpeta_firebase}/{nombre_archivo}"
            storage.child(archivo_firebase).download(nuevo_archivo)
            # Reproducir el nuevo archivo
            reproducir_archivo(nuevo_archivo)

    def on_deleted(self, event):
        if not event.is_directory:
            archivo_eliminado = event.src_path
            # Eliminar el archivo local
            os.remove(archivo_eliminado)

    def actualizar_archivos_locales(self):
        nuevos_archivos = set(os.listdir(self.carpeta_local))
        archivos_nuevos = nuevos_archivos - self.archivos_locales
        archivos_eliminados = self.archivos_locales - nuevos_archivos

        # Descargar nuevos archivos desde Firebase
        for archivo in archivos_nuevos:
            archivo_path = os.path.join(self.carpeta_local, archivo)
            archivo_firebase = f"{self.carpeta_firebase}/{archivo}"
            storage.child(archivo_firebase).download(archivo_path)
            # Reproducir el nuevo archivo
            reproducir_archivo(archivo_path)

        # Eliminar archivos locales eliminados en Firebase
        for archivo in archivos_eliminados:
            archivo_path = os.path.join(self.carpeta_local, archivo)
            os.remove(archivo_path)

        self.archivos_locales = nuevos_archivos
