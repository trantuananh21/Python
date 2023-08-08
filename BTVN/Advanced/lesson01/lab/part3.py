from datetime import datetime

class CustomDate:
    def get_date(self):
        date = datetime.now().strftime("%d/%m/%Y")
        return date
    
    def get_time(self):
        time = datetime.now().strftime("%H:%M:%S")
        return time
    
now = CustomDate()

print(now.get_date())
print(now.get_time())