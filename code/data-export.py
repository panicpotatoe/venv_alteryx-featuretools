# Load mock data
import featuretools as ft
data = ft.demo.load_mock_customer()

# Split mock data into dfs
customers_df = data['customers']
print('sample of customers_df')
print(customers_df.sample(5))

sessions_df = data['sessions']
print('sample of sessions_df')
print(sessions_df.sample(5))

transactions_df = data['transactions']
print('sample of transactions_df')
print(transactions_df.sample(5))

customers_df.to_csv('../dataset/customers_df.csv', index=False)
sessions_df.to_csv('../dataset/sessions_df.csv', index=False)
transactions_df.to_csv('../dataset/transactions_df.csv', index=False)