from datetime import datetime, date
now = datetime.now()
today = date.today()
current_date = today.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
print("Current Time: ", current_time)
print("Current Date: ", current_date)

