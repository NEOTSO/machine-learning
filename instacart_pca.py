import pandas as pd

aisles = pd.read_csv('./data/instacart/aisles.csv')
orders = pd.read_csv('./data/instacart/orders.csv')
products = pd.read_csv('./data/instacart/products.csv')
products.sort_values(by=['aisle_id'])
order_products__prior = pd.read_csv('./data/instacart/order_products__prior.csv')
table1 = pd.merge(aisles, products, on=['aisle_id'])
table2 = pd.merge(table1, order_products__prior, on=['product_id'])
table3 = pd.merge(table2, orders, on=['order_id'])
table4 = pd.crosstab(table3['user_id'], table3['aisle'])

print(table4)