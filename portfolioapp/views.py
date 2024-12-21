from django.shortcuts import render, redirect
from .models import Project, Contact
import requests
from django.utils import timezone

# Telegram bot token va chat ID
TELEGRAM_BOT_TOKEN = '7786775435:AAEWbhz7slYCHMLDnTjmZ1Ec5Cil2903v2Y'
TELEGRAM_CHAT_ID = '6225572459'

def index(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Contact modeliga ma'lumotni saqlash
        contact = Contact.objects.create(name=name, email=email, message=message)

        # Telegramga yuborish
        send_to_telegram(contact)

        return redirect('/')  # Bosh sahifaga qaytish

    return render(request, 'index.html', {'projects': projects})

def send_to_telegram(contact):
    message_text = f"""
    📝 Yangi Kontakt Xabari:
    🔹 Ismi: {contact.name}
    📧 Email: {contact.email}
    💬 Xabar: {contact.message}
    📅 Sana: {contact.date_submitted.strftime('%Y-%m-%d %H:%M:%S')}
    """

    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message_text,
        'parse_mode': 'HTML',
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(f"Xabar muvaffaqiyatli yuborildi: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Telegramga yuborishda xatolik: {e}")
        if 'response' in locals():
            print(f"Xatolik ma'lumotlari: {response.text}")
