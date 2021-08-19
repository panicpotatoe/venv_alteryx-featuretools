#https://featuretools.alteryx.com/en/stable/getting_started/using_entitysets.html
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

#%% adding entities with entity_id='products'
# entity_id is any name based on your choice
es = es.entity_from_dataframe(entity_id='products',
                              dataframe=products_df,
                              index='product_id')
print('es')
print(es) #there will be no relationship
print('es[\'products\'].variables')
print(es['products'].variables) #use entity_id you defined above

#%% adding relationship
new_relationship = ft.Relationship(es['products']['product_id'],
                                   es['transactions']['product_id'])
es = es.add_relationship(new_relationship)
print('es')
print(es) #now relationship exists

#%% using the EntitySet
feature_matrix, feature_defs = ft.dfs(entityset=es,
                                      target_entity='products')
print('the feature_matrix')
print(feature_matrix.sample(5))
print('the feature_defs[18]')
print(feature_defs[18])
print('the feature_defs[18] lineage graphs')
ft.graph_feature(feature_defs[18], to_file='../viz/demo-2.2-def18_graphviz.png')
print('the feature_defs[18] describe')
print(ft.describe_feature(feature_defs[18]))