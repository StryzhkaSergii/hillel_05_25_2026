# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

single_quotes = [char for char in alice_in_wonderland if char == "'"]

print(f"Кількість символів: {len(single_quotes)}")
print(f"Символи: {single_quotes}")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402  # км²
azov_sea_area = 37800  # км²
total_area = black_sea_area + azov_sea_area # Разом площа двох морів

print("Разом Чорне та Азовське моря займають", total_area, "км².")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375291
sm1_sm2 = 250449
sm2_sm3 = 222950

sm3 = total - sm1_sm2
sm1 = total - sm2_sm3
sm2 = sm1_sm2 - sm1

print(f"Всього: {total} товарів")
print(f"Склад 1: {sm1} товарів")
print(f"Склад 2: {sm2} товарів")
print(f"Склад 3: {sm3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 1.5 * 12  # 1.5 року = 18 місяців
monthly_payment = 1179  # грн
total_price = months * monthly_payment  # Загальна вартість комп'ютера

print(f"Вартість комп'ютера: {int(total_price)} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"a) 8019 : 8 — остача:, {a}")
print(f"b) 9907 : 9 — остача:, {b}")
print(f"c) 2789 : 5 — остача:, {c}")
print(f"d) 7248 : 6 — остача:, {d}")
print(f"e) 7128 : 5 — остача:, {e}")
print(f"f) 19224 : 9 — остача:, {f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

total_money = pizza_big + pizza_medium + juice + cake + water

print(f"Піца велика: {pizza_big} грн")
print(f"Піца середня: {pizza_medium} грн")
print(f"Сік: {juice} грн")
print(f"Торт: {cake} грн")
print(f"Вода: {water} грн")
print(f"Всього потрібно: {total_money} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
per_page = 8

pages = photos // per_page

print(f"Фотографій: {photos}")
print(f"Фото на сторінці: {per_page}")
print(f"Потрібно сторінок: {pages}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600  # км
fuel_per_100km = 9  # літрів
tank_capacity = 48  # літрів

total_fuel = (distance / 100) * fuel_per_100km
refuels = total_fuel // tank_capacity

print(f"1) Для подорожі потрібно {int(total_fuel)} літрів бензину.")
print(f"2) Родині потрібно заїхати на заправку щонайменше {int(refuels)} рази.")