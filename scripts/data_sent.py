import pandas as pd

# Read the CSV file
df = pd.read_csv('packetSent.csv')  # Replace with your file path

# Group by 'client_id' and sum the 'value' for each client
result = df.groupby('client_id')['value'].sum().reset_index()
# result = df['value'].sum()

# Save the result to a new CSV file
result.to_csv('dataSent.csv', index=False)
print(result)

# print("Output saved to 'dataSent.csv'")