import requests
from PIL import Image
import io

BASE_URL = "http://127.0.0.1:8080"

print("="*60)
print("Клієнтська частина для взаємодії з сервером завантаження")
print("="*60)

# 1. Створюємо тестове зображення
print("\n[1] Створення тестового зображення...")
test_image = Image.new('RGB', (200, 200), color='red')
image_bytes = io.BytesIO()
test_image.save(image_bytes, format='JPEG')
image_bytes.seek(0)

filename = 'test_image.jpg'
print(f"✓ Тестове зображення створено: {filename}")

# 2. POST запит - завантажуємо зображення на сервер
print(f"\n[2] POST запит до /upload")
print(f"    Завантажуємо файл: {filename}")

image_bytes.seek(0)
files = {'image': (filename, image_bytes, 'image/jpeg')}
response = requests.post(f"{BASE_URL}/upload", files=files)

print(f"    Статус: {response.status_code}")
print(f"    Відповідь: {response.json()}")

if response.status_code == 201:
    upload_response = response.json()
    image_url = upload_response['image_url']
    print(f"✓ Зображення успішно завантажено!")
    print(f"  URL: {image_url}")
else:
    print("✗ Помилка при завантаженні")
    exit(1)

# 3. GET запит - отримуємо URL зображення
print(f"\n[3] GET запит до /image/{filename}")
print(f"    Content-Type: text/plain")

headers = {'Content-Type': 'text'}
response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)

print(f"    Статус: {response.status_code}")
print(f"    Відповідь: {response.json()}")

if response.status_code == 200:
    get_response = response.json()
    retrieved_url = get_response['image_url']
    print(f"✓ URL успішно отримано!")
    print(f"  URL: {retrieved_url}")
else:
    print("✗ Помилка при отриманні URL")
    exit(1)

# 4. DELETE запит - видаляємо зображення з сервера
print(f"\n[4] DELETE запит до /delete/{filename}")

response = requests.delete(f"{BASE_URL}/delete/{filename}")

print(f"    Статус: {response.status_code}")
print(f"    Відповідь: {response.json()}")

if response.status_code == 200:
    delete_response = response.json()
    print(f"✓ Зображення успішно видалено!")
    print(f"  Повідомлення: {delete_response['message']}")
else:
    print("✗ Помилка при видаленні")
    exit(1)

# 5. Перевіряємо, що файл дійсно видалений
print(f"\n[5] Перевірка видалення файлу (GET запит)...")

headers = {'Content-Type': 'text'}
response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)

if response.status_code == 404:
    print(f"    Статус: {response.status_code}")
    print(f"✓ Файл дійсно видалений!")
else:
    print(f"    Статус: {response.status_code}")
    print(f"✗ Файл все ще існує!")

print("\n" + "="*60)
print("Тестування завершено успішно!")
print("="*60)
