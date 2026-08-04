import requests
import sys

BASE_URL = "https://images-api.nasa.gov"

# 1. Пошук зображень
print("=== Крок 1: Пошук зображень ===", flush=True)
sys.stdout.flush()

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params, timeout=10)
response.raise_for_status()
print(f"HTTP запит 1: GET {search_url}", flush=True)
print(f"Статус: {response.status_code}\n", flush=True)

data = response.json()
items = data["collection"]["items"]

# Витягуємо nasa_id
nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

print(f"Знайдено {len(nasa_ids)} об'єктів", flush=True)
print(f"NASA IDs: {nasa_ids[:5]}...\n", flush=True)

# 2. Отримання URL зображень
print("=== Крок 2: Отримання списків файлів ===", flush=True)

image_urls = []
request_count = 1

for nasa_id in nasa_ids:
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    response = requests.get(asset_url, timeout=10)
    response.raise_for_status()
    request_count += 1
    print(f"HTTP запит {request_count}: GET {asset_url}", flush=True)
    print(f"Статус: {response.status_code}", flush=True)

    asset_data = response.json()
    files = asset_data["collection"]["items"]

    # Шукаємо .jpg файл
    for file_item in files:
        href = file_item["href"]
        if href.endswith(".jpg"):
            image_urls.append(href)
            print(f"Знайдено JPG: {href[:60]}...", flush=True)
            break

    # Нам потрібно лише 2 фотографії
    if len(image_urls) == 2:
        print("", flush=True)
        break

print(f"\nВсього знайдено {len(image_urls)} JPG-зображень\n", flush=True)

# 3. Завантаження фотографій
print("=== Крок 3: Завантаження зображень ===", flush=True)

for index, url in enumerate(image_urls, start=1):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    request_count += 1
    print(f"HTTP запит {request_count}: GET {url[:60]}...", flush=True)
    print(f"Статус: {response.status_code}", flush=True)

    filename = f"mars_photo{index}.jpg"

    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"✓ {filename} ({len(response.content)} байт)\n", flush=True)

print(f"{'='*50}", flush=True)
print(f"Готово! Завантажено {len(image_urls)} зображень", flush=True)
print(f"Всього HTTP запитів: {request_count}", flush=True)
print(f"{'='*50}", flush=True)