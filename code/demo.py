import os
os.system('pip install featuretools')
os.system('pip install graphviz')

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

# Specify a dictionary with all entities in dataset
entities = {
    'customers': (customers_df, 'customer_id'),
    'sessions': (sessions_df, 'session_id', 'session_start'),
    'transactions': (transactions_df, 'transaction_id', 'transaction_time')
}

# Specify how entities are related
relationships = [
    # Link 'customer_id' in 'sessions' to 'customer_id' in 'transactions'
    ('sessions', 'session_id', 'transactions', 'session_id'),
    # Link 'customer_id' in 'customers' to 'customer_id' in 'sessions'
    ('customers', 'customer_id', 'sessions', 'customer_id')]

# Run Deep Feature Synthesis target_entity='customers'
feature_matrix_customers, customer_features_defs = ft.dfs(
    entities=entities,
    relationships=relationships,
    target_entity='customers')
print('the feature_matrix_customers')
print(feature_matrix_customers.sample(5))
print('the customer_features_defs[18]')
print(customer_features_defs[18])
print('the customer_features_defs[18] lineage graphs')
ft.graph_feature(customer_features_defs[18], to_file='../viz/demo_customer-features-def18_graphviz.png')
print('the customer_features_defs[18] describe')
print(ft.describe_feature(customer_features_defs[18]))

# Run Deep Feature Synthesis target_entity='sessions'
feature_matrix_sessions, session_features_defs = ft.dfs(
    entities=entities,
    relationships=relationships,
    target_entity='sessions')
print('the feature_matrix_sessions')
print(feature_matrix_sessions.sample(5))
print('the session_features_defs[18]')
print(session_features_defs[18])
print('the session_features_defs[18] lineage graphs')
ft.graph_feature(session_features_defs[18], to_file='../viz/demo_session-features-def18_graphviz.png')
print('the session_features_defs[18] describe')
print(ft.describe_feature(session_features_defs[18]))

# Run Deep Feature Synthesis target_entity='transactions'
feature_matrix_transactions, transaction_features_defs = ft.dfs(
    entities=entities,
    relationships=relationships,
    target_entity='transactions')
print('the feature_matrix_transactions')
print(feature_matrix_transactions.sample(5))
print('the transaction_features_defs[18]')
print(transaction_features_defs[18])
print('the transaction_features_defs[18] lineage graphs')
ft.graph_feature(transaction_features_defs[18], to_file='../viz/demo_transaction-features-def18_graphviz.png')
print('the transaction_features_defs[18] describe')
print(ft.describe_feature(transaction_features_defs[18]))