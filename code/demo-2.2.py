#https://featuretools.alteryx.com/en/stable/getting_started/using_entitysets.html#creating-entity-from-existing-table
import featuretools as ft

#%% load mock data
data = ft.demo.load_mock_customer()

#%% split into dataframes
products_df = data['products']
print('products_df.sample(5)')
print(products_df.sample(5))

customers_df = data['customers']
print('customers_df.sample(5)')
print(customers_df.sample(5))

transactions_df = data['transactions']
print('transactions_df.sample(5)')
print(transactions_df.sample(5))

sessions_df = data['sessions']
print('sessions_df.sample(5)')
print(sessions_df.sample(5))

#%% merge `transactions`, `sessions`, and `customers` into `transactions_df`
transactions_df = data['transactions'].merge(data['sessions']).merge(data['customers'])
print('transactions_df.sample(10)')
print(transactions_df.sample(10))

#%% create an EntitySet
es = ft.EntitySet(id='customer_data')

#%% adding entities with entity_id='transactions'
# entity_id is any name based on your choice
es = es.entity_from_dataframe(entity_id='transactions',
                              dataframe=transactions_df,
                              index='transaction_id', #something like primary key
                              time_index='transaction_time',
                              variable_types={'product_id': ft.variable_types.Categorical,
                                              'zip_code': ft.variable_types.ZIPCode})
print('es')
print(es) #there will be no relationship
print('es[\'transactions\'].variables')
print(es['transactions'].variables) #use entity_id you defined above

#%% create entity from existing table - 'sessions' entity
es = es.normalize_entity(base_entity_id='transactions',
                         new_entity_id='sessions',
                         index='session_id',
                         make_time_index='session_start',
                         additional_variables=['device', 'customer_id',
                                               'zip_code', 'session_start',
                                               'join_date'])
print('es')
print(es) #now relationship exists

print('es[\'transactions\'].variables')
print(es['transactions'].variables)

print('es[\'sessions\'].variables')
print(es['sessions'].variables)

#%% create entity from existing table - 'customer' entity
es = es.normalize_entity(base_entity_id='sessions',
                         new_entity_id='customers',
                         index='customer_id',
                         make_time_index='join_date',
                         additional_variables=['zip_code', 'join_date'])
print('es')
print(es) #now relationship exists

print('es[\'sessions\'].variables')
print(es['sessions'].variables)

print('es[\'customers\'].variables')
print(es['customers'].variables)
