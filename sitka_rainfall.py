from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates = []
rainfall = []

for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        prcp = float(row[5])  # PRCP column
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(prcp)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color="red", alpha=0.5)
ax.fill_between(dates, rainfall, facecolor="blue", alpha=0.2)

# Format plot.
ax.set_title("Daily Rainfall, 2021\nSitka, Alaska", fontsize=20)
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("Rainfall (inches)", fontsize=16)

fig.autofmt_xdate()

plt.show()
