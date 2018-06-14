from datetime import datetime
delta = datetime.now() - datetime(1900,12,31)
print(delta.days)
print(delta.seconds)
print(datetime.now())