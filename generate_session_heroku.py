"""
سكريبت لتوليد String Session على Heroku مباشرة
سيطلب منك إدخال رقم الهاتف ورمز التحقق
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

# استخدام المتغيرات من Heroku
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

print("=" * 70)
print("🔐 مولد String Session لـ Telegram")
print("=" * 70)
print("\n📝 ملاحظات:")
print("- سيُطلب منك رقم الهاتف (مثال: +9627XXXXXXXX)")
print("- ثم رمز التحقق من Telegram")
print("- إذا كان لديك التحقق بخطوتين، سيُطلب كلمة المرور\n")

try:
    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        session_string = client.session.save()
        
        print("\n" + "=" * 70)
        print("✅ تم توليد الـ String Session بنجاح!")
        print("=" * 70)
        print("\n📋 الآن نفذ الأمر التالي في Heroku CLI:")
        print("\nheroku config:set SESSION_STRING=\"" + session_string + "\"")
        print("\n" + "=" * 70)
        print("💡 أو من Dashboard:")
        print("Settings -> Config Vars -> Add")
        print("Key: SESSION_STRING")
        print("Value: " + session_string[:50] + "...")
        print("=" * 70)
        
except Exception as e:
    print(f"\n❌ حدث خطأ: {e}")
    print("تأكد من صحة API_ID و API_HASH")
