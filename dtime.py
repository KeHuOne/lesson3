#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta

today = datetime.now()
today.strftime('%d.%m.%Y %H:%M')
print(today)

yesterday = today - timedelta(days=1)
print(yesterday)

month_ago = today - timedelta(days=30)
print(month_ago)

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)
