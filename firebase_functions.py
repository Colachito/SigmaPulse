from firebase_admin import credentials, initialize_app, storage as fb_storage
import io
from dotenv import load_dotenv
import os

load_dotenv()

ruta_credenciales = "sigmapulse-tech-firebase-adminsdk-93slm-5d2a80f414.json"
# Cargar las credenciales de Firebase desde el archivo json

firebase_cred = credentials.Certificate(ruta_credenciales)
# Inicializar la app con las credenciales cargadas

# Configuración de Firebase
firebase_config = {
   "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID")
}

firebase = initialize_app(firebase_cred, firebase_config)

storage = fb_storage.bucket()
