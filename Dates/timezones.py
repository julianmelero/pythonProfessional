from datetime import datetime
import pytz


spain_timezone = pytz.timezone('Europe/Madrid')

spain_date = datetime.now(spain_timezone)

print(spain_date.strftime('%d/%m/%Y, %H:%M:%S'))


