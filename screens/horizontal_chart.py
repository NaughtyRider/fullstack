import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('fullstack/screens/daily_activity_data.csv')
data['date'] = pd.to_datetime(data['date'])

# Create a 'month' column
data['month'] = data['date'].dt.strftime('%m-%Y')
# Count the occurrences of each activity
print(len(data))
month='02-2025'
data = data[data['month']==month]
print(len(data))
activity_counts = data['activity'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
activity_counts.plot(kind='bar', color='skyblue')
plt.title('Daily Activities Distribution')
plt.xlabel('Activity')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.grid(axis='y', linestyle='--')

# Show the bar chart
plt.tight_layout()  # Adjust layout for better spacing
plt.show()