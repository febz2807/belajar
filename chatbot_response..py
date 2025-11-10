def chatbot_response(user_input):
    if "halo" in user_input.lower():
        return "Halo juga! Apa abar?"
    elif "kabarmu" in user_input.lower():
        return "Aku baik, terima kasihsudh bertanya!"
    elif "siapa kamu"in user_input.lower():
        return "Aku chatbot sederhana buatan Febryanto Nugroho."
    else:
        return "Maaf, aku belum mengerti msudmu."