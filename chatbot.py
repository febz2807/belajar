# ====================================
# Chatbot Sederhana
# ====================================
import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

# Sapaan dasar
if "hai" in user_input or "halo" in user_input or "hi" in user_input:
    return "Halo! Senang berbicara denganmu"

elif"nama kamu" in user_input:
    return "Saya adalah chatbot sederhana buatan Febryanto Nugroho"

elif "apa kabar" in user_input:
    return "Saya baik-baik saja! Terima kasih sudah bertanya"

elif "jam berapa" in user_input:
    now = datetime.datetime.now().strtime("%H:%M:%S")
    return f"Sekarang pukul {now}"

elif "hari apa" in user_input:
    today = datetime.datetime.now().strtime("%A")
    return f"hari ini adalah {today}"

elif "cuaca" in user_input:
    return "Saya tidak bisa melihat cuaca, tapi semoga hari ini cerah di tempatmu"

elif "terima kasih" in user_input:
    return "Sama-sama!"

elif "keluar" in user_input or "exit" in user_input:
    return "exit"

else:
    return "Maaf, saya belum mengerti pertanyaanmu. Coba lagi ya!"

# ==============================
# Program Utama
# ==============================

print("Chatbot Sederhana - by Febryanto Nugroho")
print("Ketik 'keluar' unutuk mengakhiri percakapan.")
print("="*50)

while True:
    user_input = input("Kamu: ")
    response = chatnot_response(user_input)
    if response == "exit":
        print("Chatbot: Sampai jumpa!")
        break
    else:
        print("Chatbot:", response)