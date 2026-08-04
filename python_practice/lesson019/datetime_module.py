from datetime import datetime

row1 = "2026-08-03 19:49:59" #UTC ISO format
row2 = "24-08-03T7:49:40.200 PM" #UTC
row3 = "24-08-03 19:49:40.200 -0200" #TZ -2

# print(datetime.now())
# print(type(datetime.now()))

# row1_dt = datetime.fromisoformat(row1)
# row2_dt = datetime.fromisoformat(row2) не ISO формат
row1_dt = datetime.strptime(row1, "%Y-%m-%d %H:%M:%S")
row2_dt = datetime.strptime(row2, "%y-%m-%dT%I:%M:%S.%f %p")
row3_dt = datetime.strptime(row3, "%y-%m-%d %H:%M:%S.%f %z")
# print(row1_dt)
# print(row1_dt.date())
# print(row1_dt.time())
# print(type(row1))
# print(type(row1_dt))
print(row2_dt)
print(row3_dt)
print(row2_dt.tzinfo)
print(row2_dt.tzname())

print(row3_dt.tzinfo)
print(row3_dt.tzname())

str_row3 = datetime.strftime(row3_dt, "%H:%M:%S")
print(str_row3)
print(type(str_row3))