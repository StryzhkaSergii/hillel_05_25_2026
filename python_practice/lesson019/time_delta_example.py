from datetime import datetime, timedelta, UTC
import pytz

todayUtc = datetime.now(UTC)
todayLocal = pytz.timezone("Europe/Kyiv").localize(datetime.now())
print(todayUtc)
print(todayLocal)
print(todayLocal - todayUtc)

today = datetime.now()
print(today)
seven_days_ago = today - timedelta(days=7, hours=2)
print(seven_days_ago)