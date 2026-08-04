from datetime import datetime, UTC
import time
import pytz

row3 = "24-08-03 19:49:40.200"

row3_dt = datetime.strptime(row3, "%y-%m-%d %H:%M:%S.%f")


data = datetime.now(UTC)
# data = datetime.utcnow() #deprecated
print(data.tzname())

cur_time_with_tz = time.localtime()
print(cur_time_with_tz.tm_zone)
print("-"*80)
client_time = "24-08-03 19:49:40.200"
server_time = "24-08-03 19:49:40.200+00:00"

# print(pytz.all_timezones) #отримати список усіх таймзон


client_time_dt = datetime.strptime(client_time, "%y-%m-%d %H:%M:%S.%f")
server_time_dt = datetime.strptime(server_time, "%y-%m-%d %H:%M:%S.%f%z")
client_time_dt_with_tz = pytz.timezone("Europe/Kyiv").localize(client_time_dt) #important



print(client_time_dt)
print(client_time_dt_with_tz.tzname())
diff_in_time = server_time_dt - client_time_dt_with_tz
print(type(diff_in_time))
print(diff_in_time.days)

# assert diff_in_time == 0, "Error, differance should be 0"