from django.shortcuts import render, redirect
from .models import ChatMessage
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/cabrio/chatpro/groupchat-a8352-firebase-adminsdk-nrog7-2be436307d.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://groupchat-a8352-default-rtdb.firebaseio.com'
    })

def index(request):
    ref = db.reference('messages')
    messages = ref.order_by_child('timestamp').get()
    chat_messages = []
    if messages:
        for key, value in messages.items():
            chat_messages.append(ChatMessage(user=value['user'], message=value['message'], timestamp=value['timestamp']))
        chat_messages.sort(key=lambda x: x.timestamp)
    return render(request, 'chat/index.html', {'messages': chat_messages})

def send_message(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        message = request.POST.get('message')
        
        # Save message to Firebase Realtime Database
        ref = db.reference('messages')
        new_message_ref = ref.push({
            'user': user,
            'message': message,
            'timestamp': datetime.utcnow().isoformat()
        })
        
        # Save message to Django database (optional)
        ChatMessage.objects.create(user=user, message=message)
        
        return redirect('index')
    return redirect('index')
