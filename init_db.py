import os
import psycopg2
import urllib.parse as urlparse

# استخراج معلومات الاتصال من Heroku DATABASE_URL
url = urlparse.urlparse(os.environ['DATABASE_URL'])

conn = psycopg2.connect(
    dbname=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cursor = conn.cursor()

print("🔧 جاري إنشاء الجداول...")

# إنشاء جدول المستخدمين
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    username TEXT,
    order_id TEXT,
    language TEXT DEFAULT NULL,
    verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
print("✅ تم إنشاء جدول users")

# إنشاء جدول الطلبات
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_code TEXT UNIQUE,
    is_banned BOOLEAN DEFAULT FALSE
);
""")
print("✅ تم إنشاء جدول orders")

# إنشاء جدول السجل
cursor.execute("""
CREATE TABLE IF NOT EXISTS usage_log (
    id SERIAL PRIMARY KEY,
    order_id TEXT,
    user_id BIGINT,
    username TEXT,
    account TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
print("✅ تم إنشاء جدول usage_log")

conn.commit()
conn.close()

print("🎉 تم إنشاء جميع الجداول بنجاح!")
