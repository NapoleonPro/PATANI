import os
from app import app, db
from routes.models import User
from werkzeug.security import generate_password_hash
from datetime import datetime

# --- KONFIGURASI ADMIN ---
# Anda bisa mengubah password di sini jika mau
ADMIN_EMAIL = 'admin@patani.com'
ADMIN_PASSWORD = 'admin123'
# -------------------------

with app.app_context():
    # 1. Cek apakah admin sudah ada
    if User.query.filter_by(email=ADMIN_EMAIL).first():
        print(f"User admin dengan email '{ADMIN_EMAIL}' sudah ada.")
    else:
        # 2. Hash password
        hashed_password = generate_password_hash(ADMIN_PASSWORD, method='pbkdf2:sha256')

        # 3. Buat user admin baru
        admin_user = User(
            name='Admin Utama',
            dob=datetime.strptime('1990-01-01', '%Y-%m-%d'),
            gender='Lainnya',
            email=ADMIN_EMAIL,
            phone='0000000000',
            password=hashed_password,
            role='admin',
            region='Kantor Pusat'
        )

        # 4. Tambahkan ke database
        db.session.add(admin_user)
        db.session.commit()
        print(f"User admin '{ADMIN_EMAIL}' berhasil dibuat!")