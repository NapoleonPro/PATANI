import os


# --- Secret Key (harus diganti saat produksi) ---
SECRET_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyDo2Q29VmglZMKBYYTBDZPK4cGkTnXF8zM')

# --- Konfigurasi Database ---
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Gemastikusk23@localhost:5432/agrolldb')
SQLALCHEMY_TRACK_MODIFICATIONS = False
