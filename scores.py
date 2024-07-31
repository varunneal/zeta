import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

# Read data
dates, scores = [], []
with open('data.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))
        scores.append(int(row[1]))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot_date(dates, scores)#, '-')

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gcf().autofmt_xdate() # Rotation

plt.xlabel('Date')
plt.ylabel('Score')
plt.title('Score Over Time')
plt.tight_layout()
plt.show()
