import csv
import datetime
import os

def init(csv_file):
    if not os.path.exists(csv_file):
        with open(csv_file, 'w') as f: 
            csv_write = csv.writer(f)
            csv_head = ['Datum', 'Konto', 'Art', 'Betrag', 'Kategorie', 'Beschreibung']
            csv_write.writerow(csv_head)

def getDate():
    today = datetime.date.today()
    month_name = today.strftime('%B')
    year_name = today.strftime('%Y')
    last_month = today.replace(day=1) - datetime.timedelta(days=1)
    last_month_name = last_month.strftime('%B')
    return (month_name, year_name, last_month_name)
