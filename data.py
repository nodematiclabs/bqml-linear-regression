import pandas as pd
import random
from datetime import datetime, timedelta

# Define a function to generate a random date
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

start = datetime(2023, 1, 1)
end = datetime(2023, 7, 8)

date_list = []

# Generate 100 random dates
for _ in range(100):
    random_dt = random_date(start, end)
    date_list.append(random_dt.strftime('%b %d, %Y'))

# Sort the date list
date_list.sort(key=lambda date: datetime.strptime(date, '%b %d, %Y'))

percentage_list = []

# Generate 100 random but increasing percentages
for i in range(100):
    percentage_list.append(round(i*random.random(), 2))

# Create a dataframe
df = pd.DataFrame({
    'Date': date_list,
    'Cases Closed': percentage_list
})

# Write the dataframe to a CSV file
df.to_csv('data.csv', index=False)
