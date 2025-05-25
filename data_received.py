import pandas as pd

# Read the CSV file
df = pd.read_csv('packetReceived.csv')  # Replace with your file path

# Group by 'client_id' and sum the 'value' for each client
result = df.groupby('client_id')['value'].sum().reset_index()

# Save the result to a new CSV file
result.to_csv('dataReceived.csv', index=False)

print("Output saved to 'dataReceived.csv'")