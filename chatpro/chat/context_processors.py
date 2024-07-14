# chat/context_processors.py
from firebase_admin import db

def firebase(request):
    return {
        'firebase': db.reference()  # Adjust based on your Firebase setup
    }
