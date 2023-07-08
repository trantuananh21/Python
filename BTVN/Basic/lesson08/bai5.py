from datetime import datetime
now = datetime.now()
print(now)

print(now.strftime('Today is ' + '%Y/%m/%d'))
print(now.strftime('Time right now ' + '%H:%M:%S'))