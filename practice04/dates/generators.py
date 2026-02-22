from datetime import date
today = date.today()
print(today)



from datetime import date
today = date.today()
print(today.year)



from datetime import date
today = date.today()
print(today.month)



from datetime import date
today = date.today()
print(today.day)



from datetime import date
d = date(2026, 1, 1)
print(d)



from datetime import date
d1 = date(2026, 1, 1)
d2 = date(2026, 1, 10)
print(d2 - d1)




from datetime import date, timedelta
today = date.today()
new_date = today + timedelta(days=5)
print(new_date)



from datetime import date, timedelta
today = date.today()
new_date = today - timedelta(days=7)
print(new_date)



from datetime import datetime
now = datetime.now()
print(now.hour)



from datetime import date
today = date.today()
birthday = date(2026, 5, 1)
print(birthday - today)