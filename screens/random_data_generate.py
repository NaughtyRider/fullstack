import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Generate sample data
def generate_activity_data(num_records):
    activities = ['Running', 'Reading', 'Coding', 'Walking', 'Gaming', 'Cooking', 'Sleeping', 'Exercise']
    data = []

    for _ in range(num_records):
        date = fake.date_between(start_date='-30d', end_date='today')  # Random date in the last 30 days
        from_time = fake.time()  # Random time for start
        # Ensure to_time is after from_time
        from_datetime = datetime.combine(date, datetime.strptime(from_time, "%H:%M:%S").time())
        duration = random.randint(15, 180)  # Duration in minutes
        to_datetime = from_datetime + timedelta(minutes=duration)
        to_time = to_datetime.time()  # Convert back to time format
        activity = random.choice(activities)
        
        data.append([date, from_time, to_time, activity])

    return data

# Save to CSV
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'from_time', 'to_time', 'activity'])  # Header
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    num_records = 100  # Specify the number of records you want to generate
    activity_data = generate_activity_data(num_records)
    save_to_csv(activity_data, 'daily_activity_data.csv')
    print(f'Sample data generated and saved to daily_activity_data.csv')