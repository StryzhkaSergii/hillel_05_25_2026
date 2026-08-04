import time

print(time.time()) #кількість секунд з 1970
print(time.localtime()) #повертає об'єкт дати

cur_date = time.localtime()


print(cur_date.tm_year)
print(cur_date.tm_mon)
print(cur_date.tm_mday)
print(cur_date.tm_zone)
print(cur_date.tm_sec)

print(f"Now is {cur_date.tm_hour}:{cur_date.tm_min}:{cur_date.tm_sec}")

# cur_time_sec = time.time()
# time.sleep(3.5) #почекати n секунд
# print(f"Diff was {time.time() - cur_time_sec}")

#wait 10 seconds
cur_time = time.time()
while time.time() - cur_time < 10:
    print("sending request...")
    time.sleep(1)

print(time.time())
time.sleep(5)
print(time.time())