from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

class DateHandler:
    def format_date(input):
        date = input.strftime("%d/%m/%Y")
        return date
    
    def get_days_between(start, end):
        return (end - start).days
    

print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:",
       DateHandler.get_days_between(start_date, end_date))

