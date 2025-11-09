# ==========================================================
# Project: prediksi Harga Rumah Menggunakan Machine Learning
# Penulis: Febryanto Nugroho
# Progam Studi Teknik Informatika
# ===========================================================

# --- 1. Import Library ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.matrics import mean_absolute_error, mean_squared_error, r2_score

# --- 2. Dataset Sederhana (contoh manual) ---
# Misalnya kita punya data rumah dengan luas, jumlah kamar, dam harga
data = {
    'Luas (m2)': [100, 150, 200, 250, 300, 350, 400, 450],
    'Jumlah Kamar':[3, 3, 4, 4, 5, 5, 6, 6],
    'harga (juta)': [500, 650, 800, 950, 1100, 1250, 1400, 1550]
}

df = pd.DataFrame(data)
print("=== Data Awal ===")
print(df)

# --- 3. Pisahkan Fitur dan Target ---
x = df[['Lusa (m2)', 'Jumlah Kamar']]
y = df['Harga (juta)']

#--- 4. Bagi Data Model Linear Regression ---
model = LinearRegression()
model.fit(X_train, y_train)

#---6. Prediksi ---
y_pred = model.predict(X_test)

#---7. Evaluasi Model ---
print("\n=== Evaluasi Model ===")
print("Mean Absolute Error", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error :", mean_squared_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))

# ---8. Bandingkan Nilai Asli vs Prediksi---
hasil = pd.DataFrame({'Asli': y_test.values, 'Prediksi': y_pred})
print(hasil)

# --- 9. Visualisas ---
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test], color='red', linestyle='--')
plt.ylabel("Harga Prediksi (juta)")
plt.title("Perbandingan Harga Asli vs Prediksi")
plt.show()

#--- 10.Uji Prediksi Rumah Baru---
print("\n=== Prediksi Rumah Baru===")
luas_baru = 30
kamar_baru = 5
harga_prediksi = model.predict([[luas_baru, kamar_baru]])
print(f"Prediksi harga rumah dengan luas {luas_baru} m2 dan {kamar_baru} kamar: {harga_prediksi[0]:.2f} juta")
